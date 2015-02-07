"""  ch10 No.3 
Program name: opengl_3D_visible_normals_1.py 
Objective: Construct normals at the centroid of each face. 
 
Keywords: OpenGL, triangle, normals, lighting. 
============================================================================79 
From the book "Python Graphics for Games: Working in 3 Dimensions"

Comments: Each triangle face has its normal drawn on it pointing in the 
positive direction. 

Tested on: Python 2.6, Python 2.7.3, Python 3.2.3       
Author:  Mike Ohlson de Fine 
================================ 
""" 
# To get this to work with python3.x 
#import sys 
#sys.path.append("/usr/local/lib/python2.7/dist-packages/PyOpenGL-3.1.0-py2.7.egg/")
from OpenGL.GL import * 
from OpenGL.GLUT import * 
from OpenGL.GLU import * 
import vector_2d3d_ops 

rotation_y = 0.0 
''' 
octet4tri =  [ 
-0.0, 0.7, 0.7,    -0.0, 1.0, 0.0,    -0.7, 0.7, 0.0,  # 1st triangle 
-0.7, 0.0, 0.7,    -0.0, 0.7, 0.7,    -0.7, 0.7, 0.0,  # 2nd triangle 
-0.0, 0.7, 0.7,    -0.7, 0.0, 0.7,    -0.0, 0.0, 1.0,  # 3rd triangle 
-1.0, 0.0, 0.0,    -0.7, 0.0, 0.7,    -0.7, 0.7, 0.0 ] # 4th triangle 
''' 
octet4tri =  [ 
-0.0, 0.7, 0.7,    -0.7, 0.7, 0.0,    -0.0, 1.0, 0.0,   # 1st triangle - sequence change. Reverses normal. 
-0.7, 0.0, 0.7,    -0.0, 0.7, 0.7,    -0.7, 0.7, 0.0,   # 2nd triangle 
-0.0, 0.7, 0.7,    -0.7, 0.0, 0.7,    -0.0, 0.0, 1.0,  # 3rd triangle 
-1.0, 0.0, 0.0,    -0.7, 0.0, 0.7,    -0.7, 0.7, 0.0 ] # 4th triangle 

#==================================================== 
octet4tri_vertices = len(octet4tri)/3  
print 'octet4tri_vertices: ', octet4tri_vertices 
octet4tri_norm = vector_2d3d_ops.array_triangle_normals(octet4tri) 

octet4tri_arrows = vector_2d3d_ops.centroid_normals(octet4tri, 0.05) 
octet4tri_arrows_vertices = len(octet4tri_arrows)/3 
print 'octet4tri_arrows_vertices: ', octet4tri_arrows_vertices 
octet4tri_arrows_norm = vector_2d3d_ops.array_triangle_normals(octet4tri_arrows) 
#======================================================== 
def InitGL(Width, Height): 
        """ Initialize and setup the Graphics Software/Hardware pipeline. 
        """ 
        # Note -  the value of the fourth parameter is immaterial for diffuse light. 
        diffuse_lite_kula_white   = [1.0, 1.0, 1.0, 0.0] 
        light0_position   = [  5.0, 1.0, 5.0, 0.0 ] 
        glClearColor(0.6, 0.6, 1.0, 0.0) 
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

def Octocapsule(): 
        """ A four triangle open surface with normal arrows.
        """ 
        global rotation_y 
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) 

        # Enable vertex arrays 
        glEnableClientState(GL_VERTEX_ARRAY)        
        glEnableClientState(GL_NORMAL_ARRAY) 
        
        # 1 first octant of Vertex arrays  
        glLoadIdentity() 
        glTranslatef(0.0,  -0.4,  -3.0) 
        glRotatef(rotation_y, 0.0, 1.0, 0.0)          
        glScale(1.0,  1.0,  1.0) 
        glColor3f(1.0, 0.0, 0.0)                     # Red              
        glVertexPointer(3, GL_FLOAT, 0, octet4tri)      # (size, type, stride, pointer) 
        glNormalPointer(GL_FLOAT, 0, octet4tri_norm)    # (type, stride, pointer). 
        glDrawArrays(GL_TRIANGLES, 0, 12)  # (primitive type, starting index, number of vertices to be rendered) 

        # Yellow visible normal arrows/spikes.
        glColor3f(1.0, 1.0, 0.0)  
        glVertexPointer(3, GL_FLOAT, 0, octet4tri_arrows)      # (size, type, stride, pointer) 
        glNormalPointer(GL_FLOAT, 0, octet4tri_arrows_norm)    # (type, stride, pointer). 
        glDrawArrays(GL_TRIANGLES, 0, 24)  # (primitive type, starting index, number of vertices to be rendered) 
          
        # Disable vertex arrays. 
        glDisableClientState(GL_VERTEX_ARRAY)       
        glDisableClientState(GL_NORMAL_ARRAY) 
        
        rotation_y += 0.02  # Slow rotation around the y-axis.
        glutSwapBuffers() 
        
        
def main(): 
        ''' Main Program. 
        '''    
        glutInit(sys.argv) 
        glutInitWindowSize(600,600)    # Width, Height. Line gets scaled to the window. 
        glutCreateWindow('OpenGL Vertex Arrays Triangles: Normals made visible') 
        InitGL(600, 600) 
        glutIdleFunc(Octocapsule)      # During idle time redraw the frame. 
        glutMainLoop() 

main()
