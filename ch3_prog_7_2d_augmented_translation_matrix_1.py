""" ch3 No.7 
Program name: 2d_augmented_translation_matrix_1.py 
Objective: Demonstration translation (shifting) using the augmented matrix. 

Keywords: 2d objects, augmented matrix, translation, shift functions. 
============================================================================79 
From the book "Python Graphics for Games: Working in 3 Dimensions"

Comments: To support the translation (shifting sideways and up or down),
 we need to work with augmented matrices. 
When the vertices of 2D shapes are extended by one "dimension", then objects
can be shifted by multiplication with the aaugmented matrix. 

The original data must be expressed as vertices which can then be converted
into matrices (by the Numpy module). 
Simple matrix multiplication will then achieve the translation but the result
is another matrix which must finally be flattened into a simple x-y list 
of coordinates that tkinter "create_line()" function will understand. 
                                                                                      
Tested on: Python 2.7, Python 3.2, 
Author: Mike Ohlson de Fine    
================================ 
""" 
from Tkinter import * 
# from tkinter import *   # Use this instead of the above for python version 3.x
import numpy 
import math 
import faces 

root = Tk() 
root.title('Faces Translated: x+=100, y+=50.') 
cw = 700                                      # canvas width. 
ch = 550                                      # canvas height. 
canvas_1 = Canvas(root, width=cw, height=ch, background="white") 
canvas_1.grid(row=0, column=1) 

#==================================================================== 
# Convert a Python list into a homogeneous Numpy matrix ( 2D/3D) of vertices. 
# This form is necessary to support translation matrices. 
def list2matrix_homog(xy_shape): 
    """ Convert a Python list (xy list of a shape) into a 
        Numpy matrix of vertices 
    """ 
    vertex_array = [] 
    for i in range(0, len(xy_shape), 2): 
        vertex_x =  xy_shape[ i] 
        vertex_y =  xy_shape[i + 1] 
        extra_element = 1.0 
        vertex = [vertex_x, vertex_y, extra_element]       
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
 

def Translate(shift_x, shift_y): 
    """ Shift the shape in the x-direction and y-direction by shift_x 
        and shift_y respectively.
    """ 
    shifted = numpy.matrix([[1.0,           0.0,    1.0  ],
                            [0.0,           1.0,    1.0  ],
                            [shift_x,   shift_y,    1.0  ]]) 
    return shifted 

# Translation variables. 
x_shift = 100.0 
y_shift = 50.0 

# View the original face. 
for set in range(len(faces.face_set)): 
    face_matrix = list2matrix_homog(faces.face_set[set])                  # step 1 
    canvas_1.create_line(faces.face_set[set], fill = 'green', width = 3)  # Original 

# Translate and view faces. 
for i in range(3): 
    for set in range(len(faces.face_set)): 
         face_matrix = list2matrix_homog(faces.face_set[set])              # step 1 
         shifted_face_matrix = face_matrix * Translate(x_shift, y_shift)   # step 2 
         xylist_shifted_face = matrix2list(shifted_face_matrix)            # step 3 
         canvas_1.create_line(xylist_shifted_face, fill = 'red', width = 3)# step 4 
    x_shift += 100 
    y_shift += 50 

root.mainloop()
