# -*- coding: utf-8 -*-
"""
Created on Fri Jun 16 17:13:42 2017

@author: ekrupczak

Decompression schedules for various gas mixes
"""

import pandas as pd
import numpy as np
import datetime as dt
import math

## Import Buhlmann's tables for nitrogen and helium halftime, a and b values
inert_gas_table = pd.read_table("./buhlmann_table.txt")
water_vapor_pressure = 0.0627 #atm

def Schreiner(Po, descent_rate, fgas, start_depth, end_depth, half_time):
    """
    half-time in minutes from the inert gas table
    descent rate in atm per minute
    """
    Pabs = start_depth/33+1 ##atm pressure in sea water at start depth
    Palv = fgas*Pabs*(1 - water_vapor_pressure) ## alveolar pressure (pressure of inspired inert gas)
    k = math.log(2)/half_time
    ##rate of change of inert gas pressure
    R = descent_rate/33*fgas
    t = (end_depth-start_depth)/descent_rate
#    print(Pabs, Palv, k, R, t)
    return Palv + R*(t-1/k) - (Palv-Po-(R/k))*math.e**(-k*t)

def Schreiner_stationary(Po, t, fgas, depth, half_time):
    """
    Schreiner equation with R = 0 and t = bottom time
    """
    Pabs = depth/33+1 ##atm pressure in sea water at start depth
    Palv = fgas*Pabs*(1 - water_vapor_pressure) ## alveolar pressure (pressure of inspired inert gas)
    k = math.log(2)/half_time
#    print(Pabs, Palv, k, R, t)
    return Palv - (Palv-Po)*math.e**(-k*t)

def Instantaneous(Po, t, fgas, depth, half_time):
    """
    Rephrased version of the stationary Schreiner equation, called the "Instantaneous Equation"
    """
    Pabs = depth/33+1 ##atm pressure in sea water at start depth
    Palv = fgas*Pabs*(1 - water_vapor_pressure) ## alveolar pressure (pressure of inspired inert gas)   
    return Po + (Palv - Po)*(1-2**(-t/half_time))



if __name__ == "__main__":
    fN2 = 0.68 ##initial nitrogen pressure at the surface
    ##Initial pressure after breathing air
    Po = 0.79 *(1-water_vapor_pressure) 
    descent_rate = 20*3.3 #ft per minute
    start_depth = 0
    end_depth = 30*3.3 #down to 4 ata 
#    compartment = 1
    P = pd.DataFrame(index = range(16), columns = ["Compartment", "P"])
    for i in P.index:
        compartment = i+1
        half_time = inert_gas_table.loc[inert_gas_table["Compartment"] == compartment]["N2-Half-time"].values[0]
        P.loc[i] = [compartment, Schreiner(Po, descent_rate, fN2, start_depth, end_depth, half_time)]
        
    ## Assume no bottom time; bounce to 33 ft and back
#    descent_rate = -descent_rate
    start_depth = end_depth
    end_depth = 0
    for i in P.index:
        compartment = i+1
        half_time = inert_gas_table.loc[inert_gas_table["Compartment"] == compartment]["N2-Half-time"].values[0]
        P.loc[i, "P2"] = Schreiner(P.loc[i, "P"], descent_rate, fN2, start_depth, end_depth, half_time)
        P.loc[i, "Schreiner Stationary"]  = Schreiner_stationary(P.loc[i, "P"], 10, fN2, 33, half_time)
        P.loc[i, "Instantaneous"]= Instantaneous(P.loc[i, "P"], 10, fN2, 33, half_time)
    
    
    #### Example from the internet using a more conservative half-life table
#    fN2 = 0.68 ##initial nitrogen pressure at the surface
#    ##Initial pressure after breathing air
#    Po = 0.79 *(1-water_vapor_pressure) 
#    descent_rate = 20*3.3 #ft per minute
#    start_depth = 0
#    end_depth = 30*3.3 #down to 4 ata    
#    print(Schreiner(Po, descent_rate, fN2, start_depth, end_depth, 5))