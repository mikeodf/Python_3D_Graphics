"""   ch9 No.5 
Program name: opengl_boxy_triangles_1.py 
Objective: Use variable parameters to define multiple objects. 

keywords: opengl, glut, triangles, boxes, color control 
==============================================================================79 
From the book "Python Graphics for Games: Working in 3 Dimensions"

Explanation: The idea is to be able pre-construct a shape like a box 
             and then be able to draw multiple instances each with their own 
             shape, position and rotation dynamics. 
Variable parameters rather than constants are used to populate vertex arrays. 
The names of the variables are used as OpenGL vertex arrays. 
That is, that are referenced by their Python list names. 
 This avoids the awkwardness and some of the speed performance penalty 
associated with the "glBegin ... glEnd" style of 3D object definition. 

Three different animation functions are available: 
1. glutIdleFunc(all_displays)     
2. glutDisplayFunc(all_displays)   
3. glutTimerFunc(1,update,0) calling "update" which calls "all_displays()". 

 
Tested on: Python 2.6, Python 2.7.3, Python 3.2.3 
Author:          Mike Ohlson de Fine 
""" 
# To get this to work with python3.x 
#import sys 
#sys.path.append("/usr/local/lib/python2.7/dist-packages/PyOpenGL-3.1.0-py2.7.egg/")
from OpenGL.GL import * 
from OpenGL.GLUT import * 
from OpenGL.GLU import * 

#======================================================================== 
# Individual object properties for each of three instances of the rectangular tube. 
# there are the effective "state" parameters of the 3D objects controlled by Python. 

rotate_angle_1 = 0.0 
rotate_angle_2 = 0.0 
rotate_angle_3 = 0.0 

rotation_speed_1 = 0.2 
rotation_speed_2 = 0.4 
rotation_speed_3 = 0.3 

rotation_axis_1 = [0.8, 0.3, 0.0] 
rotation_axis_2 = [0.3, 0.8, 0.0] 
rotation_axis_3 = [0.0, 0.5, 0.4] 

shift_1 = [0,    0,     -20 ] 
shift_2 = [0,    0,      -8 ] 
shift_3 = [-2,  0.5,     -12 ] 

origin_1 = [ -1, 1, 0 ] 
origin_2 = [  1, 1, 0 ] 
origin_3 = [  0, 0, 0 ] 

w_1, w_2, w_3 = 0.2,   1.5, 2 
h_1, h_2, h_3 = 0.2,   0.5, 1 
d_1, d_2, d_3 = 5.0,   0.1, 2 

kula = [ [ 0.0,  0.0,  0.4], 
             [ 0.0,  0.0,  0.6], 
             [ 0.0,  0.2,  0.3], 
             [ 0.0,  0.3,  0.6], 
             [ 0.0,  0.4,  0.0], 
             [ 0.0,  0.6,  0.0], 
             [ 0.3,  0.0,  0.0], 
             [ 0.6,  0.2,  0.0]       ] 
#====================================================================== 
def TriBox(org_x, org_y, org_z, width ,height ,depth ): 
    ''' Draw a square tube (open ended box) from triangles. 
        Arguments: origin (bottom left), given as tri1 and tri2. 
                    width(x-dirn.), height(y-dirn) and depth(z-dirn). 
    ''' 

    tr1 = [org_x, org_y, org_z,   org_x+width, org_y+height, org_z-depth ]   # Parameters 

    # vertex        1                            2                         3              
    #        ---------------------     --------------------     -----------------------      
    #        0         1       2         3      4       5         6        7       8      

    vt1 = [  tr1[0], tr1[1], tr1[2],  tr1[3], tr1[1], tr1[5],   tr1[0], tr1[1], tr1[5] ] 
    vt2 = [  tr1[0], tr1[1], tr1[2],  tr1[3], tr1[1], tr1[5],   tr1[3], tr1[1], tr1[2] ] 
    vt3 = [  tr1[3], tr1[1], tr1[2],  tr1[3], tr1[4], tr1[5],   tr1[3], tr1[1], tr1[5] ] 
    vt4 = [  tr1[3], tr1[1], tr1[2],  tr1[3], tr1[4], tr1[2],   tr1[3], tr1[4], tr1[5] ] 

    vt5 = [  tr1[3], tr1[4], tr1[2],  tr1[0], tr1[4], tr1[5],   tr1[3], tr1[4], tr1[5] ] 
    vt6 = [  tr1[3], tr1[4], tr1[2],  tr1[0], tr1[4], tr1[2],   tr1[0], tr1[4], tr1[5] ] 
    vt7 = [  tr1[0], tr1[4], tr1[2],  tr1[0], tr1[1], tr1[5],   tr1[0], tr1[4], tr1[5] ] 
    vt8 = [  tr1[0], tr1[4], tr1[2],  tr1[0], tr1[1], tr1[2],   tr1[0], tr1[1], tr1[5] ] 
  
    return vt1, vt2, vt3, vt4, vt5, vt6, vt7, vt8 

