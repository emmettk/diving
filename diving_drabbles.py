# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 17:36:50 2018

@author: ekrupczak

Diving Drabbles

"""

def ACR(start, end, time, depth):
    '''
    Air Consumption Rate
    start, end in psi
    time in minutes
    depth in fsw
    returns ACR in psi per minute
    '''
    return ((start-end)/time)/((depth+33)/33)
 

def DCR(SAC, depth):
    '''
    Depth Consumption Rate
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

def SAC(time, start,end, depth, volume, working_pressure):
    '''
    Surface Air Consumption
    start, end in psi
    time in minutes
    depth in fsw
    volume of tank in psi
    working pressure of tank in psi
    returns SAC in ft^3 per minute
    '''
    return ((start-end)/working_pressure)*volume/(time*((depth+33)/33))

def SAC_worksheet_version(time, psi_used, avg_depth, cylinder_volume, working_pressure):
    '''
    Surface Air Consumption rate from WHOI dive worksheet
    time - dive time in minutes
    psi_used - air consumed during the dive in psi
    avg_depth - average depth of the dive in feet
    cylinder_volume in cubic feet
    working_pressure of cylinder in psi
    '''
    print("In ", time, " minutes I used ", psi_used, " psi from my cylinder at depth.")
    B = psi_used/time
    print("Therefore in one minute I used ", B, " psi from my cylinder at depth.")
    print("The average depth of my dive was ", avg_depth, " feet.")
    D = avg_depth/33 +1
    print("The pressure during the dive was ", round(D,2), "ATA.")
    E = B/D
    print("The amount of air I used in my cylinders in one minute at the surface is ", round(E,2), " psi.")
    print("My cylinder is ", cylinder_volume, " cubic feet at ", working_pressure, " psi working pressure.")
    G = working_pressure/cylinder_volume
    print("Every time I breathe ", G, " psi, I will use one cubic foot from my tanks.")
    H = E/G
    print("Since I used ", round(E,2), " psi per minute at the surface, my SAC rate is ", round(H,2), " cubic ft/minute.")
    return H
