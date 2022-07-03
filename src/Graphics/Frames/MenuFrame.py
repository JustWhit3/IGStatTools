#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 21:33:00 2022
Author: Gianluca Bianco
"""

#############################################################
#    Modules
#############################################################

# Standard libraries
import tkinter as tk
import instaloader as ig
import glob
import threading
from PIL import ImageTk, Image
import shutil as sh

# Utils libraries
from Utils import GraphicsUtils as gu
from Utils import InstaloaderUtils as iu
from Utils import GenericUtils as gen

#############################################################
#    MenuFrame
#############################################################
class MenuFrame( tk.Frame ):
    """
    Class used to create the Menu frame.

    Args:
        tk (tkinter.Frame): inherits from tkinter.Frame class.
    """
    
    def __init__( self, window ):
        
        # Generic settings
        super().__init__( window )
        self.chosen_font = ( "Helvetica", 15 )
        self[ "bg" ] = "gray10"
        self[ "width" ] = 1800
        self[ "height" ] = 1500
        self.config( highlightbackground = "black", highlightthickness = 4 )
        self.place( anchor = "center", relx = 0.5, rely = 0.5 )
        
        # Progress spinner
        self.spinner_gif = gu.ImageLabel( self )
        self.spinner_gif.load( "../img/icons/spinner.gif", width = 80, height = 80 )
        self.spinner_gif.config( bg = "grey10" )
        gu.CreateToolTip( self.spinner_gif, "Loading..." )
        
        if glob.glob( "*/.session_cookies" ):
            self.Load( "on" )
            
    #############################################################
    #    SetButtonStyle
    #############################################################
    def SetButtonStyle( self, button ):
        """
        Method used to set the predefined buttons style.

        Args:
            button (tkinter.Button): the given button.
        """
        
        button.config(
            font = ( "Helvetica", 20, "bold" ),
            cursor = "hand2",
            width = 12,
            height = 2, 
            bg = "gray20", 
            fg = "white"
            )
        
    #############################################################
    #    SetLabelStyle
    #############################################################
    def SetLabelStyle( self, button ):
        """
        Method used to set the predefined labels style.

        Args:
            button (tkinter.Label): the given label.
        """
        
        button.config(
            font = ( "Helvetica", 15, "bold" ),
            bg = "gray10", 
            fg = "white"
            )
        
    #############################################################
    #    Load
    #############################################################
    def Load( self, save ):
        """
        Method used to load instagram profile information from Loading function.
        """

        self.save = save
        self.spinner_gif.place( anchor = "center", relx = 0.975, rely = 0.97 )
        self.tkraise()
        threading.Thread( target = self.Loading ).start()
        
    def Loading( self ):
        """
        Method used to load instagram profile information
        """

        # Variables
        username = ""
        self.loader = ig.Instaloader()

        # Loading instagram profile info
        if self.save == "on":
            for session_file in glob.glob( "*/.session_cookies" ):
                username = session_file.split( "/" )[0]
                self.loader.load_session_from_file( username, filename = session_file )
            self.profile = ig.Profile.from_username( self.loader.context, username )
        elif self.save == "off":
            pass
        
        # Downloading useful information
        self.loader.download_profilepic( self.profile )
        self.followers = iu.GetObjects( self.profile.get_followers() )
        self.followees = iu.GetObjects( self.profile.get_followees() )
        self.posts = iu.GetObjects( self.profile.get_posts() )
        self.likes, self.comments = iu.GetTotalLikesComments( self.profile )
        self.photos, self.videos = iu.GetTotalPhotosVideos( self.profile )
        self.score = gen.Score( self.followers.size, self.followees.size )
        
        # Other settings
        self.__create_widgets()
        self.spinner_gif.place_forget()    
        
    #############################################################
    #    __logout
    #############################################################
    def __logout( self ):
        """
        Function used to logout from the current profile.
        """
        
        sh.rmtree( self.profile.username )
        self.place_forget()
        
    #############################################################
    #    __refresh
    #############################################################
    def __refresh( self ):
        """
        Function used to refresh and restart the frame.
        """
        
        for widget in self.winfo_children():
            if widget != self.spinner_gif:
                widget.destroy()
                
        self.Load( "on" )

    #############################################################
    #    __create_widgets
    #############################################################
    def __create_widgets( self ):
        """
        Method used to create basic frame widgets.
        """
        
        # Logout button
        self.logout_img = ImageTk.PhotoImage( Image.open( "../img/icons/logout.ico" ).resize( ( 80, 80 ) ) )
        self.logout_button = tk.Button( self, image = self.logout_img, command = self.__logout )
        self.logout_button.config( command = None, cursor = "hand2", highlightthickness = 0, bd = 0, bg = "gray10" )
        gu.CreateToolTip( self.logout_button, text = "Logout" )
        self.logout_button.place( anchor = "center", relx = 0.024, rely = 0.97 ) 
        
        # Refresh button
        self.refresh_img = ImageTk.PhotoImage( Image.open( "../img/icons/refresh.png" ).resize( ( 60, 60 ) ) )
        self.refresh_button = tk.Button( self, image = self.refresh_img )
        self.refresh_button.config( command = self.__refresh, cursor = "hand2", highlightthickness = 0, bd = 0 )
        gu.CreateToolTip( self.refresh_button, text = "Refresh" )
        self.refresh_button.place( anchor = "ne", relx = 1, rely = 0 )

        # Placing profile pic at the center of the screen
        for profile_pic in glob.glob( "*/*profile_pic.jpg" ):
            self.profile_img = ImageTk.PhotoImage( Image.open( profile_pic ) )
            break
        self.profile_img_label = tk.Label( self, image = self.profile_img )
        self.profile_img_label[ "image" ] = self.profile_img
        self.profile_img_label.place( anchor = "center", relx = 0.5, rely = 0.5 )
        
        # Placing followers counter on the right
        self.followers_count = tk.Label( self, text = "{}".format( self.followers.size ) )
        self.followers_count.place( anchor = "center", relx = 0.3, rely = 0.47 )
        self.SetLabelStyle( self.followers_count )
        self.followers_count.config( font = ( "Helvetica", 20, "bold" ) )
        self.followers_label = tk.Label( self, text = "FOLLOWERS" )
        self.followers_label.place( anchor = "center", relx = 0.3, rely = 0.52 )
        self.SetLabelStyle( self.followers_label )
        
        # Placing followees counter on the left
        self.followees_count = tk.Label( self, text = "{}".format( self.followees.size ) )
        self.followees_count.place( anchor = "center", relx = 0.7, rely = 0.47 )
        self.SetLabelStyle( self.followees_count )
        self.followees_count.config( font = ( "Helvetica", 20, "bold" ) )
        self.followees_label = tk.Label( self, text = "FOLLOWEES" )
        self.followees_label.place( anchor = "center", relx = 0.7, rely = 0.52 )
        self.SetLabelStyle( self.followees_label )
        
        # Placing profile name on the top
        self.profile_name_label = tk.Label( self, text = self.profile.username )
        self.profile_name_label.place( anchor = "center", relx = 0.5, rely = 0.35 )
        self.SetLabelStyle( self.profile_name_label )
        self.profile_name_label.config( font = ( "Helvetica", 20, "bold" ) )
        
        # Placing posts counter on the bottom (0.1)
        self.posts_counter = tk.Label( self, text = "{}".format( self.posts.size ) )
        self.posts_counter.place( anchor = "center", relx = 0.1, rely = 0.70 )
        self.SetLabelStyle( self.posts_counter )
        self.posts_counter.config( font = ( "Helvetica", 20, "bold" ) )
        self.posts_label = tk.Label( self, text = "POSTS" )
        self.posts_label.place( anchor = "center", relx = 0.1, rely = 0.75 )
        self.SetLabelStyle( self.posts_label )
        
        # Placing photos counter on the bottom (0.3)
        self.photos_counter = tk.Label( self, text = "{}".format( self.photos ) )
        self.photos_counter.place( anchor = "center", relx = 0.3, rely = 0.70 )
        self.SetLabelStyle( self.photos_counter )
        self.photos_counter.config( font = ( "Helvetica", 20, "bold" ) )
        self.photos_label = tk.Label( self, text = "PHOTOS" )
        self.photos_label.place( anchor = "center", relx = 0.3, rely = 0.75 )
        self.SetLabelStyle( self.photos_label )
        
        # Placing videos counter on the bottom (0.5)
        self.videos_counter = tk.Label( self, text = "{}".format( self.videos ) )
        self.videos_counter.place( anchor = "center", relx = 0.5, rely = 0.70 )
        self.SetLabelStyle( self.videos_counter )
        self.videos_counter.config( font = ( "Helvetica", 20, "bold" ) )
        self.videos_label = tk.Label( self, text = "VIDEOS" )
        self.videos_label.place( anchor = "center", relx = 0.5, rely = 0.75 )
        self.SetLabelStyle( self.videos_label )
        
        # Placing likes counter on the bottom (0.7)
        self.likes_counter = tk.Label( self, text = "{}".format( self.likes ) )
        self.likes_counter.place( anchor = "center", relx = 0.7, rely = 0.70 )
        self.SetLabelStyle( self.likes_counter )
        self.likes_counter.config( font = ( "Helvetica", 20, "bold" ) )
        self.likes_label = tk.Label( self, text = "LIKES" )
        self.likes_label.place( anchor = "center", relx = 0.7, rely = 0.75 )
        self.SetLabelStyle( self.likes_label )
        
        # Placing comments counter on the bottom (0.9)
        self.comments_counter = tk.Label( self, text = "{}".format( self.comments ) )
        self.comments_counter.place( anchor = "center", relx = 0.9, rely = 0.70 )
        self.SetLabelStyle( self.comments_counter )
        self.comments_counter.config( font = ( "Helvetica", 20, "bold" ) )
        self.comments_label = tk.Label( self, text = "COMMENTS" )
        self.comments_label.place( anchor = "center", relx = 0.9, rely = 0.75 )
        self.SetLabelStyle( self.comments_label )
        
        # Placing app settings button (0.2)
        self.settings_button = tk.Button( self, text = "SETTINGS", command = None )
        self.settings_button.place( anchor = "center", relx = 0.2, rely = 0.2 )
        self.SetButtonStyle( self.settings_button )
        
        # Placing followers info button (0.5)
        self.followers_button = tk.Button( self, text = "FOLLOWERS", command = None )
        self.followers_button.place( anchor = "center", relx = 0.5, rely = 0.2 )
        self.SetButtonStyle( self.followers_button )
        
        # Placing profile stats button (0.7)
        self.stats_button = tk.Button( self, text = "STATISTICS", command = None )
        self.stats_button.place( anchor = "center", relx = 0.8, rely = 0.2 )
        self.SetButtonStyle( self.stats_button )
        
        # Placing profile rank
        self.profile_rank_label = tk.Label( self, text = "{}".format( self.score ) )
        self.profile_rank_label.place( anchor = "center", relx = 0.5, rely = 0.1 )
        self.SetLabelStyle( self.profile_rank_label )
        self.profile_rank_label.config( font = ( "Helvetica", 20, "bold" ) )