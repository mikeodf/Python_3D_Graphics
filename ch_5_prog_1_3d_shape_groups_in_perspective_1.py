""" ch5 No.1 
Program name: 3d_shape_groups_in_perspective_1.py 
Objective: Create 3D perspective transform and display. 


Keywords: 3d projections, perspective, transforms, display. 
============================================================================79 
From the book "Python Graphics for Games: Working in 3 Dimensions"

Comments: This program uses the matrix_transformation module as an import. 
An array of planar strips is used to demonstrate the concept. 

Tested on: Python 2.6, Python 2.7.3, Python 3.2.3       
Author:  Mike Ohlson de Fine 
================================ 
""" 
from Tkinter import * 
#from tkinter import *   # Use this instead of the above for python version 3.x 
import math 
import copy 
import numpy as np 
import matrix_transforms 

root = Tk() 
root.title('Move any old shapes in perspective') 
cw = 800                                     # canvas width. 
ch = 800                                      # canvas height. 
canvas_1 = Canvas(root, width=cw, height=ch, background="#110011") 
canvas_1.grid(row=0, column=1) 
cycle_period= 30 
############################################################################### 
# Generate Planar Surface of Rectangular Strips. 
def stripface(n, x0, y0, z0, w, h): 
    """ Generate a planar set of n rectangular strips starting at x0, y0, z0 
        width w in the x direction, and length h in the y direction. 
    """ 
    x_new = x0 
    xy_strip_set = []     
    for i in range(n): 
        xy= [ [ x_new,   y0,   z0, 1.0 ],\
              [ x_new+w, y0,   z0, 1.0 ],\
              [ x_new+w, y0+h, z0, 1.0 ],\
              [ x_new,   y0+h, z0, 1.0 ] ] 
        xy_mat = np.matrix(xy)  
        xy_strip_set.append(xy_mat) 
        x_new += 2*w 
    return xy_strip_set 
#============================================================================ 
def display_matrix_object(numpy_threed_matrix,kula): 
    """ Convert a 3D homogeneous matrix (numpy form) to a list for a tkinter 'create_polygon'. 
    """ 
    bbb = numpy_threed_matrix.tolist() 
    twod_line = [] 
    for i in range(0, len(bbb)): 
        twod_line.append( bbb[i][0] ) 
        twod_line.append( bbb[i][1] ) 
    #canvas_1.create_line( twod_line, width = 1,  tag = 'lines_1', fill= kula ) 
    canvas_1.create_polygon( twod_line, width = 1,  tag = 'lines_1', fill= kula ) 
    return twod_line 

def scale_shift_3d_object(object_vertices,  scale_y, scale_z, x_shift, y_shift): 
    """  This places a 3D piece "object" at a convenient viewing position and at a 
         a convenient size. 
    """ 
    view_vertices = copy.deepcopy(object_vertices) 
    for h in range(len(view_vertices)): 
        for j in range(len(view_vertices[h])): 
            view_vertices[h][j] = view_vertices[h][j] * matrix_transforms.T_scaling(scale_x, scale_y, scale_z) 
            view_vertices[h][j] = view_vertices[h][j] * matrix_transforms.T_translate(x_shift, y_shift, 0.0)             
    return view_vertices 
#=============================================================================== 
# Initialization of variables and data. 
rad_ninety_deg = 90 * math.pi/180.0 
rad_one_deg = math.pi/180.0 
rad_angle = 0.0 

f = 8.0  # f is an analog of focal length for perspective projections. 

# A General Planar Strip in x-y plane, width w, height h 
x0 = 0.0 
y0 = 0.0 
z0 = 0.0 
w = 0.1 
h = 6.0 

# Locate the shape-set (for temporary display purposes only) at x_shift, y_shift. 
x_shift = 200.0 
y_shift = 100.0    
scale_x = 40.0 
scale_y = 40.0 
scale_z = 40.0 
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ 
# Create (instantiate) objects and position them. 
assemblage_A = stripface(30, x0, y0, z0, w, h) # Make an instance of the planar object. 
for h in range(len(assemblage_A)):       # Disposition and setup - Shift to a new location. 
            assemblage_A[h] = assemblage_A[h] * matrix_transforms.T_translate(2.2, 2.2, 0)  
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ 
# Dynamic (animated) rotation of the object). 

def transform_display(object_vertices, rad_angle, kula): 
        """ Transform and then Display. 
            There are two very distinct and separate operations here: 
            A) Rotate the object around the X, Y and Z axes. This alters the position of every vertex permanently. 
            B) Translate and scale each vertex temporarily for viewing. These operations are performed on a separate 
               copy of the rotated object. After each view the copy has no worth - it will be overwritten when the 
               next view is created. 
        """ 
        #1: Strips: Rotate Assemblage. Any other transforms may be applied to the vertices here. Their effect will be permanent. 
        #   For this example only rotation by a common angle is considered. 
        for h in range(len(object_vertices)):     
            object_vertices[h] = object_vertices[h] * matrix_transforms.T_rotx(rad_angle)   # Rotate around x.   
            object_vertices[h] = object_vertices[h] * matrix_transforms.T_roty(rad_angle)   # Rotate around y.   
            object_vertices[h] = object_vertices[h] * matrix_transforms.T_rotz(rad_angle)   # Rotate around z. 

        perspective_vertices = copy.deepcopy(object_vertices)  # Preserve the original and view an independent copy. 

        #2: Apply perspective transforms in Z directions - single-vanishing point perspective.   
        for h in range(len(object_vertices)):   
            for i in range(len(object_vertices[h])): 
               perspective_vertices[h][i] = perspective_vertices[h][i]*matrix_transforms.T_Z_perspective(perspective_vertices[h][i], f) 

        #3: Position and size the strip-grid for convenient viewing. 
        view_perspective_vertices = [] 
        for h in range(len(perspective_vertices)): 
           one_component = scale_shift_3d_object(perspective_vertices[h],  scale_y, scale_z, x_shift, y_shift)    
           view_perspective_vertices.append(one_component) 

        # 4: Display perspective projections.  
        for h in range(len(object_vertices)): 
            display_matrix_object(view_perspective_vertices[h], kula) 

for i in range (200): 
        transform_display(assemblage_A, rad_angle, "#880000") 
        rad_angle = rad_one_deg * 1.0 
        canvas_1.update()                    # This refreshes the drawing on the canvas. 
        canvas_1.after(cycle_period)   # This makes execution pause for 30 milliseconds, nominally. 
        canvas_1.delete('lines_1') 

root.mainloop()
