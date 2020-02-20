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
d = pd.read_csv('code\data.csv')
d = np.array(d)

# Variables 
dist = np.array([d[0:6,2]],dtype=float) # Distance Observations
ang = np.array(d[9:17,1:4],dtype=float)
ang = ang[:,0] + ang[:,1]/60 + ang[:,2]/3600 



## CONDITIONS ##

# Sum around polygon - should be 360
# 1 + 8 + 7 + 6 + 5 + 4 + 3 + (2-3)  
int_angle = ang[0] + ang[7] + ang[6] + ang[5] + ang[4] + ang[3] + ang[1] 


# Random Sympy thing 
x = Symbol('x')
A = diff(x**2)
B = A.subs(x,3)

# Sine Law 
something = m.sin(ang[7])/dist[0,2] - m.sin(ang[4])/dist[0,4]
print(something)