def InitGL(Width, Height): 
        """ Initialize and setup the state of Graphics Software/Hardware pipeline. 
        """ 
        diffuse_lite_kula_white   = [1.0, 1.0, 1.0, 0.0] 
        light0_position   = [  5.0, 1.0, 5.0, 0.0 ] 
        glClearColor(0.8, 0.8, 1.0, 0.0) 
        # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ 
        glEnable(GL_NORMALIZE) 
        glEnable(GL_COLOR_MATERIAL) 
        glEnable(GL_LIGHTING) 
        glEnable(GL_LIGHT0) 
        glLightfv(GL_LIGHT0, GL_POSITION, light0_position) 
        glLightfv(GL_LIGHT0, GL_DIFFUSE,   diffuse_lite_kula_white) 
        #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ 
        glEnable(GL_DEPTH_TEST) 
        glMatrixMode(GL_PROJECTION) 
        glLoadIdentity() 
        gluPerspective(45.0, float(Width)/float(Height), 0.1, 100.0) 
        glMatrixMode(GL_MODELVIEW) 

def all_displays(): 
    ''' This is the 'mothership' of the dynamic control of each instance of a shape ( box 
        in this example). It controls the global values of the rotation angles. 
        all_displays() calls display_n(...) passing individual properties to them 
        as arguments. 
    ''' 
    global rotate_angle_1, rotate_angle_2, rotate_angle_3 

    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT) # Clear the colour and depth buffer       
    glEnableClientState(GL_VERTEX_ARRAY); 
    display_n(rotation_axis_1, kula, shift_1, rotate_angle_1, origin_1, w_1, h_1, d_1) 
    display_n(rotation_axis_2, kula, shift_2, rotate_angle_2, origin_2, w_2, h_2, d_2) 
    display_n(rotation_axis_3, kula, shift_3, rotate_angle_3, origin_3, w_3, h_3, d_3) 
    
    glFlush() # Makes sure that we output the model to the graphics card 
    glutSwapBuffers() 
    glutPostRedisplay() 

    rotate_angle_1 += rotation_speed_1 
    rotate_angle_2 += rotation_speed_2 
    rotate_angle_3 += rotation_speed_3 

def display_n(rotation_axis, kula, shift, rotate_angle, origin, width, height, depth): 
    """ Draw the object "box" which is an instance of TriBox(...). 
        The shape and location of "box" are passed as variables to TriBox(...) 
        and are draw as openGL vertex arrays. 
    """ 
    glLoadIdentity()                                       # Clear the modelview matrix stack 
    glTranslatef(shift[0],shift[1],shift[2])               # Each object's seprate origin. 
    glRotate(rotate_angle, rotation_axis[0],  rotation_axis[1],  rotation_axis[2]) 

    box = TriBox(origin[0], origin[1], origin[2],  width, height, depth) # For each box 
    for i in range(0,len(box)): 
        glColor3f(kula[i][0], kula[i][1],  kula[i][2])                 
        glVertexPointer(3, GL_FLOAT, 0, box[i]) 
        glDrawArrays(GL_TRIANGLES, 0, 3) 

def update(a): 
    """ Animation frame rate control. 
        glutTimerFunc(frame-rate, update, 0). Frame-rate is in milliseconds. 
    """ 
    all_displays() 
    glutTimerFunc(2, update, 0) 

def main(): 
        ''' Main Program. 
        '''    
        glutInit(sys.argv) 
        glutInitWindowSize(600,600)    # Width, Height. Object gets scaled to the window. 
        glutCreateWindow('OpenGL Vertex Arrays: Triangulated rectangular tubes') 
        InitGL(600, 600) 
        glutIdleFunc(all_displays)      # 1. Method 1 - During idle time redraw the frame. 
        #glutDisplayFunc(all_displays)  # 2. Method 2
        #glutTimerFunc(1,update,0)      # 3. Method 3 - Control re-draw with timed interrups. 
        glutMainLoop() 

main()
