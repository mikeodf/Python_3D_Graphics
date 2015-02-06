""" ch3 No.6 
Program name: 2d_concatenated_transforms_1.py 
Objective: Demonstrate concatenated transforms. 

Keywords: 2d objects, concatenated operations. 
============================================================================79 
From the book "Python Graphics for Games: Working in 3 Dimensions"

Comments: The same result is achieved in two different ways: 

First - a concatenated matrix = X_Reflect_Matrix()*Y_Reflect_Matrix()*Rotate_Matrix(3.0)*Shear_Matrix(0.5,0.7)*Scale_Matrix(1.3,0.8) 
 = concatenation =  [[ 1.41540945  0.50889301] 
                     [ 0.71743716  0.73554599]], 
is multiplied by the vertices of the object being transformed. 

Second - a series of matrix multiplications are performed, with 
the result of each multiplication being fed to the subsequent one. 
                                                                                      
Tested on: Python 2.6, Python 2.7, Python 3.2, 
Author: Mike Ohlson de Fine    
================================ 
""" 
from Tkinter import * 
#from tkinter import *   # Use this instead of the above for python version 3.x
import numpy 
import math 
import faces 

root = Tk() 
root.title('Chained Transformations: Face reflected, sheared, rotated and Scaled.') 
cw = 650                                      # canvas width. 
ch = 400                                      # canvas height. 
canvas_1 = Canvas(root, width=cw, height=ch, background="white") 
canvas_1.grid(row=0, column=1) 
#==================================================================== 
# The scaling matrix. 
def Scale_Matrix(x_scale_factor, y_scale_factor): 
    """ Scaling matrix for 2D shapes. """ 
    scaling_matrix  = numpy.matrix([[ x_scale_factor, 0.0], [0.0,  y_scale_factor]]) 
    return scaling_matrix 

# The x-reflection matrix (vertical reflections). 
def X_Reflect_Matrix(): 
    """ Reflect matrix shape from the X-axis. """ 
    xreflect_matrix  =  numpy.matrix([[-1.0, 0.0],
                                      [ 0.0, 1.0] ]) 
    return xreflect_matrix 

# The y-reflection matrix (horizontal reflections). 
def Y_Reflect_Matrix(): 
    """ Reflect matrix shape from the Y-axis. """ 
    YReflect_Matrix  = numpy.matrix([[1.0,   0.0],
                                     [ 0.0, -1.0] ]) 
    return YReflect_Matrix 

# The rotate in the plane matrix. 
def Rotate_Matrix(theta): 
    """ Rotate points theta (radians)around the Z-axis.    """ 
    rotate_matrix = numpy.matrix([ [math.cos(theta),  -math.sin(theta)],
                                   [math.sin(theta),   math.cos(theta)] ])                
    return rotate_matrix 

# The combined x and y shear matrix. 
def Shear_Matrix(shear_x, shear_y): 
    """ Shear a matrix shape simultaneously in the X- and Y-directions. 
    """ 
    shear_matrix = numpy.matrix([ [      1.0,     shear_x],
                                  [shear_y,           1.0]])                 
    return shear_matrix 

# Convert a Python list into a Numpy matrix of vertices. 
def list2matrix(xy_shape): 
    """ Convert a Python list (xy list of a shape) into a 
        Numpy matrix of vertices 
    """ 
    vertex_array = [] 
    for i in range(0, len(xy_shape), 2): 
        vertex_x =  xy_shape[2 * i] 
        vertex_y =  xy_shape[2 * i + 1] 
        vertex = [vertex_x, vertex_y]       
        vertex_array.append(vertex)  
    vertex_matrix = numpy.matrix(vertex_array) 
    return  vertex_matrix 

# Re-craft a 2D matrix into a nice Python list for display on the canvas. 
def matrix2list(vertex_matrix): 
    """ Convert Numpy matrix of vertices into a Python list (xy list of a shape) 
    """ 
    flat_array = vertex_matrix.tolist() 
    xy_list = [] 
    for i in range(0, len(flat_array)): 
         xy_list.append( flat_array[i][0] ) 
         xy_list.append( flat_array[i][1] ) 
    return xy_list 


# Series sequential transforms. 
for set in range(len(faces.face_set)): 
     triangle_matrix = list2matrix(faces.face_set[set])                 # step 1 
     xreflected_triangle = triangle_matrix * X_Reflect_Matrix()         # step 2 
     yreflected_triangle = xreflected_triangle * Y_Reflect_Matrix()     # step 3 
     rotated_triangle = yreflected_triangle * Rotate_Matrix(3.0)        # step 4 
     sheared_triangle = rotated_triangle * Shear_Matrix(0.5, 0.7)       # step 5 
     bigger_triangle_matrix = sheared_triangle * Scale_Matrix(1.3,0.8)  # step 6 
     bigger_triangle = matrix2list(bigger_triangle_matrix)              # step 7 
     #canvas_1.create_line(bigger_triangle, fill = 'blue', width = 3)   # step 8 

# Concatenation of matrix operations. 
concatenation  = X_Reflect_Matrix() *  Y_Reflect_Matrix() * Rotate_Matrix(3.0) * Shear_Matrix(0.5, 0.7) * Scale_Matrix(1.3,0.8) 
print ('concatenation: ' ,concatenation)   # For python 3.2 use this instead of the line above. 
for set in range(len(faces.face_set)): 
    face_matrix = list2matrix(faces.face_set[set])                      # step 1 
    face_caboodle =  face_matrix * concatenation                        # steps 2 - 6 
    view_face = matrix2list(face_caboodle)                              # step 7 
    canvas_1.create_line(view_face, fill = 'red', width = 3)            # step 8 
    canvas_1.create_line(faces.face_set[set], fill = 'green', width = 3)# Untransformed original. 

root.mainloop()
