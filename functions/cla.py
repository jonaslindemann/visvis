# -*- coding: utf-8 -*-
# Copyright (c) 2010, Almar Klein
#
# Visvis is distributed under the terms of the (new) BSD License.
# The full license can be found in 'license.txt'.

import visvis as vv

def cla():
    """ cla()
    
    Clear the current axes. 
    
    """
    a = vv.gca()
    a.Clear()
    return a

