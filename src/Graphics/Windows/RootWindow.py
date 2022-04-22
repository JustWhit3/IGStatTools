#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 15:06:00 2022
Author: Gianluca Bianco
"""

#############################################################
#    Modules
#############################################################
import os, sys

#############################################################
#    RootWindow
#############################################################
def RootWindow( root ):
    """
    Function used to set the main root window settings.

    Args:
        root (tkinter.Window): the main root window.
    """
    
    # Variables
    window_width = 1800
    window_height = 1500
    
    # Set basic values
    root.title( "IGStatTools" )
    
    # Set the icon
    path_to_icon = os.getcwd() + "/../img/icons/logo_small_icon_only_inverted"
    if "nt" == os.name:
        root.iconbitmap( path_to_icon + ".ico")
    else:
        root.iconbitmap( "@" + path_to_icon + ".xbm" )
    
    # Centering the window
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    center_x = int( screen_width / 2 - window_width / 2 )
    center_y = int( screen_height / 2 - window_height / 2 )
    root.geometry( f"{window_width}x{window_height}+{center_x}+{center_y}" )
    
    # Enabling some commands
    root.bind( "<Control-z>", sys.exit )