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
from lib2to3.pytree import Base
import tkinter as tk
from PIL import ImageTk, Image
import instaloader as ig

#############################################################
#    TogglePassword
#############################################################
def TogglePassword( password_entry, toggle_button ):
    """
    Function used to change visibility status while inserting a password.

    Args:
        password_entry (tkinter.Entry): the password entry.
        toggle_button (tkinter.Button): the toggle button.
    """
    
    # Variables
    global eye
    global hide
    eye = ImageTk.PhotoImage( Image.open( "../img/icons/eye.png" ).resize( ( 30, 30 ) ) )
    hide = ImageTk.PhotoImage( Image.open( "../img/icons/hide.png" ).resize( ( 30, 30 ) ) )
    
    # Toggle choice
    if password_entry.cget( "show" ) == "":
        password_entry.config( show = "*" )
        toggle_button.config( image = eye )
        toggle_button.image = eye
    else:
        password_entry.config( show = "" )
        toggle_button.config( image = hide )
        toggle_button.image = hide
        
#############################################################
#    SwitchToPasswd
#############################################################
def SwitchToPasswd( username_input, password_input ):
    """
    Function used to switch from username to password input.

    Args:
        username_input (tkinter.Entry): the username entry.
        password_input (tkinter.Entry): the password entry.
    """
    
    if username_input.get() != "":
        password_input.focus_set()

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
    global exception_label
    
    # Reset exception label
    try:
        exception_label.destroy()
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
#    RestartProgram
#############################################################
def RestartProgram( frame ):
    """
    Function used to restart a frame.

    Args:
        frame (tkinter.Frame): the frame to be restarted.
    """
    
    LoginFrame( frame )
    try:
        exception_label.destroy()
    except BaseException:
        pass

#############################################################
#    LoginFrame
#############################################################
def LoginFrame( login_frame ):
    
    # Variables
    global eye_img
    global refresh_img
    
    # Frame settings
    login_frame.config( highlightbackground = "black", highlightthickness = 4 )
    
    # Log in label
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
    eye_img = ImageTk.PhotoImage( Image.open( "../img/icons/eye.png" ).resize( ( 30, 30 ) ) )
    toggle_button = tk.Button( login_frame, image = eye_img )
    toggle_password = lambda: TogglePassword( password_input, toggle_button )
    toggle_button.place( anchor = "center", relx = 0.67, rely = 0.5 )
    toggle_button.config( command = toggle_password, cursor = "hand2", highlightthickness = 0, bd = 0, bg = "white" )
    
    # Login into account
    login = lambda event = 0: Login( login_frame, username_input, password_input, chosen_font )
    switch_to_passwd = lambda event = 0: SwitchToPasswd( username_input, password_input )
    username_input.bind( "<Return>", switch_to_passwd )
    password_input.bind( "<Return>", login )
    login_button = tk.Button( login_frame, text = "Authenticate", font = chosen_font, command = login )
    login_button.place( anchor = "center", relx = 0.5, rely = 0.55 )
    login_button.config( cursor = "hand2", width = 30, padx = -10, bg = "black", fg = "white" )
    
    # Refresh button
    refresh_img = ImageTk.PhotoImage( Image.open( "../img/icons/refresh.png" ).resize( ( 60, 60 ) ) )
    restart_program = lambda: RestartProgram( login_frame )
    refresh_button = tk.Button( login_frame, image = refresh_img )
    refresh_button.place( anchor = "ne", relx = 1, rely = 0 )
    refresh_button.config( command = restart_program, cursor = "hand2", highlightthickness = 0, bd = 0 )