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