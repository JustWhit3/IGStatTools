#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 9 16:43:00 2022
Author: Gianluca Bianco
"""

#############################################################
#    Modules
#############################################################

# Standard libraries
import instaloader as ig
import numpy as np
from pwinput import pwinput
from termcolor import colored as cl
import sys

# Utils
import InstaloaderUtils as iu

#############################################################
#    Main function
#############################################################
def main():
    
    # Basic setup
    loader = ig.Instaloader()
    
    # Login into account
    print( "Press Ctrl+C to close the program.", end = "\n\n" )
    while True:
        try:
            username = input( "Username: " )
            password = pwinput()
            loader.login( username, password )
        except ig.exceptions.TwoFactorAuthRequiredException:
            two_factor_code = int( input( "Two-factor authentication code is required: " ) )
            loader.two_factor_login( two_factor_code )
        except BaseException as e:
            print()
            print( cl( e, "red" ), end = "\n\n" )
    
        # Getting metadata
        profile = ig.Profile.from_username( loader.context, username )
        followers = iu.GetFollowers( profile )
        followees = iu.GetFollowees( profile )

        # Getting the name of the accounts which don't follow you back:
        print()
        print( "This is the list of the accounts who don't follow \"{}\" back:".format( username ), end = "\n" )
        unmatches = iu.GetUnmatches( followers, followees )
        for index, account in np.ndenumerate( unmatches ):
            print( "{}) {}".format( index[0] + 1, account.username ) )
        
        sys.exit()

if __name__ == "__main__":
    main()