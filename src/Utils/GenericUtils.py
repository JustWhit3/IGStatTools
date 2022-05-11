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
def StringToPicNum( pic_string_name ):
    """
    Function used to convert a pic name into a number.

    Args:
        pic_string_name (str): picture name.

    Returns:
        int: the converted number.
        
    Testing:
        >>> StringToPicNum( "2019-04-12_09-10-13_UTC_profile_pic" )
        20190412091013
    """
    
    pic_num = pic_string_name.split( "_" )[0] + pic_string_name.split( "_" )[1]
    pic_num = int( pic_num.replace( "-", "" ) )
    
    return pic_num

#############################################################
#    Main program
#############################################################
if __name__ == "__main__":
    doctest.testmod()