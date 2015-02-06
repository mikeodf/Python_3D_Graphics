""" ch3 No.4 
Program name: 2d_matrix_conversion_1.py 
Objective: Construct matrix converters and transforms for scaling of 2D objects. 
The operators should be expressed as functions. 

Keywords: 2d objects, matrix, scaling, amplification, functions,display. 
============================================================================79 
From the book "Python Graphics for Games: Working in 3 Dimensions"

Comments: The original data must be expressed as vertices which can then be
 converted into matrices (by the Numpy module). 
A scaling matrix is created: 
Scaling_Matrix  = numpy.matrix([[ x_scale_factor, 0.0], [0.0,  y_scale_factor]]) 
Simple matrix multiplication will then achieve the amplification but the
result is another matrix which must finally be flattened into a simple
x-y list of coordinates that the tkinter "create_line()" function will understand. 
                                                                                      
Tested on: Python 2.6, Python 2.7, Python 3.2, 
Author: Mike Ohlson de Fine    
================================ 
""" 
from Tkinter import * 
# from tkinter import * # Use this instead of the above for python version 3.x
import numpy 

root = Tk() 
root.title('Triangles Amplified/scaled: X*15, Y*5.') 
cw = 700                                      # canvas width. 
ch = 250                                      # canvas height. 
canvas_1 = Canvas(root, width=cw, height=ch, background="white") 
canvas_1.grid(row=0, column=1) 

#==================================================================== 
triangle_1 = [ 21.0, 40.0   ,4.1 , 7.0    ,23.0 , 18.3,   21.0, 40.0  ] 
triangle_2 = [ 5.3 , 4.8    ,42.4, 7.5    ,23.6 , 17.4,    5.3,  4.8  ] 
triangle_3 = [ 42.6, 10.0   ,23.7, 40.6   ,23.8 , 18.2 ,  42.6, 10.0  ] 
#==================================================================== 

# Convert a Python list into a Numpy matrix of vertices. 
def list2matrix(xy_shape): 
    """ Convert a Python list (xy list of a shape) into a 
        Numpy matrix of vertices 
    """ 
    vertex_array = [] 
     for i in range(0, len(xy_shape), 2): 
          vertex_x =  xy_shape[i] 
          vertex_y =  xy_shape[i + 1] 
          vertex = [vertex_x, vertex_y]       
          vertex_array.append(vertex)  
     vertex_matrix = numpy.matrix(vertex_array) 
     return  vertex_matrix 

# Re-craft a 2D matrix into a nice Python list for display on the canvas. 
def matrix2list(vertex_matrix): 
    """ Convert Numpy matrix of vertices into a Python list
        (xy list of a shape) 
    """ 
    flat_array = vertex_matrix.tolist() 
    xy_list = [] 
    for i in range(0, len(flat_array)): 
         xy_list.append( flat_array[i][0] ) 
         xy_list.append( flat_array[i][1] ) 
    return xy_list 

# Size amplification factors - note horizontal is 3x more than vertical. 
x_scale_factor = 15.0 
y_scale_factor = 5.0 

# Step 1: Construct the scaling matrix. 
Scaling_Matrix  = numpy.matrix([[ x_scale_factor, 0.0], [0.0,  y_scale_factor]]) 

# Step 2: Transform the Python list into a list of individual vertices. 
triangle_1_matrix = list2matrix(triangle_1) 
triangle_2_matrix = list2matrix(triangle_2) 
triangle_3_matrix = list2matrix(triangle_3) 

# Step 3: Perform the matrix multiplication that does the scaling. 
# Note: The result is in the wrong format for display on a canvas. 
bigger_triangle_matrix_1 = triangle_1_matrix * Scaling_Matrix 
bigger_triangle_matrix_2 = triangle_2_matrix * Scaling_Matrix 
bigger_triangle_matrix_3 = triangle_3_matrix * Scaling_Matrix 

# Step 4:Convert the scaled matrix to  Python xy-list. 
bigger_triangle_1 = matrix2list(bigger_triangle_matrix_1) 
bigger_triangle_2 = matrix2list(bigger_triangle_matrix_2) 
bigger_triangle_3 = matrix2list(bigger_triangle_matrix_3) 

# Step 5: Display the results. 
canvas_1.create_line(triangle_1) 
canvas_1.create_line(triangle_2) 
canvas_1.create_line(triangle_3) 
canvas_1.create_line(bigger_triangle_1, width = 3) 
canvas_1.create_line(bigger_triangle_2, width = 3) 
canvas_1.create_line(bigger_triangle_3, width = 3) 

root.mainloop()
