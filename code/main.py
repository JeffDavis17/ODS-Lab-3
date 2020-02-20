import numpy as np 
from sympy import *
import pandas as pd
import math as m


# Lab assignment number 3: Conditions in Triangulateration
# In this lab there are 5 unknowns, 14 observations, 1 known baseline. That means there are 14+1-5 = 10 redundant observations?
# unknowns: Dqs, Dqt, Dqr, AZqt, AZqs

# Possible Geometric Conditions include: Sine Law, Cosine Law, sum of angles in polygon, Horizon  
# We either need 9 or 10 independant conditions


# We can determine the rank of the B matrix and this should equal the number of redundant observations either 9 or 10?? probably 10

# Data
d = pd.read_csv(r'C:/Users/Family/Documents/GitHub/ODS-Lab-3/code/data.csv')
d = np.array(d)

# Variables 
dist = np.array([d[0:6,2]],dtype=float) # Distance Observations
ang = np.array(d[9:17,1:4],dtype=float)
ang = ang[:,0] + ang[:,1]/60 + ang[:,2]/3600 

# Sympy Variables
a1 = Symbol('a1')
a2 = Symbol('a2')
a3 = Symbol('a3')
a4 = Symbol('a4')
a5 = Symbol('a5')
a6 = Symbol('a6')
a7 = Symbol('a7')
a8 = Symbol('a8')
Dqr = Symbol('Dqr')
Drs = Symbol('Drs')
Dst = Symbol('Dst')
Dtq = Symbol('Dtq')
Dqs = Symbol('Dqs')
Drt = Symbol('Drt')
var = np.array([a1,a2,a3,a4,a5,a6,a7,a8,Dqr,Drs,Dst,Dtq,Dqs,Drt])


## CONDITIONS and Derivatives for 2nd Design Matrix
# Second Design matrix should be number conditions by number observations? Maybe 10 by 14
b = np.zeros([10,14])


# Sum around the polygon
ang_Sum = sum(var[0:8]) # Sum angles
ang_diff = np.array(np.zeros(14)) # Initialize 
ang_diff[:] = diff(ang_Sum,var[:]) # Take Derivative

ang_sum_w = sum(ang) - ang[2] # Misclosure of Internal Angles


# Sine Law 
sin_421 = sin(a7)/Dst - sin(a4)/Dqs
sin_421_diff = []
sin_421_diff[:] = np.array(diff(sin_421,var[:])) # Take Derivative

sin_421_w = m.sin(ang[7])/dist[0,2] - m.sin(ang[4])/dist[0,4] # Misclosure of sine law 




# Some other relationship that d1*d2=1????
something2 = (dist[0,1]/dist[0,0])*(dist[0,0]/dist[0,4])*(dist[0,4]/dist[0,1]) - 1


dist_rela = (Drs/Dqr)*(Dqr/Dqs)*(Dqs/Drs)
dist_rela_diff = []
dist_rela_diff[:] = np.array(diff(dist_rela,var[:]))
print(dist_rela_diff)