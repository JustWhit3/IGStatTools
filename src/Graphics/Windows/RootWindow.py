#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 15:06:00 2022
Author: Gianluca Bianco
"""

#############################################################
#    Modules
#############################################################

# Standard libraries
import tkinter as tk
import os, sys
import glob

# Load frames
from Graphics.Frames.LogoFrame import LogoFrame
from Graphics.Frames.LoginFrame import LoginFrame
from Graphics.Frames.MenuFrame import MenuFrame

#############################################################
#    RootWindow
#############################################################
class RootWindow( tk.Tk ):
    """
    Main window of the app.

    Args:
        tk (tkinter): main tkinter class.
    """
    
    def __init__( self ):
        """
        Main constructor of the class
        """
        
        super().__init__()
        
        # Variables
        window_width = 1800
        window_height = 1500
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        center_x = int( screen_width / 2 - window_width / 2 )
        center_y = int( screen_height / 2 - window_height / 2 )
        
        # Basic settings
        self.title( "IGStatTools" )
        self.geometry( f"{window_width}x{window_height}+{center_x}+{center_y}" )
        
        # Icon settings
        path_to_icon = os.getcwd() + "/../img/icons/logo_small_icon_only_inverted"
        if "nt" == os.name:
            self.iconbitmap( path_to_icon + ".ico")
        else:
            self.iconbitmap( "@" + path_to_icon + ".xbm" )

        # Other commands
        self.bind( "<Control-z>", sys.exit )
        self.__create_widgets()
        
    #############################################################
    #    __create_widgets
    #############################################################
    def __create_widgets( self ):
        """
        Method used to create frames.
        """
    
        self.menu_frame = MenuFrame( self )
        self.login_frame = LoginFrame( self, self.menu_frame )
        self.logo_frame = LogoFrame( self )