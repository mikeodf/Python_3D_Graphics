""" ch4 No.3
Program name: 3d_2d_shape_conversion_and_rotation_1.py 
Objective: Rotate a shape about X, Y, Z or all 
selected axes in any position. 
 
Keywords: 3d projections, 2d shapes, transforms, arbitrary rotation.. 
============================================================================79
From the book "Python Graphics for Games: Working in 3 Dimensions"
 
Comments: The five vertices constituting the fish shape are gives a a list of 
x,y coordinates. The function "twod_shape_2_homogeneous_matrix(twod_shape)" 
converts them to an augmented 4d (homogeneous) list of vectors. 
Each vector is the location of a vertex in 3d (homogeneous) space. 

Tested on: Python 2.7.3, Python 3.2.3       
Author:  Mike Ohlson de Fine 
================================ 
""" 
from Tkinter import * 
#from tkinter import *   # Use this instead of the above for python version 3.x
import math 
import numpy 
import matrix_transforms 

root = Tk() 
root.title('Rotate Fish Shape around X,Y and Z simultaneously') 
cw = 600                                   # canvas width. 
ch = 600                                   # canvas height. 
canvas_1 = Canvas(root, width=cw, height=ch, background="#110011") 
canvas_1.grid(row=0, column=1) 

cycle_period= 30 

rad_one_deg = math.pi/180.0 
rad_angle = 0.0 

# 2D VERSION - CO-PLANAR 
tiny_fish =  [-1.61,0.50,  0.75,-0.50,  1.61,0.13,  0.87,0.49,   -1.43,-0.22] 
#=================================================================
# 2 ESSENTIAL GRAPHIC VECTOR TYPE CONVERSIONS 
#============================================= 
# For Display - Downconvert a 3D/4D matrix down to a 2D list. 
def fourd_shape_2_twod_line(numpy_threed_matrix, kula, line_thickness): 
    """ Convert a 3D homogeneous matrix (numpy form) to a list for 'create_line'. 
    """ 
    bbb = numpy_threed_matrix.tolist() 
    twod_line = [] 
    for i in range(0, len(bbb)): 
        twod_line.append( bbb[i][0] ) 
        twod_line.append( bbb[i][1] ) 
    canvas_1.create_line( twod_line, width = line_thickness,  fill=kula ) 
    return twod_line 

# Expand a 2D shape -> A 4d (homogeneous) matrix array 
def twod_shape_2_homogeneous_matrix(twod_shape): 
    """ Convert a 2D shape list into a homogeneous 4D matrix (numpy form). 
        The z coordinate is zero. z = 0. 
    """ 
    homogenous_4d_array =[] 
    for i in range(0, len(twod_shape), 2): 
        new_x =  twod_shape[ i] 
        new_y =  twod_shape[ i + 1] 
        new_z =  0.0 
        new_w = 1 
        new_vertex = [new_x, new_y, new_z, new_w]       
        homogenous_4d_array.append(new_vertex)  
    homogenous_4d_mat = numpy.matrix(homogenous_4d_array) 
    return homogenous_4d_mat 


#======================================================================= 
# CONVERT 2D SHAPES TO 4D MATRICES (NUMPY FORM) 
fish_2d24d_mat = twod_shape_2_homogeneous_matrix(tiny_fish) 
# Scale the tiny fish up into a big fish 
bigfish_mat = fish_2d24d_mat * matrix_transforms.T_scaling(150.0 , 200.0, 0.0) 

# Dynamic rotation of fish_1 around axes within the shape 
bigfish_view = bigfish_mat * matrix_transforms.T_translate( 300.0, 300.0, 0.0)  # Viewing convenience. 
fourd_shape_2_twod_line(bigfish_view, 'yellow', 4)   

for i in range (160): 
    bigfish_mat = bigfish_mat * matrix_transforms.T_rotx(rad_angle) # Rotation about X axis. 
    bigfish_mat = bigfish_mat * matrix_transforms.T_roty(rad_angle) # Rotation about Y axis. 
    bigfish_mat = bigfish_mat * matrix_transforms.T_rotz(rad_angle) # Rotation about Z axis. 
    bigfish_view = bigfish_mat * matrix_transforms.T_translate( 300.0, 300.0, 0.0) # Viewing convenience. 
    fourd_shape_2_twod_line(bigfish_view, 'green', 1)   
    rad_angle = rad_one_deg * 5.0 

root.mainloop()
