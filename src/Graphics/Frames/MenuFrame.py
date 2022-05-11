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

# Utils libraries
from Utils import GraphicsUtils as gu

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
        
        super().__init__( window )
        self.chosen_font = ( "Helvetica", 15 )
        self[ "width" ] = 1800
        self[ "height" ] = 1500
        self.config( highlightbackground = "black", highlightthickness = 4 )
        self.place( anchor = "center", relx = 0.5, rely = 0.5 )
        self.spinner_gif = gu.ImageLabel( self )
        self.spinner_gif.load( "../img/icons/spinner.gif", width = 80, height = 80 )
        
        if glob.glob( "*/.session_cookies" ):
            self.Load( "on" )
        
    #############################################################
    #    Load
    #############################################################
    def Load( self, save ):
        """
        Method used to load instagram profile information from Loading function.
        """

        self.save = save
        self.spinner_gif.place( anchor = "center", relx = 0.975, rely = 0.97 )
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
        
        # Other settings
        self.tkraise()
        self.__create_widgets()
        self.spinner_gif.place_forget()    

    #############################################################
    #    __create_widgets
    #############################################################
    def __create_widgets( self ):
        """
        Method used to create basic frame widgets.
        """

        # placing profile pic at the center of the screen
        for profile_pic in glob.glob( "*/*profile_pic.jpg" ):
            self.profile_img = ImageTk.PhotoImage( Image.open( profile_pic ) )
            break
        self.profile_img_label = tk.Label( self, image = self.profile_img )
        self.profile_img_label[ "image" ] = self.profile_img
        self.profile_img_label.place( anchor = "center", relx = 0.5, rely = 0.5 )