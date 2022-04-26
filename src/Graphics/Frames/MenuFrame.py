#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 21:33:00 2022
Author: Gianluca Bianco
"""

#############################################################
#    Modules
#############################################################

# Standard libraries
import tkinter as tk
import instaloader as ig
import glob
import threading
from PIL import ImageTk, Image
import os

#############################################################
#    Loading
#############################################################
def Loading( menu_frame ):
    
    # Variables
    username = ""
    loader = ig.Instaloader()
    global profile
    
    # Loading instagram profile info
    for session_file in glob.glob( "*/.session_cookies" ):
        username = session_file.split( "/" )[0]
        loader.load_session_from_file( username, filename = session_file )
    profile = ig.Profile.from_username( loader.context, username )
    
    # Placing basic profile info on the screen   
    loader.download_profilepic( profile )            
    for profile_pic in glob.glob( "*/*profile_pic.jpg" ):
        profile_img = ImageTk.PhotoImage( Image.open( profile_pic ) )
            
    profile_img_label = tk.Label( menu_frame, image = profile_img )
    profile_img_label.image = profile_img
    profile_img_label.place( anchor = "center", relx = 0.5, rely = 0.5 )

#############################################################
#    MenuFrame
#############################################################
def MenuFrame( menu_frame ):
    
    # Variables
    chosen_font = ( "Helvetica", 15 )
    
    # Frame settings
    menu_frame.place( anchor = "center", relx = 0.5, rely = 0.5 )
    menu_frame.config( highlightbackground = "black", highlightthickness = 4 )
    
    # Loading main profile information on the frame
    threading.Thread( target = Loading, args = ( menu_frame, ) ).start()