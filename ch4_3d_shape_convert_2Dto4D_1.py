"""   ch4 No.1 
Program name: 3d_shape_convert_2Dto4D_1.py 
Objective: Convert a 2D planar shape into a list of 4D vertex vectors. 

"canonical" (definition): A mathematical expression in the simplest or standard form. 

Keywords: 3d shape, 2d shapes, conversion function. 
==================================================================79 
From the book "Python Graphics for Games: Working in 3 Dimensions"

Comments: 2d shape vertices are converted to lists of 4d (homogeneous) matrix/vectors. 
Each vector is the location of a vertex in 3d (homogeneous) space. 

A 'shape' is a 2d planar line of arbtrary number of segments. 
The final list corresponds to a shape object in 3 dimensions. 
The shape object is a Python list of 4D vertices. 

Tested on: Python 2.6, Python 2.7.3, Python 3.2.3       
Author:  Mike Ohlson de Fine 
================================ 
""" 
import numpy 

# 2D SHAPE - A simple fish shape in the x-y plane 
fish_1 = [ 169.2,161.6  ,  309.2,102.3  ,  360.0,139.5  ,  316.4,160.9  ,  180.0,118.7 ] 

#===================================================
# CONVERSION OF A 2D LIST TO A MATRIX OF 4D VERTICES. 
#===================================================
def twod_shape_2_homogeneous_matrix(twod_shape): 
    """ Convert a 2D shape list into a homogeneous 4D matrix (numpy form). 
        The z coordinate is zero. ie. z = 0. 
    """ 
    homogenous_4d_array = [] 
    for i in range(0, len(twod_shape), 2): 
        new_x =  twod_shape[2 * i] 
        new_y =  twod_shape[2 * i + 1] 
        new_z =  0.0 
        new_w = 1 
        new_vertex = [new_x, new_y, new_z, new_w]       
        homogenous_4d_array.append(new_vertex)  

    homogenous_4d_mat = numpy.matrix(homogenous_4d_array) 
    return homogenous_4d_mat 

#===================================================
# CONVERT 2D SHAPES TO 4D MATRICES (NUMPY FORM) 
#===================================================
fish_1_2d24d_mat = twod_shape_2_homogeneous_matrix(fish_1) 
print ('fish_1_2d24d_mat:', fish_1_2d24d_mat) # Use instead of the above for Python 3.x.

''' RESULT 
fish_1_2d24d_mat: 
[[ 169.2  161.6    0.     1. ] 
 [ 309.2  102.3    0.     1. ] 
 [ 360.   139.5    0.     1. ] 
 [ 316.4  160.9    0.     1. ] 
 [ 180.   118.7    0.     1. ]] 
'''
