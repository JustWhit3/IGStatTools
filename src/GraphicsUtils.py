#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 23:33:00 2022
Author: Gianluca Bianco
"""

#############################################################
#    Modules
#############################################################
from PIL import ImageTk, Image

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
    
    eye = ImageTk.PhotoImage( Image.open( "../img/eye.png" ).resize( ( 30, 30 ) ) )
    hide = ImageTk.PhotoImage( Image.open( "../img/hide.png" ).resize( ( 30, 30 ) ) )
    
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