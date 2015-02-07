"""  ch14 No.1 
Program name: opengl_3D_compact_shield_1.py 
Objective: Construct an enclosed solid from an 11.25 degree strip 
using symmetry. 
 
Keywords: OpenGL, triangle, hemi-sphere, strip, separate, normals, lighting. 
============================================================================79 
From the book "Python Graphics for Games: Working in 3 Dimensions"

Comments: Each 32nd angular portion is derived from the same vertex array 
and is positioned,scaled and rotated in a single Python loop. 

Tested on: Python 2.6, Python 2.7.3, Python 3.2.3       
Author:  Mike Ohlson de Fine 
================================ 
""" 
from OpenGL.GL import * 
from OpenGL.GLUT import * 
from OpenGL.GLU import * 

rotation_y = 0.0 
rotation_x = 0.0 

# Hemisphere object 
hemi_strip =     [ 
 0.0031, 0.9522, 0.2684,   -0.1051, 0.8312, 0.5407,  -0.0499,   0.9522,  0.2632, 
-0.1051, 0.8311,0.54073,    0.0031, 0.9522, 0.2684,   0.0031,   0.8312,  0.5514, 
 0.0031, 0.8312, 0.5514,   -0.1475, 0.6358, 0.754,    -0.1051,  0.8312,  0.5407, 
 0.0031, 0.3846, 0.9136,   -0.1757, 0.3846, 0.8959,   -0.1475,  0.6358,    0.754, 
-0.1475, 0.6358,  0.754,    0.0031, 0.8314, 0.5514,    0.0031,  0.6358,  0.7688, 
-0.1475, 0.6358,  0.754,    0.0031, 0.6358, 0.7688,    0.0031,  0.3846,  0.9136, 
 0.0031, 0.3846, 0.9136,   -0.1951,    0.0, 0.9808,   -0.1757,  0.3846,    0.896, 
   -0.0,    0.0,    1.0,   -0.1951,    0.0, 0.9808,    0.0031,  0.3846,   0.9136 ] 

# Object color strips 
kula_1 = [ 
[1.0 , 0.0, 0.0], [1.0 , 0.0, 0.0], # red 
[1.0 , 1.0, 0.0], [1.0 , 1.0, 0.0], # yellow 
[0.0 , 1.0, 0.0], [0.0 , 1.0, 0.0], # green 
[0.0 , 1.0, 1.0], [0.0 , 1.0, 1.0], # lilac 
[0.0 , 0.0, 1.0], [0.0 , 0.0, 1.0], # blue 
[1.0 , 0.0, 1.0], [1.0 , 0.0, 1.0], # purple 
[1.0 , 1.0, 1.0], [1.0 , 1.0, 1.0], # white 
[0.0 , 0.0, 0.0], [0.0 , 0.0, 0.0], # black 
[1.0 , 0.0, 0.0], [1.0 , 0.0, 0.0], # red 
[1.0 , 1.0, 0.0], [1.0 , 1.0, 0.0], # yellow 
[0.0 , 1.0, 0.0], [0.0 , 1.0, 0.0], # green 
[0.0 , 1.0, 1.0], [0.0 , 1.0, 1.0], # lilac 
[0.0 , 0.0, 1.0], [0.0 , 0.0, 1.0], # blue 
[1.0 , 0.0, 1.0], [1.0 , 0.0, 1.0], # purple 
[1.0 , 1.0, 1.0], [1.0 , 1.0, 1.0], # white 
[0.0 , 0.0, 0.0], [0.0 , 0.0, 0.0]] # black 

#========================================================
hemi_strip_faces = len(hemi_strip)/3  
print 'hemi_strip_faces: ', hemi_strip_faces 
#======================================================== 
def InitGL(Width, Height): 
        """ Initialize and setup the Graphics Software/Hardware pipeline. 
        """ 
        # Experimental colors and light position. 
        diffuse_lite_kula   = [ 1.0, 1.0, 1.0, 0.0 ] 
        light0_position     = [-1.0, 3.0, 1.0, 0.0 ] 
        emissive_kula       = [ 0.0, 0.0, 0.0, 0.0 ] 
        # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ 
        glEnable(GL_NORMALIZE) 
        glEnable(GL_COLOR_MATERIAL 
        glEnable(GL_LIGHTING) 

        glEnable(GL_LIGHT0) 
        glLightfv(GL_LIGHT0, GL_POSITION, light0_position) 
        glLightfv(GL_LIGHT0, GL_DIFFUSE,   diffuse_lite_kula) 
        #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ 
        glEnable(GL_DEPTH_TEST) 
        glMatrixMode(GL_PROJECTION) 
        glLoadIdentity() 
        gluPerspective(45.0, float(Width)/float(Height), 0.1, 100.0) 
        glMatrixMode(GL_MODELVIEW) 

def draw32segments(seg_angle, kula): 
      """ Generate hemisphere from the vertical strip object hemi_strip. 
      """ 
      for i in range(32): 
        glLoadIdentity() 
        glTranslatef(0.0,  0.0,  -4.0) 
        glRotatef(90.0, 1.0, 0.0, 0.0)  
        glRotatef(rotation_x, 0.0, 0.0, 1.0)   
        glRotatef(i*seg_angle, 0.0, 1.0, 0.0) 
        glScale(1.0,  1.0,  1.0) 
        glColor3f(kula[i][0], kula[i][1], kula[i][2])                                
        glVertexPointer(3, GL_FLOAT, 0, hemi_strip)        # (size, type, stride, pointer) .
        glNormalPointer(GL_FLOAT, 0, hemi_strip)          # (type, stride, pointer) - smoothed normals. 
        glDrawArrays(GL_TRIANGLES, 0, 24)  # (primitive, start index, number of indices. 

def Octocapsule(): 
        """ Draw an enclose eight segmented solid by suitably rotating the 
            same segment into position using matrix operations. 
        """ 
        global rotation_x 
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)       
        glEnableClientState(GL_VERTEX_ARRAY)   # Enable vertex arrays     
        glEnableClientState(GL_NORMAL_ARRAY)        
        draw32segments(11.25, kula_1)   # 11.25 is the angular width of the strip. 
        rotation_x += 0.1  
        glutSwapBuffers() 


def main(): 
        ''' Main Program. 
        '''    
        glutInit(sys.argv) 
        glutInitWindowSize(600,600)    # Width, Height. Line gets scaled to the window. 
        glutCreateWindow('OpenGL Lighting: Emissive color = black') 
        InitGL(600, 600) 
        glutIdleFunc(Octocapsule)      # During idle time redraw the frame. 
        glutDisplayFunc(Octocapsule) 
        glutMainLoop() 

main() 
