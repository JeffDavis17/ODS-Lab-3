import numpy as np 
from sympy import *
import pandas as pd
import math as m
from data import *


## CONDITIONS and Derivatives for 2nd Design Matrix
# Second Design matrix should be number conditions by number observations? Maybe 10 by 14
b = np.zeros([9,14])

# Sum around the polygon 
ang_sum = 360 - sum(var[6:14]) - var[8] # Equation
ang_diff = np.array(np.zeros(14)) # Initialize 
ang_diff[:] = diff(ang_sum,var[:]) # Take Derivative
ang_sum_w = ang_sum.subs(variables) # Misclosure of Internal Angles

# Sine Law 
sin_41 = sin(a1)/Drs - sin(a4)/Dqr  # Equation
sin_41_diff = [] # Initialize
sin_41_diff[:] = np.array(diff(sin_41,var[:])) # Take Derivative
sin_41_w = sin_41.subs(variables) # Misclosure 

# Sine Law  
sin_58 = sin(a5)/Dtq - sin(a8)/Dst  # Equation
sin_58_diff = [] # Initialize
sin_58_diff[:] = np.array(diff(sin_58,var[:])) # Take Derivative
sin_58_w = sin_58.subs(variables) # Misclosure

# Cosine Law 421
cos_2 = sqrt(Drs**2 + Dqr**2 - (2*Dqr*Drs*cos(a2))) -Dqs # Equation
cos_2_diff = [] # Initialize
cos_2_diff[:] = np.array(diff(cos_2,var[:]))
cos_2_w = cos_2.subs(variables) # Misclosure

# Cosine Law 5678
cos_78 = sqrt(Dst**2 + Dtq**2 - (2*Dst*Dtq*cos(a6+a7))) - Dqs
cos_78_diff = [] # Initialize
cos_78_diff[:] = np.array(diff(cos_78,var[:])) # Take Derivative
cos_78_w = cos_78.subs(variables) # Misclosure

# Sum of Interior Triangle 241
tri_241 = a2 + a4 + a1 - 180# Equation
tri_241_diff = [] # Initialization
tri_241_diff = np.array(diff(tri_241,var[:])) # take Derivative
tri_241_w = tri_241.subs(variables)  # Misclosure

# Sum of interior Triangle 5678
tri_856 = a8 + a5 + a6 + a7 - 180# Equation
tri_856_diff = [] # Initialization
tri_856_diff = np.array(diff(tri_856,var[:])) # take Derivative
tri_856_w = tri_856.subs(variables)  # Misclosure

# Sum of interior Triangle 345
tri_345 = a3 + a4 + a5 + a6 - 180# Equation
tri_345_diff = [] # Initialization
tri_345_diff = np.array(diff(tri_345,var[:])) # take Derivative
tri_345_w = tri_345.subs(variables)  # Misclosure

# Distance Relationship using Cosine law: tri QRS solve dist rs
dr = (sqrt(Dqs**2 + Dqr**2 - (2*Dqs*Dqr*cos(a1))))/(sqrt(Dst**2 + Dtq**2 - (2*Dst*Dtq*cos(a6+a7))))*(sqrt(Dst**2 + Dtq**2 - (2*Dst*Dtq*cos(a6+a7)))/Dqr)*(Dqr/sqrt(Dqs**2 + Dqr**2 - (2*Dqs*Dqr*cos(a1)))) - ((Drs/sin(a1))*(sin(a2)/Dqs)) # Equation
dr_diff = [] # Initialize
dr_diff[:] = np.array(diff(dr,var[:])) # Take Derivative
dr_w = dr.subs(variables) # Misclosure
print(dr_w)


# For loop to sub in derivative values fpr design matrix 
for i in range(14):
    sin_41_diff[i] = sin_41_diff[i].subs(variables)
    sin_58_diff[i] = sin_58_diff[i].subs(variables)
    cos_2_diff[i] = cos_2_diff[i].subs(variables)
    cos_78_diff[i] = cos_78_diff[i].subs(variables)
    tri_241_diff[i] = tri_241_diff[i].subs(variables)
    tri_856_diff[i] = tri_856_diff[i].subs(variables)
    tri_345_diff[i] = tri_345_diff[i].subs(variables)
    dr_diff[i] = dr_diff[i].subs(variables)
    #ang_diff[i] = ang_diff[i].subs(variables)


b[0,:] = ang_diff[:]
b[1,:] = sin_41_diff[:]
b[2,:] = sin_58_diff[:]
b[3,:] = cos_2_diff[:]
b[4,:] = cos_78_diff[:]
b[5,:] = tri_241_diff[:]
b[6,:] = tri_856_diff[:]
b[7,:] = tri_345_diff[:]
b[8,:] = dr_diff[:]

print(np.linalg.matrix_rank(b))
