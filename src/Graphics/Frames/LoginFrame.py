#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 15:20:00 2022
Author: Gianluca Bianco
"""

#############################################################
#    Modules
#############################################################

# Standard modules
import tkinter as tk
from PIL import ImageTk, Image
import instaloader as ig
import threading
import glob

# Utils modules
from Utils import GraphicsUtils as gu

#############################################################
#    LoginFrame
#############################################################
class LoginFrame( tk.Frame ):
    """
    Class used to create the Login frame.

    Args:
        tk (tkinter.Frame): inherits from tkinter.Frame class.
    """
    
    def __init__( self, window, controller ):
        """
        Main constructor of the class.

        Args:
            window (tkinter.Tk): the window hosting the frame.
        """
        
        super().__init__( window )
        self.controller = controller
    
        if glob.glob( "*/.session_cookies" ):
            self.controller.tkraise()
        
        self[ "width" ] = 1800
        self[ "height" ] = 1500
        self.config( highlightbackground = "black", highlightthickness = 4 )
        self.__create_widgets()
        self.place( anchor = "center", relx = 0.5, rely = 0.5 )
        
    #############################################################
    #    __create_widgets
    #############################################################
    def __create_widgets( self ):
        """
        Method used to create widgets.
        """
        
        # Progress spinner settings
        self.spinner_gif = gu.ImageLabel( self )
        self.spinner_gif.load( "../img/icons/spinner.gif", width = 40, height = 40 )

        # Log in label
        self.chosen_font = ( "Helvetica", 15 )
        self.login_label = tk.Label( self, text = "Log in", font = ( "Helvetica", 25 ) )
        self.login_label.place( anchor = "center", relx = 0.5, rely = 0.37 )

        # Username label and input
        self.username_label = tk.Label( self, text = "Username:", font = self.chosen_font )
        self.username_label.place( anchor = "center", relx = 0.37, rely = 0.45 )
        self.username_input = tk.Entry( self, font = self.chosen_font )
        self.username_input.place( anchor = "center", relx = 0.56, rely = 0.45 )
        self.username_input.focus_set()

        # Password label and input (with toggle)
        self.password_label = tk.Label( self, text = "Password:", font = self.chosen_font )
        self.password_label.place( anchor = "center", relx = 0.37, rely = 0.5 )
        self.password_input = tk.Entry( self, font = self.chosen_font  )
        self.password_input.place( anchor = "center", relx = 0.56, rely = 0.5 )
        self.password_input.config( show = "*" )
        self.eye_img = ImageTk.PhotoImage( Image.open( "../img/icons/eye.png" ).resize( ( 30, 30 ) ) )
        self.toggle_button = tk.Button( self, image = self.eye_img )
        self.toggle_password = lambda event = 0: self.TogglePassword()
        self.toggle_button.place( anchor = "center", relx = 0.67, rely = 0.5 )
        self.toggle_button.config( command = self.toggle_password, cursor = "hand2", highlightthickness = 0, bd = 0, bg = "white" )
        self.password_input.bind( "<Control-c>", self.toggle_password )

        # Login into account
        def login( event = 0 ):
            self.spinner_gif.place( anchor = "center", relx = 0.7, rely = 0.55 )
            threading.Thread( target = self.Login ).start()

        self.switch_to_passwd = lambda event = 0: self.SwitchToPasswd()
        self.username_input.bind( "<Return>", self.switch_to_passwd )
        self.username_input.bind( "<Down>", lambda event: self.password_input.focus_set() )
        self.password_input.bind( "<Return>", login )
        self.password_input.bind( "<Up>", lambda event: self.username_input.focus_set() )
        self.login_button = tk.Button( self, text = "Authenticate", font = self.chosen_font, command = login )
        self.login_button.place( anchor = "center", relx = 0.5, rely = 0.55 )
        self.login_button.config( cursor = "hand2", width = 30, padx = -10, bg = "black", fg = "white" )

        # Remember login button
        self.remember_login_label = tk.Label( self, text = "Remember me", font = ( "Helvetica", 13 ) )
        self.remember_login_label.place( anchor = "center", relx = 0.515, rely = 0.6 )
        self.remember_login_label.config( highlightthickness = 0, bd = 0 )
        self.button_size = ( 30, 30 )
        self.checkbutton_var = tk.IntVar()
        self.checkbutton_img = ImageTk.PhotoImage( Image.open( "../img/icons/checkbutton.png" ).resize( self.button_size) )
        self.checkbutton_img_tick = ImageTk.PhotoImage( Image.open( "../img/icons/checkbutton_tick.png" ).resize( self.button_size ) )
        self.remember_login_checkbutton = tk.Checkbutton( self, variable = self.checkbutton_var, onvalue = 1, offvalue = 0, command = None )
        self.remember_login_checkbutton.place( anchor = "center", relx = 0.435, rely = 0.598 )
        self.remember_login_checkbutton.config( indicatoron = False, image = self.checkbutton_img, selectimage = self.checkbutton_img_tick, cursor = "hand2", highlightthickness = 0, bd = 0, bg = "white" )
        self.remember_login_checkbutton[ "image" ] = self.checkbutton_img
        self.remember_login_checkbutton[ "selectimage" ] = self.checkbutton_img_tick

        # Refresh button
        self.refresh_img = ImageTk.PhotoImage( Image.open( "../img/icons/refresh.png" ).resize( ( 60, 60 ) ) )
        self.restart_program = lambda event = 0: self.RestartProgram()
        self.username_input.bind( "<Escape>", self.restart_program )
        self.password_input.bind( "<Escape>", self.restart_program )
        self.refresh_button = tk.Button( self, image = self.refresh_img )
        self.refresh_button.place( anchor = "ne", relx = 1, rely = 0 )
        self.refresh_button.config( command = self.restart_program, cursor = "hand2", highlightthickness = 0, bd = 0 )
        gu.CreateToolTip( self.refresh_button, text = "Refresh" )
        
    #############################################################
    #    Login
    #############################################################
    def Login( self ):
        """
        Method used to login into Instagram account.
        """

        # Variables
        loader = ig.Instaloader()
        username = self.username_input.get()
        password = self.password_input.get()
        
        def login_small():
            """
            Small function used to set-up login information.
            """
            
            if self.checkbutton_var.get() == 1:
                loader.save_session_to_file( "{}/.session_cookies".format( username ) )
            self.controller.profile = ig.Profile.from_username( loader.context, username )
            self.controller.Load( "off" )

        # Reset exception label
        try:
            self.exception_label.destroy()
        except BaseException:
            pass
        
        # Doing login
        try:
            if password == "" and username != "":
                raise BaseException( "Error: you forgot to insert the password." )
            elif username == "" and password != "":
                raise BaseException( "Error: you forgot to insert the username." )
            elif password == "" and username == "":
                raise BaseException( "Error: you forgot to insert username and password." )
            else:
                loader.login( username, password )
                login_small()

        # Exception for two-factor authentication
        except ig.exceptions.TwoFactorAuthRequiredException as e:
            self.exception_label = tk.Label( self, text = e, font = self.chosen_font )
            self.exception_label.place( anchor = "center", relx = 0.5, rely = 0.65 )
            self.exception_label.config( fg = "red" )

            self.twofactor_label = tk.Label( self, text = "Code(*):", font = self.chosen_font )
            self.twofactor_label.place( anchor = "center", relx = 0.38, rely = 0.70 )
            self.twofactor_input = tk.Entry( self, font = self.chosen_font  )
            self.twofactor_input.place( anchor = "center", relx = 0.56, rely = 0.70 )
            self.twofactor_input.focus_set()

            self.twofactor_message = "(*) Insert two-factor authentication code received by message/app."
            self.twofactor_star = tk.Label( self, text = self.twofactor_message, font = self.chosen_font )
            self.twofactor_star.place( anchor = "s", relx = 0.5, rely = 0.95 )

            def two_factor_login( event = 0 ):
                """
                Small function to deal with two-factor login.

                Args:
                    event (int, optional): variable used to enable the button. Defaults to 0.
                """

                twofactor_code = int( self.twofactor_input.get() )

                try:
                    self.exception_twof_label.destroy()
                except BaseException:
                    pass
                
                if self.twofactor_input.get() != "":
                    try:
                        loader.two_factor_login( twofactor_code )
                        login_small()
                    except BaseException as e:
                        self.exception_twof_label = tk.Label( self, text = e, font = self.chosen_font )
                        self.exception_twof_label.place( anchor = "center", relx = 0.5, rely = 0.80 )
                        self.exception_twof_label.config( fg = "red" )

                self.spinner_gif.place_forget()

            def TwoFactorLogin( event = 0 ):
                self.spinner_gif.place_forget()
                self.spinner_gif.place( anchor = "center", relx = 0.70, rely = 0.75 )
                threading.Thread( target = two_factor_login ).start()

            self.twofactor_input.bind( "<Return>", TwoFactorLogin )
            self.twofactor_input.bind( "<Escape>", self.restart_program )
            self.password_input.bind( "<Down>", lambda event: self.twofactor_input.focus_set() )
            self.twofactor_input.bind( "<Up>", lambda event: self.password_input.focus_set() )
            self.twofactor_login = tk.Button( self, text = "Authenticate with two-factor code", font = self.chosen_font, command = TwoFactorLogin )
            self.twofactor_login.place( anchor = "center", relx = 0.5, rely = 0.75 )
            self.twofactor_login.config( cursor = "hand2", width = 29, bg = "black", fg = "white" )

        except BaseException as e:
            self.exception_label = tk.Label( self, text = e, font = self.chosen_font )
            self.exception_label.place( anchor = "center", relx = 0.5, rely = 0.65 )
            self.exception_label.config( fg = "red" )

        self.spinner_gif.place_forget()
        
    #############################################################
    #    TogglePassword
    #############################################################
    def TogglePassword( self ):
        """
        Method used to change visibility status while inserting a password.
        """
        
        # Variables
        self.eye = ImageTk.PhotoImage( Image.open( "../img/icons/eye.png" ).resize( ( 30, 30 ) ) )
        self.hide = ImageTk.PhotoImage( Image.open( "../img/icons/hide.png" ).resize( ( 30, 30 ) ) )
        
        # Toggle choice
        if self.password_input.cget( "show" ) == "":
            self.password_input.config( show = "*" )
            self.toggle_button.config( image = self.eye )
            self.toggle_button[ "image" ] = self.eye
        else:
            self.password_input.config( show = "" )
            self.toggle_button.config( image = self.hide )
            self.toggle_button[ "image" ] = self.hide
            
    #############################################################
    #    SwitchToPasswd
    #############################################################
    def SwitchToPasswd( self ):
        """
        Method used to switch from username to password input.
        """

        if self.username_input.get() != "":
            self.password_input.focus_set()

    #############################################################
    #    RestartProgram
    #############################################################
    def RestartProgram( self ):
        """
        Method used to restart the frame.
        """

        self.spinner_gif.place_forget()

        LoginFrame( self, self.controller )

        try:
            self.exception_label.destroy()
            self.twofactor_star.destroy()
            self.twofactor_label.destroy()
            self.twofactor_input.destroy()
            self.twofactor_login.destroy()
            self.exception_twof_label.destroy()
        except BaseException:
            pass