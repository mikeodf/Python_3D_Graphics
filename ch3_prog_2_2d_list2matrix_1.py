""" ch3 No.2 
Program name: 2d_list2matrix_1.py 
Objective: Convert a Python canvas shape list to numpy matrix of vertices. 

Keywords: 2d canvas list, objects, convert, matrix, vertex 
============================================================================79 
From the book "Python Graphics for Games: Working in 3 Dimensions"

Comments: A triangle specified as a Python list is converted to
a matrix (numpy compatible). 
The rows of the numpy matrix are the x-y vertices of the triangle. 
                                                                                       
Tested on:  Python 2.7, Python 3.2, 
Author: Mike Ohlson de Fine    
================================ 
""" 
import numpy 

#==================================================================== 
triangle_1 = [ 21.0, 40.0   ,4.1, 7.0   ,23.0, 18.3, 21.0, 40.0  ] 
#==================================================================== 

# Convert a Python list into a Numpy matrix of vertices. 
vertex_array_1 = [] 
for i in range(0, len(triangle_1), 2): 
        vertex_x =  triangle_1[i] 
        vertex_y =  triangle_1[i + 1] 
        vertex = [vertex_x, vertex_y]       
        vertex_array_1.append(vertex)  

triangle_1_matrix = numpy.matrix(vertex_array_1) 
#print 'triangle_1_matrix: ' , triangle_1_matrix  # This form only works with python 2.x or lower
print ('triangle_1_matrix: ' , triangle_1_matrix)  # This form  works with python 2.x  and 3.x
''' Results 
    ======= 
triangle_1_matrix:  [[ 21.    40. ] 
                     [  4.1    7. ] 
                     [ 23.    18.3] 
                     [ 21.    40. ]] 
'''
