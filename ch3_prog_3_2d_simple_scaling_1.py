"""  ch3 No.3 
Program name: 2d_simple_scaling_1.py 
Objective: Demonstrate the matrix scaling of 2D objects.. 

Keywords: 2d objects, scaling, amplification, display. 
============================================================================79 
From the book "Python Graphics for Games: Working in 3 Dimensions"

Comments: The original data must be expressed as vertices which can then be
converted into matrices (by the Numpy module). 
A scaling matrix is created. Simple matrix multiplication will then achieve
the amplification but the result is another matrix which must finally be
flattened into a simple x-y list of coordinates that tkinter
"create_line()" function will understand. 
                                                                                      
Tested on: Python 2.7, Python 3.2, 
Author: Mike Ohlson de Fine    
================================ 
""" 
from Tkinter import * 
# from tkinter import *   # Use this instead of the above for python version 3.x
import numpy 

root = Tk() 
root.title('Triangles Amplified/scaled') 
cw = 500                                     # canvas width. 
ch = 500                                      # canvas height. 
canvas_1 = Canvas(root, width=cw, height=ch, background="white") 
canvas_1.grid(row=0, column=1) 

#==================================================================== 
triangle_1 = [ 21.0, 40.0   ,4.1, 7.0   ,23.0, 18.3, 21.0, 40.0  ] 
#==================================================================== 

# Size amplification factors - note horizontal is 3x more than vertical. 
x_scale_factor = 15.0 
y_scale_factor = 5.0 

# Step 1: Construct the scaling matrix. 
Scaling_Matrix  = numpy.matrix([[ x_scale_factor, 0.0], [0.0,  y_scale_factor]]) 
 
# Step 2: Transform the Python list into a list of individual vertices. 
triangle_vertex_1 = [ 21.0,  40.0 ]  
triangle_vertex_2 = [ 4.1,   7.0  ]   
triangle_vertex_3 = [ 23.0, 18.3  ] 
triangle_vertex_4 = [ 21.0,  40.0 ]  

# Step 3: Combine the vertices into a list and then convert to a Numpy matrix. 
triangle_shape_1 = [ triangle_vertex_1, triangle_vertex_2, triangle_vertex_3, triangle_vertex_4 ] 
triangle_shape_matrix_1 = numpy.matrix(triangle_shape_1) 

# Step 4: Perform the matrix multiplication that does the scaling. 
# Note: The result is in the wrong format for display on a canvas. 
bigger_triangle_matrix_1 = triangle_shape_matrix_1 * Scaling_Matrix 
bigger_triangle_wronglist_1 = bigger_triangle_matrix_1.tolist() 

# Step 5: Re-craft the resultant matrix into a nice Python list for the canvas. 
bigger_triangle_goodlist_1 = [] 
for i in range(0, len(bigger_triangle_wronglist_1)): 
        bigger_triangle_goodlist_1.append( bigger_triangle_wronglist_1[i][0] ) 
        bigger_triangle_goodlist_1.append(bigger_triangle_wronglist_1[i][1] ) 

canvas_1.create_line(triangle_1, fill ='green', width = 2) 
canvas_1.create_line(bigger_triangle_goodlist_1, fill ='red', width = 3) 
root.mainloop()

# Just for the record, show the various data structures. 
# Note that numpy matrices have no comma separators - slightly alien creatures they are. 

# Use the following 9 instructions with python 2.x and  python 3.x
print ('Scaling_Matrix: ' , Scaling_Matrix) 
print (' ...............................') 
print ('triangle_matrix_1: ' , triangle_shape_matrix_1) 
print (' ...............................') 
print ('bigger_triangle_matrix_1: ' , bigger_triangle_matrix_1) 
print (' ...............................') 
print ('bigger_triangle_wronglist_1: ' , bigger_triangle_wronglist_1) 
print (' ...............................') 
print ('bigger_triangle_goodlist_1: ' , bigger_triangle_goodlist_1 )  

''' Results 
    ======= 
Scaling_Matrix:  [[ 5.  0.] 
                  [ 0.  8.]] 
 ............................... 
triangle_matrix_1:  [[ 21.   40. ] 
                     [  4.1   7. ] 
                     [ 23.   18.3]] 
 ............................... 
bigger_triangle_matrix_1:  [[ 105.   320. ] 
                            [  20.5   56. ] 
                            [ 115.   146.4]] 
 ............................... 
bigger_triangle_wronglist_1:  [[105.0, 320.0], [20.5, 56.0], [115.0, 146.4]] 
 ............................... 
bigger_triangle_goodlist_1:  [105.0, 320.0, 20.5, 56.0, 115.0, 146.4] 
''' 
