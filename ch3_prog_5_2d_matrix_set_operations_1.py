""" ch3 No.5 
Program name: 2d_matrix_set_operations_1.py 
Objective: Construct matrix converters and transforms for scaling of 2D objects. 
The operators should be expressed as functions and sets of objects 
processed as a single entity. 

Keywords: 2d objects, matrix, scaling, amplification, functions,display. 
============================================================================79 
From the book "Python Graphics for Games: Working in 3 Dimensions"

Comments: The original data must be expressed as vertices which can then be
 converted into matrices (by the Numpy module). 
A scaling matrix is created. Simple matrix multiplication will then achieve
the amplification but the result is another matrix which must finally be 
flattened into a simple x-y list of coordinates that tkinter "create_line()"
function will understand. 
                                                                                      
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
triangle_1 = [ 21.0, 40.0   ,4.1, 7.0   ,23.0, 18.3, 21.0, 40.0 ] 
triangle_2 = [ 5.3 , 4.8   ,42.4, 7.5   ,23.6 , 17.4  ,5.3 , 4.8  ] 
triangle_3 = [ 42.6, 10.0   ,23.7, 40.6  ,23.8, 18.2 , 42.6, 10.0   ] 
#==================================================================== 
# Now do everything by sets. 
triangle_shape_set = [ triangle_1, triangle_2, triangle_3 ] 

# Convert a Python list into a Numpy matrix of vertices. 
def list2matrix(xy_shape): 
    """ Convert a Python list (xy list of a shape) into a 
        Numpy matrix of vertices 
    """ 
    vertex_array = [] 
    for i in range(0, len(xy_shape), 2): 
        vertex_x =  xy_shape[ i] 
        vertex_y =  xy_shape[ i + 1] 
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

# Size amplification factors - note horizontal is 3x more than vertical. 
x_scale_factor = 15.0 
y_scale_factor = 5.0 

# Step 1: Construct the scaling matrix. 
Scaling_Matrix  = numpy.matrix([[ x_scale_factor, 0.0], [0.0,  y_scale_factor]]) 

for set in range(len(triangle_shape_set)): 
     triangle_matrix = list2matrix(triangle_shape_set[set])         # step 2 
     bigger_triangle_matrix = triangle_matrix * Scaling_Matrix      # step 3 
     bigger_triangle = matrix2list(bigger_triangle_matrix)          # step 4 
     canvas_1.create_line(bigger_triangle, fill = 'red', width = 3) # step 5 
     canvas_1.create_line(triangle_shape_set[set], fill = 'green')  # step 6 

root.mainloop() 
