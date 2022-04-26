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

# Utils modules
from Utils import GraphicsUtils as gu

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
#    RestartProgram
#############################################################
def RestartProgram( frame ):
    """
    Function used to restart a frame.

    Args:
        frame (tkinter.Frame): the frame to be restarted.
    """
    
    spinner_gif.place_forget()
    
    LoginFrame( frame )
    
    try:
        exception_label.destroy()
        twofactor_star.destroy()
        twofactor_label.destroy()
        twofactor_input.destroy()
        twofactor_login.destroy()
        exception_twof_label.destroy()
    except BaseException:
        pass

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
    global twofactor_star
    global twofactor_input
    global twofactor_login
    global twofactor_label
    
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
            if checkbutton_var.get() == 1:
                loader.save_session_to_file( "{}/.session_cookies".format( username ) )
            frame.place_forget()
            
    # Exception for two-factor authentication
    except ig.exceptions.TwoFactorAuthRequiredException as e:
        exception_label = tk.Label( frame, text = e, font = chosen_font )
        exception_label.place( anchor = "center", relx = 0.5, rely = 0.65 )
        exception_label.config( fg = "red" )
        
        twofactor_label = tk.Label( frame, text = "Code(*):", font = chosen_font )
        twofactor_label.place( anchor = "center", relx = 0.38, rely = 0.70 )
        twofactor_input = tk.Entry( frame, font = chosen_font  )
        twofactor_input.place( anchor = "center", relx = 0.56, rely = 0.70 )
        twofactor_input.focus_set()
        
        twofactor_message = "(*) Insert two-factor authentication code received by message/app."
        twofactor_star = tk.Label( frame, text = twofactor_message, font = chosen_font )
        twofactor_star.place( anchor = "s", relx = 0.5, rely = 0.95 )
        
        def two_factor_login( event = 0 ):
            """
            Small function to deal with two-factor login.

            Args:
                event (int, optional): variable used to enable the button. Defaults to 0.
            """
            
            global exception_twof_label
            twofactor_code = twofactor_input.get()
            
            try:
                exception_twof_label.destroy()
            except BaseException:
                pass
            
            if twofactor_input.get() != "":
                try:
                    loader.two_factor_login( twofactor_code )
                    if checkbutton_var.get() == 1:
                        loader.save_session_to_file( "{}/.session_cookies".format( username ) )
                    frame.place_forget()
                except BaseException as e:
                    exception_twof_label = tk.Label( frame, text = e, font = chosen_font )
                    exception_twof_label.place( anchor = "center", relx = 0.5, rely = 0.80 )
                    exception_twof_label.config( fg = "red" )
                    
            spinner_gif.place_forget()
                    
        def TwoFactorLogin( event = 0 ):
            spinner_gif.place_forget()
            spinner_gif.place( anchor = "center", relx = 0.70, rely = 0.75 )
            threading.Thread( target = two_factor_login ).start()
        
        twofactor_input.bind( "<Return>", TwoFactorLogin )
        twofactor_input.bind( "<Escape>", restart_program )
        password_input.bind( "<Down>", lambda event: twofactor_input.focus_set() )
        twofactor_input.bind( "<Up>", lambda event: password_input.focus_set() )
        twofactor_login = tk.Button( frame, text = "Authenticate with two-factor code", font = chosen_font, command = TwoFactorLogin )
        twofactor_login.place( anchor = "center", relx = 0.5, rely = 0.75 )
        twofactor_login.config( cursor = "hand2", width = 29, bg = "black", fg = "white" )
        
    except BaseException as e:
        exception_label = tk.Label( frame, text = e, font = chosen_font )
        exception_label.place( anchor = "center", relx = 0.5, rely = 0.65 )
        exception_label.config( fg = "red" )
        
    spinner_gif.place_forget()

