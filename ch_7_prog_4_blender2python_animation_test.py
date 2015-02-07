"""   ch7 No.4 
Program name: blender2python_animation_test.py
Function names: 
a) fourd_shape_2_twod_line(numpy_threed_matrix,kula,l_width)
b)  show_shape(vertex_set)

Objective: Demonstrate and prove the blender.obj 3D object file into usable Python vertex and face lists is correct.

Keywords: blender, geometry, vertices, faces 
============================================================================79 
From the book "Python Graphics for Games: Working in 3 Dimensions"

Tested on: Python 2.7.3, Python 3.2.3 
Author:          Mike Ohlson de Fine 
""" 
#============================================
#  SHAPE TRANSFORM TESTING BY DRAWING 
# ============================================ 
''' The code below is just for quick visual confirmation that the data is good. 
''' 
from Tkinter import * 
#from tkinter import *   # Use this instead of the above for python version 3.x 
import math 
import matrix_transforms 
root = Tk() 
root.title("Show the current 3D triangles model.") 
cw = 600                                      # canvas width. 
ch = 600                                      # canvas height. 
canvas_1 = Canvas(root, width=cw, height=ch, background="#110011") 
canvas_1.grid(row=0, column=1) 


# For Display - Downconvert a 3D/4D matrix down to a 2D list. 
def fourd_shape_2_twod_line(numpy_threed_matrix,kula,l_width): 
    """ Convert a 3D homogeneous matrix (numpy form) to a list for 'create_line'. 
    """ 
    bbb = numpy_threed_matrix.tolist() 
    twod_line = [] 
    for i in range(0, len(bbb)): 
        twod_line.append( bbb[i][0] ) 
        twod_line.append( bbb[i][1] ) 
    canvas_1.create_line( twod_line, width = l_width,  tag = 'lines_1', fill= kula ) 
    #canvas_1.create_polygon( twod_line, width = l_width,  tag = 'lines_1', fill= kula ) 
    return twod_line 

# Dynamic rotation. 
def show_shape(vertex_set): 
    """  Demonstrate the 3D animated transformations of shapes composed of vertices and edges. 
    """ 
    cycle_period= 100 
    rad_one_deg = math.pi/180.0 
    rad_angle = 0.0 

    for i in range(len(faces_tk)): 
       for j in range(len(faces_tk[i])): 
           faces_tk[i][j] = faces_tk[i][j] * matrix_transforms.T_scaling(50 , 50, 50) 

    # Animation by rotation around 3 axes. 
    for i in range (500): 
        
        # Faces. 
        for i in range(len(faces_tk)): 
            faces_tk[i] = faces_tk[i] * matrix_transforms.T_roty(-rad_angle) 
            faces_tk[i] = faces_tk[i] * matrix_transforms.T_rotx(rad_angle*0.2) 
            faces_tk[i] = faces_tk[i] * matrix_transforms.T_rotz(rad_angle*1.3) 
            view_faces =faces_tk[i] * matrix_transforms.T_translate( 300.0,  300.0, 0.0) 
            fourd_shape_2_twod_line(view_faces , '#ffff00', 1)   
            
        rad_angle = rad_one_deg * 1.0 
        canvas_1.update()                    # This refreshes the drawing on the canvas. 
        canvas_1.after(cycle_period)   # This makes execution pause for 100 milliseconds. 
        canvas_1.delete('lines_1') 

show_shape(vertex_list) 
root.mainloop() 
