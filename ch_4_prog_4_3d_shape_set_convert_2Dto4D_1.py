"""   ch4 No.4 
Program name: 3d_shape_set_convert_2Dto4D_1.py 
Objective: Convert a 2D planar shape into a list of 4D vertex vectors. 

Keywords: 3d shape, 2d shapes, conversion function. 
============================================================================79 
From the book "Python Graphics for Games: Working in 3 Dimensions"

Comments: 2d shape vertices are converted to lists of 4d (homogeneous) matrix/vectors. 
Each vector is the location of a vertex in 3d (homogeneous) space. 

A 'shape' is a 2d planar line of arbtrary number of segments. 
The final list corresponds to a shape object in 3 dimensions. 
The shape object is a list of 4D vertices. 

Tested on:  Python 2.7.3, Python 3.2.3       
Author:  Mike Ohlson de Fine 
================================ 
""" 
import numpy 

# 2D SHAPES - Four simple fish shapes in the x-y plane 
fish_1 = [ 169.2,161.6  ,  309.2,102.3  ,  360.0,139.5  ,  316.4,160.9  ,  180.0,118.7 ] 
fish_2 = [ 515.0,270.9  ,  421.4,173.0  ,  325.7,196.6  ,  299.22,243.0  ,  392.8,291.6  ,  498.5,211.6 ] 
fish_3 = [ 164.2,306.6  ,  229.2,271.6  ,  317.1,298.7  ,  212.8,305.2  ,  149.2,265.9 ] 
fish_4 = [ 362.8,378.7  ,  300.7,353.0  ,  260.7,367.3  ,  292.8,383.7  ,  370.7,347.3  ,  424.2,375.9  ,  462.1,355.2  ,  412.1,336.6  ,  361.4,362.3 ] 

fish_set = [ fish_1, fish_2, fish_3, fish_4 ]  # Create the set.
#==================================================================
# CONVERSION OF A 2D LIST TO A MATRIX OF 4D VERTICES. 
#================================================================== 
def twod_shape_2_homogeneous_matrix(twod_shape): 
    """ Convert a 2D shape list into a homogeneous 4D matrix (numpy form). 
        The z coordinate is zero. ie. z = 0. 
    """ 
    homogenous_4d_array = [] 
    for i in range(0, len(twod_shape), 2): 
        new_x =  twod_shape[i] 
        new_y =  twod_shape[i + 1] 
        new_z =  0.0 
        new_w = 1 
        new_vertex = [new_x, new_y, new_z, new_w]       
        homogenous_4d_array.append(new_vertex)  

    homogenous_4d_mat = numpy.matrix(homogenous_4d_array) 
    return homogenous_4d_mat 

#=================================================================
# Convert 2D set SET to 4D matrices (NUMPY FORM). 
#=================================================================
fish_4d_set_mat = [] 
for set in range(len(fish_set)): 
    temp = twod_shape_2_homogeneous_matrix(fish_1) 
    fish_4d_set_mat.append(temp) 

print 'fish_4d_set_mat:' 
print fish_4d_set_mat 

''' RESULT 
fish_4d_set_mat: 
[matrix([[ 169.2,  161.6,  0. ,  1. ], 
         [ 309.2,  102.3,  0. ,  1. ], 
         [ 360. ,  139.5,  0. ,  1. ], 
         [ 316.4,  160.9,  0. ,  1. ], 
         [ 180. ,  118.7,  0. ,  1. ]]), 
 matrix([[ 169.2,  161.6,  0. ,  1. ], 
         [ 309.2,  102.3,  0. ,  1. ], 
         [ 360. ,  139.5,  0. ,  1. ], 
         [ 316.4,  160.9,  0. ,  1. ], 
         [ 180. ,  118.7,  0. ,  1. ]]), 
 matrix([[ 169.2,  161.6,  0. ,  1. ], 
         [ 309.2,  102.3,  0. ,  1. ], 
         [ 360. ,  139.5,  0. ,  1. ], 
         [ 316.4,  160.9,  0. ,  1. ], 
         [ 180. ,  118.7,  0. ,  1. ]]), 
 matrix([[ 169.2,  161.6,  0. ,  1. ], 
         [ 309.2,  102.3,  0. ,  1. ], 
         [ 360. ,  139.5,  0. ,  1. ], 
         [ 316.4,  160.9,  0. ,  1. ], 
         [ 180. ,  118.7,  0. ,  1. ]])] 
''' 
