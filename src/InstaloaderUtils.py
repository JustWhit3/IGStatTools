#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 12:43:00 2022
Author: Gianluca Bianco
"""

#############################################################
#    Modules
#############################################################
import numpy as np
import instaloader as ig
import tkinter as tk

#############################################################
#    Global variables
#############################################################
profile_ID = None

#############################################################
#    GetFollowers
#############################################################
def GetFollowers( profile ):
    """
    Function used to compute an array of followers of a given profile.

    Args:
        profile (instaloader.Instaloader.Profile): the interested profile.

    Returns:
        numpy.array: returns an array of instaloader.Instaloader.profile.
    """
    
    # Variables
    followers = np.array( [] )
    
    # Getting the array of followers of a profile:
    for follower in profile.get_followers():
        followers = np.append( followers, follower )
        
    return followers

#############################################################
#    GetFollowees
#############################################################
def GetFollowees( profile ):
    """
    Function used to compute an array of followees of a given profile.

    Args:
        profile (instaloader.Instaloader.Profile): the interested profile.

    Returns:
        numpy.array: returns an array of instaloader.Instaloader.profile.
    """
    
    # Variables
    followees = np.array( [] )
    
    # Getting the array of followees of a profile:
    for following in profile.get_followees():
        followees = np.append( followees, following )
        
    return followees

#############################################################
#    GetUnmatches
#############################################################
def GetUnmatches( followers, followees ):
    """
    Function used to compute an array of accounts who don't follow back a given profile.

    Args:
        followers (numpy.array): the array of followers of a profile.
        following (numpy.array): the array of following of a profile.

    Returns:
        numpy.array: returns an array of instaloader.Instaloader.profile.
    """
    
    # Variables
    unmatches = np.array( [] )
    
    # Get people who don't follow you back
    for following in followees:
        if following not in followers:
            unmatches = np.append( unmatches, following )
            
    return unmatches

#############################################################
#    Login
#############################################################
def Login( frame, username_input, password_input, chosen_font ):
    """
    Function used to login into Instagram account.

    Args:
        frame (tkinter.Frame): the working frame.
        username_input (str): the username.
        password_input (str): the password.
        chosen_font (tuple): a tuple with font information.

    Returns:
        instaloader.Profile: the instagram profile object.
    """
    
    # Variables
    loader = ig.Instaloader()
    username = username_input.get()
    password = password_input.get()
    
    # Doing login
    try:
        loader.login( username, password ) 
    except ig.exceptions.TwoFactorAuthRequiredException as e:
        exception_label = tk.Label( frame, text = e, font = chosen_font )
        exception_label.place( anchor = "center", relx = 0.5, rely = 0.60 )
        exception_label.config( fg = "red" )
        
        twofactor_label = tk.Label( frame, text = "Two-factor(*):", font = chosen_font )
        twofactor_label.place( anchor = "center", relx = 0.37, rely = 0.65 )
        twofactor_input = tk.Entry( frame, font = chosen_font  )
        twofactor_input.place( anchor = "center", relx = 0.6, rely = 0.65 )
        twofactor_input.focus_set()
        
        twofactor_message = "(*) Insert two-factor authentication code received by message/app."
        twofactor_star = tk.Label( frame, text = twofactor_message, font = chosen_font )
        twofactor_star.place( anchor = "s", relx = 0.5, rely = 0.95 )
        
        def TwoFactorLogin( event = 0 ):
            """
            Function used to login using two-factor authentication factor.
            """
            
            twofactor_code = twofactor_input.get()
            if twofactor_input.get() != "":
                try:
                    loader.two_factor_login( twofactor_code )
                except BaseException as e:
                    exception_label = tk.Label( frame, text = e, font = chosen_font )
                    exception_label.place( anchor = "center", relx = 0.5, rely = 0.75 )
                    exception_label.config( fg = "red" )
        
        twofactor_input.bind( "<Return>", TwoFactorLogin )
        twofactor_login = tk.Button( frame, text = "Authenticate with two-factor code", font = chosen_font, command = TwoFactorLogin )
        twofactor_login.place( anchor = "center", relx = 0.5, rely = 0.7 )
        twofactor_login.config( cursor = "hand2" )
    except BaseException as e:
        exception_label = tk.Label( frame, text = e, font = chosen_font )
        exception_label.place( anchor = "center", relx = 0.5, rely = 0.6 )
        exception_label.config( fg = "red" )

    profile_ID = ig.Profile.from_username( loader.context, username )