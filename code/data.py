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
d = pd.read_csv(r'C:/Users/jcdav/Documents/GitHub/ODS-Lab-3/code/data.csv')
d = np.array(d)

# Variables 
dist = np.array([d[0:6,2]],dtype=float) # Distance Observations
ang = np.array(d[9:17,1:4],dtype=float)
ang = ang[:,0] + ang[:,1]/60 + ang[:,2]/3600 
ang = np.radians(ang)

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
var = np.array([Dqr,Drs,Dst,Dtq,Dqs,Drt,a1,a2,a3,a4,a5,a6,a7,a8,])
variables = [(Dqr,dist[0,0]),(Drs,dist[0,1]),(Dst,dist[0,2]),(Dtq,dist[0,3]),(Dqs,dist[0,4]),(Drt,dist[0,5]),(a1,ang[0]),(a2,ang[1]),(a3,ang[2]),(a4,ang[3]),(a5,ang[4]),(a6,ang[5]),(a7,ang[6]),(a8,ang[7])]

dist_er = np.array([0.8,0.7,0.8,0.8,0.9,0.9])
ang_er = np.zeros(8)
ang_er[:] = 4*3600
error = np.zeros(14)
error[0:6] = dist_er
error[6:14] = ang_er





