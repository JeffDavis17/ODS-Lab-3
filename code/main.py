import numpy as np 
import sympy as sym
import pandas as pd



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
direction = np.array(d[9:17,1:4],dtype=float)
direction = direction[:,0] + direction[:,1]/60 + direction[:,2]/3600 



## CONDITIONS ##

# Sum around polygon - should be 360
# 1 + 8 + 7 + 6 + 5 + 4 + 3 + (2-3)  
int_angle = direction[0] + direction[7] + direction[6] + direction[5] + direction[4] + direction[3] + direction[1] 


# Random Sympy thing 
x = sym.Symbol('x')
A = sym.diff(x**5)

print(A)