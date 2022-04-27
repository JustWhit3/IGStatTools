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

# Utils Libraries
from Utils import GraphicsUtils as gu

#############################################################
#    LogoFrame
#############################################################
class LogoFrame( tk.Frame ):
    """
    Logo frame class.

    Args:
        tk (tkinter.Frame): inherit from tkinter.Frame class.
    """
    
    def __init__( self, window ):
        """
        Main constructor of the class.

        Args:
            window (tkinter.Tk): the window hosting the frame.
        """
        
        super().__init__( window )
        self[ "width" ] = 1800
        self[ "height" ] = 1500
        self.config( highlightbackground = "black", highlightthickness = 4 )
        self.__create_widgets()
        self.place( anchor = "center", relx = 0.5, rely = 0.5 )
        self.after( 1000, self.destroy ) 

    #############################################################
    #    __create_widgets
    #############################################################
    def __create_widgets( self ):
        """
        Method used to create main widgets of the frame.
        """
        
        # Logo image
        self.logo_img = ImageTk.PhotoImage( Image.open( "../img/images/logo.png" ).resize( ( 1000, 700 ) ) )
        self.logo_label = tk.Label( self, image = self.logo_img )
        self.logo_label.place( anchor = "center",relx = 0.50, rely = 0.50 )

        # Progress spinner
        self.spinner_gif = gu.ImageLabel( self )
        self.spinner_gif.load( "../img/icons/spinner.gif", width = 100, height = 100 )
        self.spinner_gif.place( anchor = "center", relx = 0.5, rely = 0.80 )
    
    