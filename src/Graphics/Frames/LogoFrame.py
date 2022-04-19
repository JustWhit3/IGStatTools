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

#############################################################
#    LogoFrame
#############################################################
def LogoFrame( logo_frame ):
    """
    Function used to set the logo frame.

    Args:
        logo_frame (tkinter.Frame): the logo frame object.
    """

    # Variables
    global logo_img

    # Settings
    logo_frame.place( anchor = "center", relx = 0.5, rely = 0.5 )
    logo_img = ImageTk.PhotoImage( Image.open( "../img/logo.png" ).resize( ( 1000, 700 ) ) )
    logo_label = tk.Label( logo_frame, image = logo_img )
    logo_label.place( anchor = "center",relx = 0.50, rely = 0.50 )