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
#    GetPosts
#############################################################
def GetObjects( objects ):
    """
    Function used to compute an array of objects of a given profile.

    Args:
        objects (any): a generic object from the Profile class.

    Returns:
        numpy.array: returns an array of instaloader.Instaloader objects.
    """
    
    # Variables
    objects_array = np.array( [] )
    
    # Getting the array of followees of a profile:
    for object in objects:
        objects_array = np.append( objects_array, object )
        
    return objects_array

#############################################################
#    GetTotalLikes
#############################################################
def GetTotalLikesComments( profile ):
    """
    Method used to get total likes of a profile.

    Args:
        profile (instaloader.Instaloader.Profile): profile object.
        
    Returns:
        int: total number of profile likes.
        int: total number of profile comments.
    """
    
    # Variables
    total_likes = 0
    total_comments = 0
    
    # Getting total number of likes and comments
    for post in profile.get_posts():
        for like in post.get_likes():
            total_likes += 1
        for comment in post.get_comments():
            total_comments += 1
    
    return total_likes, total_comments

#############################################################
#    GetTotalPhotosVideos
#############################################################
def GetTotalPhotosVideos( profile ):
    """
    Method used to get total photos number of a profile.

    Args:
        profile (instaloader.Instaloader.Profile): profile object.
        
    Returns:
        int: total number of profile photos.
        int: total number of profile videos.
    """
    
    # Variables
    total_photos = 0
    total_videos = 0
    
    # Getting total number of photos and videos
    for post in profile.get_posts():
        if post.typename == "GraphImage":
            total_photos += 1
        elif post.typename == "GraphVideo":
            total_videos += 1
    
    return total_photos, total_videos