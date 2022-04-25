#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 21:33:00 2022
Author: Gianluca Bianco
"""

#############################################################
#    Modules
#############################################################
import tkinter as tk
import instaloader as ig
import glob

#############################################################
#    MenuFrame
#############################################################
def MenuFrame( menu_frame ):
    
    # Loading instagram profile info
    loader = ig.Instaloader()
    for session_file in glob.glob( ".*session_cookies" ):
        username = session_file.split( "-" )[0][1:]
    loader.load_session_from_file( username, filename = ".session_cookies" )

    # Frame settings
    menu_frame.place( anchor = "center", relx = 0.5, rely = 0.5 )
    menu_frame.config( highlightbackground = "black", highlightthickness = 4 )
    
    
    
    label = tk.Label( menu_frame, text = "ciao" )
    label.place( anchor = "center", relx = 0.5, rely = 0.5 )