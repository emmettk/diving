# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 17:36:50 2018

@author: ekrupczak

Diving Drabbles

"""

def ACR(start, end, time, depth):
    '''
    start, end in psi
    time in minutes
    depth in fsw
    returns ACR in psi per minute
    '''
    return ((start-end)/time)/((depth+33)/33)
 

def DCR(SAC, depth):
    '''
    SAC in pounds per minute
    depth in fsw
    returns DCR in pounds per minute
    '''
    return SAC*((depth+33)/33)

def time_at_depth(SAC, air, depth):
    '''
    SAC in pounds per minute
    air in psi
    depth in fsw
    returns time to consume that quantity of air at given depth in minutes
    '''
    return air/DCR(SAC,depth)

def SAC(start,end, time, depth, working_pressure, volume):
    '''
    start, end in psi
    time in minutes
    depth in fsw
    volume of tank in psi
    working pressure of tank in psi
    returns SAC in ft^3 per minute
    '''
    return ((start-end)/working_pressure)*volume/(time*((depth+33)/33))