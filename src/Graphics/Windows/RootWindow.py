#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 15:06:00 2022
Author: Gianluca Bianco
"""

#############################################################
#    RootWindow
#############################################################
def RootWindow( root ):
    """
    Function used to set the main root window settings.

    Args:
        root (tkinter.Window): the main root window.
    """

    root.geometry( "1800x1500" )
    root.title( "IGStatTools" )