#############################################################
#    LoginFrame
#############################################################
def LoginFrame( login_frame ):
    """
    Main function used to set the login_frame settings.

    Args:
        login_frame (tkinter.Frame): the corresponding tkinter frame.
    """
    
    # Variables
    global eye_img
    global refresh_img
    global password_input
    global spinner_gif
    
    # Frame settings
    login_frame.place( anchor = "center", relx = 0.5, rely = 0.5 )
    login_frame.config( highlightbackground = "black", highlightthickness = 4 )
    
    # Progress spinner settings
    spinner_gif = gu.ImageLabel( login_frame )
    spinner_gif.load( "../img/icons/spinner.gif", width = 40, height = 40 )
    
    # Log in label
    chosen_font = ( "Helvetica", 15 )
    login_label = tk.Label( login_frame, text = "Log in", font = ( "Helvetica", 25 ) )
    login_label.place( anchor = "center", relx = 0.5, rely = 0.37 )
    
    # Username label and input
    username_label = tk.Label( login_frame, text = "Username:", font = chosen_font )
    username_label.place( anchor = "center", relx = 0.37, rely = 0.45 )
    username_input = tk.Entry( login_frame, font = chosen_font )
    username_input.place( anchor = "center", relx = 0.56, rely = 0.45 )
    username_input.focus_set()
    
    # Password label and input (with toggle)
    password_label = tk.Label( login_frame, text = "Password:", font = chosen_font )
    password_label.place( anchor = "center", relx = 0.37, rely = 0.5 )
    password_input = tk.Entry( login_frame, font = chosen_font  )
    password_input.place( anchor = "center", relx = 0.56, rely = 0.5 )
    password_input.config( show = "*" )
    eye_img = ImageTk.PhotoImage( Image.open( "../img/icons/eye.png" ).resize( ( 30, 30 ) ) )
    toggle_button = tk.Button( login_frame, image = eye_img )
    toggle_password = lambda event = 0: TogglePassword( password_input, toggle_button )
    toggle_button.place( anchor = "center", relx = 0.67, rely = 0.5 )
    toggle_button.config( command = toggle_password, cursor = "hand2", highlightthickness = 0, bd = 0, bg = "white" )
    password_input.bind( "<Control-c>", toggle_password )
    
    # Login into account
    def login( event = 0 ):
        spinner_gif.place( anchor = "center", relx = 0.7, rely = 0.55 )
        threading.Thread( target = Login, args = ( login_frame, username_input, password_input, chosen_font ) ).start()
    
    switch_to_passwd = lambda event = 0: SwitchToPasswd( username_input, password_input )
    username_input.bind( "<Return>", switch_to_passwd )
    username_input.bind( "<Down>", lambda event: password_input.focus_set() )
    password_input.bind( "<Return>", login )
    password_input.bind( "<Up>", lambda event: username_input.focus_set() )
    login_button = tk.Button( login_frame, text = "Authenticate", font = chosen_font, command = login )
    login_button.place( anchor = "center", relx = 0.5, rely = 0.55 )
    login_button.config( cursor = "hand2", width = 30, padx = -10, bg = "black", fg = "white" )
    
    # Remember login button
    remember_login_label = tk.Label( login_frame, text = "Remember me", font = ( "Helvetica", 10 ) )
    remember_login_label.place( anchor = "center", relx = 0.51, rely = 0.6 )
    remember_login_label.config( highlightthickness = 0, bd = 0 )
    button_size = ( 20, 20 )
    global checkbutton_var
    checkbutton_var = tk.IntVar()
    checkbutton_img = ImageTk.PhotoImage( Image.open( "../img/icons/checkbutton.png" ).resize( button_size) )
    checkbutton_img_tick = ImageTk.PhotoImage( Image.open( "../img/icons/checkbutton_tick.png" ).resize( button_size ) )
    remember_login_checkbutton = tk.Checkbutton( login_frame, variable = checkbutton_var, onvalue = 1, offvalue = 0, command = None )
    remember_login_checkbutton.place( anchor = "center", relx = 0.45, rely = 0.598 )
    remember_login_checkbutton.config( indicatoron = False, image = checkbutton_img, selectimage = checkbutton_img_tick, cursor = "hand2", highlightthickness = 0, bd = 0, bg = "white" )
    remember_login_checkbutton.image = checkbutton_img
    remember_login_checkbutton.selectimage = checkbutton_img_tick
    
    # Refresh button
    refresh_img = ImageTk.PhotoImage( Image.open( "../img/icons/refresh.png" ).resize( ( 60, 60 ) ) )
    global restart_program
    restart_program = lambda event = 0: RestartProgram( login_frame )
    username_input.bind( "<Escape>", restart_program )
    password_input.bind( "<Escape>", restart_program )
    refresh_button = tk.Button( login_frame, image = refresh_img )
    refresh_button.place( anchor = "ne", relx = 1, rely = 0 )
    refresh_button.config( command = restart_program, cursor = "hand2", highlightthickness = 0, bd = 0 )
    gu.CreateToolTip( refresh_button, text = "Refresh" )