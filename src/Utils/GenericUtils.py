#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 29 21:28:00 2022
Author: Gianluca Bianco
"""

#############################################################
#    Modules
#############################################################
import doctest

#############################################################
#    StringToPicNum
#############################################################
def Score( followers_count, followees_count ):
    """
    Function used to compute personal score for instagram profile.

    Args:
        followers_count (int): number of followers of a profile.
        followees_count (_type_): number of followees of a profile.

    Returns:
        str: score of the profile.
        
    Testing:
        >>> Score( 300, 300 )
        'C'
        >>> Score( 200, 400 )
        'E'
        >>> Score( 200, 600 )
        'F'
        >>> Score( 1900, 560 )
        'S'
    """
    
    # Variables
    score = round( followers_count / followees_count * 10, 2 )
    
    # Computing the score
    if score in range( 9, 11 ): return "C"
    elif score in range( 7, 9 ): return "D"
    elif score in range( 5, 7 ): return "E"
    elif score < 5: return "F"
    elif score in range( 11, 13 ): return "B"
    elif score in range( 13, 15 ): return "A"
    elif score > 15: return "S"

#############################################################
#    Main program
#############################################################
if __name__ == "__main__":
    doctest.testmod()