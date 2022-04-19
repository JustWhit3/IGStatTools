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
from PIL import ImageTk, Image
import instaloader as ig

# Utils modules
import InstaloaderUtils as iu
import GraphicsUtils as gu

#############################################################
#    Main function
#############################################################
def main():
    
    # Main window settings
    root = tk.Tk()
    root.geometry( "1800x1500" )
    root.title( "IGStatTools" )
    
    # Logo frame
    logo_frame = tk.Frame( root, width = 1700, height = 1600 )
    logo_frame.place( anchor = "center", relx = 0.5, rely = 0.5 )
    
    logo_img = ImageTk.PhotoImage( Image.open( "../img/logo.png" ).resize( ( 1000, 700 ) ) )
    logo_label = tk.Label( logo_frame, image = logo_img )
    logo_label.place( anchor = "center",relx = 0.50, rely = 0.50 )
    
    # Login frame
    login_frame = tk.Frame( root, width = 1700, height = 1600 )
    root.after( 0000, login_frame.pack )
    chosen_font = ( "Helvetica", 15 )
    
    login_label = tk.Label( login_frame, text = "Insert Instagram credentials", font = chosen_font )
    login_label.place( anchor = "center", relx = 0.50, rely = 0.40 )
    
    username_label = tk.Label( login_frame, text = "Username:", font = chosen_font )
    username_label.place( anchor = "center", relx = 0.37, rely = 0.45 )
    username_input = tk.Entry( login_frame, font = chosen_font )
    username_input.place( anchor = "center", relx = 0.6, rely = 0.45 )
    username_input.focus_set()
    
    password_label = tk.Label( login_frame, text = "Password:", font = chosen_font )
    password_label.place( anchor = "center", relx = 0.37, rely = 0.5 )
    password_input = tk.Entry( login_frame, font = chosen_font  )
    password_input.place( anchor = "center", relx = 0.6, rely = 0.5 )
    password_input.config( show = "*" )
    
    eye_img = ImageTk.PhotoImage( Image.open( "../img/eye.png" ).resize( ( 30, 30 ) ) )
    toggle_button = tk.Button( login_frame, image = eye_img )
    toggle_password = lambda: gu.TogglePassword( password_input, toggle_button )
    toggle_button.place( anchor = "center", relx = 0.715, rely = 0.5 )
    toggle_button.config( command = toggle_password, cursor = "hand2", highlightthickness = 0, bd = 0, bg = "white" )
    
    # Login into account
    login = lambda event = 0: iu.Login( login_frame, username_input, password_input, chosen_font )
    SwitchToPasswd = lambda event = 0: gu.SwitchToPasswd( username_input, password_input )
    username_input.bind( "<Return>", SwitchToPasswd )
    password_input.bind( "<Return>", login )
    login_button = tk.Button( login_frame, text = "Log in", font = chosen_font, command = login )
    login_button.place( anchor = "center", relx = 0.5, rely = 0.55 )
    login_button.config( cursor = "hand2" )
    profile = iu.profile_ID
    
    # Displaying graphics
    root.mainloop()

if __name__ == "__main__":
    main()