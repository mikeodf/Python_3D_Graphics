"""   ch4 No.5 
Program name: 3d_shape_set_2Dto4D_rotation_1.py 
Objective: Convert a 2D planar shape set into a list of 4D vertex vectors, 
and then perform transform geometry (scaling, translation and rotation). 

Keywords: 3d shape, 2d shapes, conversion of shape sets, transform sets. 
============================================================================79 
From the book "Python Graphics for Games: Working in 3 Dimensions"

Comments: 2d shape vertices are converted to lists of 4d (homogeneous) matrix/vectors. 
Each vector is the location of a vertex in 3d (homogeneous) space. 

A 'shape' is a 2d planar line of arbtrary number of segments. 
A 'set' is a collection of separate shapes. 

The final list "fish_set" corresponds to a set of shape objects in 3 dimensions. 
The shape object is a list of 4D vertices. 

Tested on: Python 2.6, Python 2.7.3, Python 3.2.3       
Author:  Mike Ohlson de Fine 
================================ 
""" 
from Tkinter import * 
# from tkinter import *   # Use this instead of the above for python version 3.x
import math 
import numpy 
import matrix_transforms 

root = Tk() 
root.title('Rotate Fish Set around X,Y and Z together') 
cw = 600                                      # canvas width. 
ch = 550                                       # canvas height. 
canvas_1 = Canvas(root, width=cw, height=ch, background="#110011") 
canvas_1.grid(row=0, column=1) 

cycle_period= 30 

rad_one_deg = math.pi/180.0 
rad_angle = 0.0 

# 2D SHAPE - A simple fish shape in the x-y plane 
fish_1 = [ 169.2,161.6  ,  309.2,102.3  ,  360.0,139.5  ,  316.4,160.9  ,  180.0,118.7 ] 
fish_2 = [ 515.0,270.9  ,  421.4,173.0  ,  325.7,196.6  ,  299.22,243.0  ,  392.8,291.6  ,  498.5,211.6 ] 
fish_3 = [ 164.2,306.6  ,  229.2,271.6  ,  317.1,298.7  ,  212.8,305.2  ,  149.2,265.9 ] 
fish_4 = [ 362.8,378.7  ,  300.7,353.0  ,  260.7,367.3  ,  292.8,383.7  ,  370.7,347.3  ,  424.2,375.9  ,  462.1,355.2  ,  412.1,336.6  ,  361.4,362.3 ] 

fish_set = [ fish_1, fish_2, fish_3, fish_4 ] 
kulas = [ 'yellow', 'orange', 'purple', 'magenta' ] 
#==================================================================
# CONVERSION OF A 2D LIST TO A MATRIX OF 4D VERTICES. 
#================================================================== 
def twod_shape_2_homogeneous_matrix(twod_shape): 
    """ Convert a 2D shape list into a homogeneous 4D matrix (numpy form). 
        The z coordinate is zero. ie. z = 0. 
    """ 
    homogenous_4d_array = [] 
    for i in range(len(twod_shape)/2): 
        new_x =  twod_shape[2 * i] 
        new_y =  twod_shape[2 * i + 1] 
        new_z =  0.0 
        new_w = 1 
        new_vertex = [new_x, new_y, new_z, new_w]       
        homogenous_4d_array.append(new_vertex)  

    homogenous_4d_mat = numpy.matrix(homogenous_4d_array) 
    return homogenous_4d_mat 

# For Display - Downconvert a 3D/4D matrix down to a 2D list. 
def fourd_shape_2_twod_line(numpy_threed_matrix, kula, line_width): 
    """ Convert a 3D homogeneous matrix (numpy form) to a list for 'create_line'. 
    """ 
    bbb = numpy_threed_matrix.tolist() 
    twod_line = [] 
    for i in range(0, len(bbb)): 
        twod_line.append( bbb[i][0] ) 
        twod_line.append( bbb[i][1] ) 
    canvas_1.create_line( twod_line, width = line_width, fill=kula ) 
    return twod_line 

#======================================================================== 
# Convert 2D set SET to 4D matrices (NUMPY FORM). 
fish_4d_set_mat = [] 
for set in range(len(fish_set)): 
    temp = twod_shape_2_homogeneous_matrix(fish_set[set]) 
    fish_4d_set_mat.append(temp) 

# Move origin to center-of-rotation(cor). 
for set in range(len(fish_set)): 
    fish_4d_set_mat[set] = fish_4d_set_mat[set] * matrix_transforms.T_translate(-300.0, -330.0, 0.0) 

# Dynamic rotation of fish_1 around axes within the shape 
for i in range (100): 
    for set in range(len(fish_4d_set_mat)): 
        fish_4d_set_mat[set] = fish_4d_set_mat[set] * matrix_transforms.T_rotx(rad_angle)   #  X rotation.
        fish_4d_set_mat[set] = fish_4d_set_mat[set] * matrix_transforms.T_roty(rad_angle)   #  Y rotation.
        fish_4d_set_mat[set] = fish_4d_set_mat[set] * matrix_transforms.T_rotz(rad_angle)   #  Z rotation.
        view_fish_set = fish_4d_set_mat[set] * matrix_transforms.T_translate( 300.0, 280.0, 0.0) 
        fourd_shape_2_twod_line(view_fish_set, kulas[set], 1)   
        
    rad_angle = rad_one_deg * 10.0 

root.mainloop()
