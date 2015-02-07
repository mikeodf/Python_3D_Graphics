""" ch5 No.1 
Code name: strip_face.py 
Objective: Rectangular Strips. 


Keywords: 3d projections, perspective, transforms, display. 
============================================================================79 
From the book "Python Graphics for Games: Working in 3 Dimensions"

Comments: This code constructs an a aray of strips used with 3d_shape_groups_in_perspective_1.py, to demonstrate a perspective transformation.

Tested on: Python 2.6, Python 2.7.3, Python 3.2.3       
Author:  Mike Ohlson de Fine 
================================ 
""" 
def stripface(n, x0, y0, z0, w, h): 
    """ Generate a planar set of n rectangular strips starting at x0, y0, z0 
        width w in the x direction, and length h in the y direction. 
    """ 
    # Rectangular strips in the x-y plane. 
    x_new = x0 
    xy_strip_set = []     
    for i in range(n): 
        xy= [ [ x_new,   y0,   z0, 1.0 ],  [ x_new+w, y0,   z0, 1.0 ], [ x_new+w, y0+h, z0, 1.0 ], [ x_new,   y0+h, z0, 1.0 ] ] 
        xy_mat = np.matrix(xy)  
        xy_strip_set.append(xy_mat) 
        x_new += 2*w 
    # Rectangular strips in the x-z plane.   
    x_new = x0 
    xz_strip_set = []  
    for i in range(n): 
        xz= [ [ x_new,   y0,   z0, 1.0 ],  [ x_new+w, y0,   z0, 1.0 ], [ x_new+w, y0, z0+h, 1.0 ], [ x_new,   y0, z0+h, 1.0 ] ] 
        xz_mat = np.matrix(xz)  
        xz_strip_set.append(xz_mat) 
        x_new += 2*w 
    # Rectangular strips in the z-y plane. 
    y_new = y0 
    yz_strip_set = [] 
    for i in range(n): 
        yz= [ [ x0,   y_new,   z0, 1.0 ],  [ x0, y_new+w,   z0, 1.0 ], [ x0, y_new+w, z0+h, 1.0 ], [ x0,   y_new, z0+h, 1.0 ] ] 
        yz_mat = np.matrix(yz)  
        yz_strip_set.append(yz_mat) 
        y_new += 2*w 

    return xy_strip_set, xz_strip_set, yz_strip_set 

# Create (instantiate) objects and position them. 
# The instructions to create and position the three instances are:
xyz_strip_sets = stripface(30, x0, y0, z0, w, h) 
assemblage_A = xyz_strip_sets[0] 
assemblage_B = xyz_strip_sets[1] 
assemblage_C = xyz_strip_sets[2] 

for h in range(len(assemblage_A)):       # Disposition and setup - Shift to a new location. 
            assemblage_A[h] = assemblage_A[h] * matrix_transforms.T_translate(2.2, 2.2, 0) 
            assemblage_B[h] = assemblage_B[h] * matrix_transforms.T_translate(2.2, 2.2, 0)  
            assemblage_C[h] = assemblage_C[h] * matrix_transforms.T_translate(2.2, 2.2, 0)  

# The Final execution loop is:
# Main execution. 
for i in range (200): 
        transform_display(assemblage_A, rad_angle, "#880000") 
        transform_display(assemblage_B, rad_angle, "#008800") 
        transform_display(assemblage_C, rad_angle, "#000088") 
        rad_angle = rad_one_deg * 1.0 
        canvas_1.update()                    # This refreshes the drawing on the canvas. 
        canvas_1.after(cycle_period)   # This makes execution pause for 200 milliseconds. 
        canvas_1.delete('lines_1') 

root.mainloop() 
