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
import os
import glob

# Utils modules
from Utils import InstaloaderUtils as iu

# Load Windows
from Graphics.Windows.RootWindow import RootWindow

# Load frames
from Graphics.Frames.LoginFrame import LoginFrame
from Graphics.Frames.LogoFrame import LogoFrame
from Graphics.Frames.MenuFrame import MenuFrame

#############################################################
#    Main function
#############################################################
def main():
    
    # Main window settings
    root = tk.Tk()
    RootWindow( root )
    
    # Frame creations for hierarchy
    menu_frame = tk.Frame( root, width = 1800, height = 1500 )
    login_frame = tk.Frame( root, width = 1800, height = 1500 )
    logo_frame = tk.Frame( root, width = 1800, height = 1500 )
    
    # Logo frame settings
    LogoFrame( logo_frame )
    
    # Login frame settings
    LoginFrame( login_frame )
    login_time_passed = 0000
    root.after( login_time_passed, logo_frame.destroy )
    
    for session_file in glob.glob( ".*session_cookies" ):
        if os.path.exists( session_file ):
            login_frame.place_forget()
    
    # Menu frame settings
    MenuFrame( menu_frame )
    
    # Displaying graphics
    root.mainloop()

if __name__ == "__main__":
    main()