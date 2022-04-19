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

# Utils modules
from Utils import GraphicsUtils as gu

#############################################################
#    Login
#############################################################
def Login( frame, username_input, password_input, chosen_font ):
    """
    Function used to login into Instagram account.

    Args:
        frame (tkinter.Frame): the working frame.
        username_input (str): the username.
        password_input (str): the password.
        chosen_font (tuple): a tuple with font information.

    Returns:
        instaloader.Profile: the instagram profile object.
    """
    
    # Variables
    loader = ig.Instaloader()
    username = username_input.get()
    password = password_input.get()
    
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
    except ig.exceptions.TwoFactorAuthRequiredException as e:
        exception_label = tk.Label( frame, text = e, font = chosen_font )
        exception_label.place( anchor = "center", relx = 0.5, rely = 0.60 )
        exception_label.config( fg = "red" )
        
        twofactor_label = tk.Label( frame, text = "Code(*):", font = chosen_font )
        twofactor_label.place( anchor = "center", relx = 0.36, rely = 0.65 )
        twofactor_input = tk.Entry( frame, font = chosen_font  )
        twofactor_input.place( anchor = "center", relx = 0.56, rely = 0.65 )
        twofactor_input.focus_set()
        
        twofactor_message = "(*) Insert two-factor authentication code received by message/app."
        twofactor_star = tk.Label( frame, text = twofactor_message, font = chosen_font )
        twofactor_star.place( anchor = "s", relx = 0.5, rely = 0.95 )
        
        def TwoFactorLogin( event = 0 ):
            """
            Function used to login using two-factor authentication factor.
            """
            
            twofactor_code = twofactor_input.get()
            if twofactor_input.get() != "":
                try:
                    loader.two_factor_login( twofactor_code )
                except BaseException as e:
                    exception_label = tk.Label( frame, text = e, font = chosen_font )
                    exception_label.place( anchor = "center", relx = 0.5, rely = 0.75 )
                    exception_label.config( fg = "red" )
        
        twofactor_input.bind( "<Return>", TwoFactorLogin )
        twofactor_login = tk.Button( frame, text = "Authenticate with two-factor code", font = chosen_font, command = TwoFactorLogin )
        twofactor_login.place( anchor = "center", relx = 0.5, rely = 0.7 )
        twofactor_login.config( cursor = "hand2", width = 30, bg = "black", fg = "white" )
    except BaseException as e:
        exception_label = tk.Label( frame, text = e, font = chosen_font )
        exception_label.place( anchor = "center", relx = 0.5, rely = 0.6 )
        exception_label.config( fg = "red" )

#############################################################
#    LoginFrame
#############################################################
def LoginFrame(login_frame):
    
    # Variables
    global eye_img
    
    # Login frame and label
    chosen_font = ( "Helvetica", 15 )
    login_label = tk.Label( login_frame, text = "Log in", font = ( "Helvetica", 25 ) )
    login_label.place( anchor = "center", relx = 0.5, rely = 0.37 )
    
    # Username label and input
    username_label = tk.Label( login_frame, text = "Username:", font = chosen_font )
    username_label.place( anchor = "center", relx = 0.36, rely = 0.45 )
    username_input = tk.Entry( login_frame, font = chosen_font )
    username_input.place( anchor = "center", relx = 0.56, rely = 0.45 )
    username_input.focus_set()
    
    # Password label and input (with toggle)
    password_label = tk.Label( login_frame, text = "Password:", font = chosen_font )
    password_label.place( anchor = "center", relx = 0.36, rely = 0.5 )
    password_input = tk.Entry( login_frame, font = chosen_font  )
    password_input.place( anchor = "center", relx = 0.56, rely = 0.5 )
    password_input.config( show = "*" )
    eye_img = ImageTk.PhotoImage( Image.open( "../img/eye.png" ).resize( ( 30, 30 ) ) )
    toggle_button = tk.Button( login_frame, image = eye_img )
    toggle_password = lambda: gu.TogglePassword( password_input, toggle_button )
    toggle_button.place( anchor = "center", relx = 0.675, rely = 0.5 )
    toggle_button.config( command = toggle_password, cursor = "hand2", highlightthickness = 0, bd = 0, bg = "white" )
    
    # Login into account
    login = lambda event = 0: Login( login_frame, username_input, password_input, chosen_font )
    SwitchToPasswd = lambda event = 0: gu.SwitchToPasswd( username_input, password_input )
    username_input.bind( "<Return>", SwitchToPasswd )
    password_input.bind( "<Return>", login )
    login_button = tk.Button( login_frame, text = "Authenticate", font = chosen_font, command = login )
    login_button.place( anchor = "center", relx = 0.5, rely = 0.55 )
    login_button.config( cursor = "hand2", width = 30, padx = -10, bg = "black", fg = "white" )