# -*- coding: utf-8 -*-
"""
Created on Fri Jun 16 16:15:44 2017

@author: ekrupczak

A little code drabble to calculate what the partial pressure is of various gasses at depth
"""

fsw = 33 ## feet sea water per atm 
psiperfsw = 0.445 ## atm per feet fresh water
psiperffw = 0.432 ## atm per feet sea water

def partial_pressure(depth, percent):
    """
    Assuming 1 atm at surface and salt water (33 fsw/atm), returns partial pressure of gas at depth
    percent: percent of the mixture comprised of the chosen gas (i.e. partial pressure in atm of gas at surface)
    """
    return round(((depth/fsw)+1)*percent,2)

def mixture_composition(depth, maxatm=1.4):
    """
    Gives the percent of chosen gas a mixture must have at the surface to have maxatm partial pressure of chosen gas at depth
    """
    return round(maxatm/((depth/fsw)+1)*100, 2)
    


if __name__ == "__main__":
    depth = 100 ## depth in feet
    
    print("Partial pressure of O2 in air:",partial_pressure(depth, 0.21), "atm")
    print("Partial pressure of N2 in air:", partial_pressure(depth, 0.79), "atm")
    print("Partial pressure of O2 in 32% O2 nitrox:", partial_pressure(depth, 0.32), "atm")
    print("Partial pressure of N2 in 32% O2 nitrox:", partial_pressure(depth, 1-0.32), "atm")
    
    
    print("Max O2 percent of gas to be breathed at", depth, "fsw:", mixture_composition(depth, 1.4),"%")
    print("Max N2 percent of gas to be breathed at", depth, "fsw:", mixture_composition(depth, 3.2), "%")
    print("Min O2 percent of gas to be breathed at", depth, "fsw:", mixture_composition(depth, 0.2), "%")
    