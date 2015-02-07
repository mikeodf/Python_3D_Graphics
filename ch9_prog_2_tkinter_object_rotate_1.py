""""   ch9 No.2   
Program name: tkinter_object_rotate_1.py 
Objective: Animated display of a 3D object using tkinter. 

Keywords: tkinter, animation, rotation geometry, vertices, faces 
============================================================================79 
From the book "Python Graphics for Games: Working in 3 Dimensions"

Comments: For objects or shapes with less than 100 vertices tkinter 
rendering speed are acceptable but are not adequate for high numbers of vertices. 

Tested on: Python 2.6, Python 2.7.3, Python 3.2.3 
Author:          Mike Ohlson de Fine 
""" 
import math 
import time 
import matrix_transforms 
import numpy 

faces =  [ 
 [[  1.0,   0.0,   0.0, 1.0], [ -1.0, 0.0,  -0.0, 1.0], [  0.0, -1.5,  -0.0, 1.0], [  1.0,  0.0,   0.0, 1.0]], 
 [[ -1.0,  -0.0, -1.05, 1.0], [  0.0, 0.5, -0.05, 1.0], [  1.0, -0.0, -1.05, 1.0], [ -1.0, -0.0, -1.05, 1.0]], 
 [[-1.05,  -0.0,  -1.0, 1.0], [-1.05, 0.0,   1.0, 1.0], [-0.05,  0.5,  -0.0, 1.0], [-1.05, -0.0,  -1.0, 1.0]], 
 [[ 1.05,   0.0,   1.0, 1.0], [ 1.05, 0.0,  -1.0, 1.0], [ 0.05,  0.5,  -0.0, 1.0], [ 1.05,  0.0,   1.0, 1.0]], 
 [[ -1.0,   0.0,  1.05, 1.0], [  0.0, 0.5,  0.05, 1.0], [  1.0,  0.0,  1.05, 1.0], [ -1.0,  0.0,  1.05, 1.0]]] 

''' Above are the vertices for four triangles. One triangle per line. 
    The fourth vertex in each line and is a duplicate of the first. 
    This allows the triangle to be completed as three line segments if the  "canvas_1.create_line( ... )" 
    option is chosen. For polygons the fourth vertex in each line is redundant. 
''' 
for i in range(len(faces)): 
    ''' This converts the simple python vertex lists into proper numpy matrices that are 
        in the correct form for matrix transforms - necessary for the fast geometry transformation 
        used to achieve the animation. 
    ''' 
    for j in range(len(faces[i])):      
        faces[i][j]   = numpy.matrix(faces[i][j])    # Convert to Numpy matrices. 

# ==================================================================== 
#  SHAPE TRANSFORM TESTING 
# ========================== 
from Tkinter import * 
#from tkinter import *
root = Tk() 
root.title('Move tkinter objects in 3D') 
cw = 400                                      # canvas width. 
ch = 400                                      # canvas height. 
canvas_1 = Canvas(root, width=cw, height=ch, background="#110055") 
canvas_1.grid(row=0, column=1) 

# For Display - Downconvert a 3D/4D matrix down to a 2D list. 
def fourd_shape_2_twod_line(numpy_threed_matrix,  kula, l_width): 
    """ Project a set of 3D vertices (homogeneous matrix - numpy form) onto a 2D plane. 
        Input arguments are a 3D shape, a color and a line width. 
        The x and y compnents are drawn as a segmented line or a polygon. 
    """ 
    bbb = numpy_threed_matrix.tolist() 
    twod_line = [] 
    for i in range(0, len(bbb)): 
        twod_line.append( bbb[i][0] ) 
        twod_line.append( bbb[i][1] ) 
    #canvas_1.create_line( twod_line, width = l_width,  tag = 'lines_1', fill= kula ) 
    canvas_1.create_polygon( twod_line, width = l_width,  tag = 'lines_1', fill= kula ) 
    return twod_line 


# Dynamic rotation. 
def show_shape(): 
    """  Demonstrate the 3D animated transformations of shapes composed of vertices. 
    """ 
    cycle_period= 30 
    rad_one_deg = math.pi/180.0 
    rad_angle = 0.0 

    for i in range(len(faces)): 
       for j in range(len(faces[i])): 
           faces[i][j] = faces[i][j] * matrix_transforms.T_scaling(100.1 , 100.1, 100.1) 

    # Animation by rotation around 3 axes. 
    for sequence in range (1000):  
        for i in range(len(faces)): 
            faces[i] = faces[i] * matrix_transforms.T_roty(-rad_angle) 
            faces[i] = faces[i] * matrix_transforms.T_rotx(rad_angle*0.7) 
            faces[i] = faces[i] * matrix_transforms.T_rotz(rad_angle*1.3) 
            view_faces = faces[i] * matrix_transforms.T_translate( 200.0,  200.0, 0.0) 
            fourd_shape_2_twod_line(view_faces ,  '#ff0044',  1)   
            
        rad_angle = rad_one_deg * 1.0 
        canvas_1.update()              # This refreshes the drawing on the canvas. 
        canvas_1.after(cycle_period)   # This makes execution pause for 200 milliseconds. 
        canvas_1.delete('lines_1') 

show_shape() 
root.mainloop()
