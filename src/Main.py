#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 16 12:44:00 2022
Author: Gianluca Bianco
"""

#############################################################
#    Modules
#############################################################

# Standard modules
import tkinter as tk

# Utils modules
from Utils import InstaloaderUtils as iu

# Load Windows
from Graphics.Windows.RootWindow import RootWindow

# Load frames
from Graphics.Frames.LoginFrame import LoginFrame
from Graphics.Frames.LogoFrame import LogoFrame

#############################################################
#    Main function
#############################################################
def main():
    
    # Main window settings
    root = tk.Tk()
    RootWindow( root )
    
    # Logo frame settings
    logo_frame = tk.Frame( root, width = 1800, height = 1500 )
    LogoFrame( logo_frame )
    
    # Login frame settings
    login_frame = tk.Frame( root, width = 1800, height = 1500 )
    LoginFrame( login_frame )
    time_passed = 0000
    root.after( time_passed, logo_frame.destroy )
    login_frame_pos = lambda: login_frame.place( anchor = "center", relx = 0.5, rely = 0.5 )
    root.after( time_passed, login_frame_pos )
    profile = iu.profile_ID
    
    # Displaying graphics
    root.mainloop()

if __name__ == "__main__":
    main()