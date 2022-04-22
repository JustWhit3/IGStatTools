#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 09:40:00 2022
Author: Gianluca Bianco
"""

#############################################################
#    Modules
#############################################################
import tkinter as tk
from PIL import ImageTk, Image
from itertools import count

#############################################################
#    ToolTip
#############################################################
class ToolTip( object ):
    """
    A class used to create a tooltip object to be used with other widgets.

    Parents:
        object: a general Tkinter object.
    """

    def __init__( self, widget ):
        """
        Main class constructor.

        Args:
            widget (Tkinter): a generic Tkinter widget.
        """
        
        self.widget = widget
        self.tipwindow = None
        self.id = None
        self.x = self.y = 0

    def showtip( self, text ):
        """
        Display text in tooltip window.

        Args:
            text (str): the text to be displayed in the tooltip.
        """

        self.text = text
        if self.tipwindow or not self.text:
            return
        x, y, cx, cy = self.widget.bbox( "insert" )
        x = x + self.widget.winfo_rootx() - 57
        y = y + cy + self.widget.winfo_rooty() + 57
        self.tipwindow = tw = tk.Toplevel( self.widget )
        tw.wm_overrideredirect(1)
        tw.wm_geometry( "+%d+%d" % ( x, y ) )
        label = tk.Label( tw, text = self.text, justify = tk.LEFT, background = "#ffffe0", relief = tk.SOLID, borderwidth = 1,
                          font = ( "tahoma", "8", "normal" ) )
        label.pack( ipadx = 1 )

    def hidetip( self ):
        """
        Function used to hide the tooltip.
        """
        
        tw = self.tipwindow
        self.tipwindow = None
        if tw:
            tw.destroy()

#############################################################
#    CreateToolTip
#############################################################
def CreateToolTip(widget, text):
    """
    Function used to create a tooltip among a certain widget.

    Args:
        widget (Tkinter): a Tkinter widget.
        text (str): the text to be displayed in the tooltip.
    """
    
    toolTip = ToolTip( widget )
    def enter( event ):
        toolTip.showtip( text )
    def leave( event ):
        toolTip.hidetip()
    widget.bind( "<Enter>", enter )
    widget.bind( "<Leave>", leave )
    
#############################################################
#    ImageLabel
#############################################################
class ImageLabel( tk.Label ):
    """
    A class that displays images, and plays them if they are gifs.

    Parent:
        tk.Label: a tkinter Label class.
    """
    
    def load( self, im, width = 100, height = 100 ):
        """
        Method used to load the image.

        Args:
            im (_type_): _description_
        """
        
        if isinstance( im, str ):
            im = Image.open( im )
        self.loc = 0
        self.frames = []

        try:
            for i in count(1):
                self.frames.append( ImageTk.PhotoImage( im.resize( ( width, height ) ).copy() ) )
                im.seek( i )
        except EOFError:
            pass

        try:
            self.delay = im.info[ "duration" ]
        except:
            self.delay = 100

        if len( self.frames ) == 1:
            self.config( image = self.frames[0] )
        else:
            self.next_frame()

    def unload( self ):
        """
        Method used to unload the image.
        """
        
        self.config( image = "" )
        self.frames = None

    def next_frame( self ):
        """
        Method used to display the next frame of the image.
        """
        
        if self.frames:
            self.loc += 1
            self.loc %= len( self.frames )
            if self.loc > 0:
                self.config( image = self.frames[ self.loc ] )
            self.after( self.delay, self.next_frame )
            