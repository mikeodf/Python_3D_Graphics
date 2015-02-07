"""  ch10 No.1  
Program name: opengl_starry3tri_vertex_arrays_1.py 
Objective: A general purpose program for inspecting 3D objects supplied as 
vertex arrays of triangles. 
 
Keywords: OpenGL, triangle, objects, world model, normals, lighting. 
============================================================================79 
From the book "Python Graphics for Games: Working in 3 Dimensions"

Comments: Demonstrate the futility of exporting unmodified Blender 
Wavefront.obj files. This illustrates the value of assembling 3D objects 
from of independent triangles. 

Tested on: Python 2.7.3, Python 3.2.3       
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
import math 

# The object to be displayed. 
starry3tri =  [ 
-1.0,  0.0,  0.5,     0.0, 1.1, 0.0,   1.0, 0.0, -0.5,   # 1st triangle 
-1.0,  0.0, -0.5,     0.0, 1.1, 0.0,   1.0, 0.0,  0.5,   # 2nd triangle 
 0.0,  0.0, -1.0,     0.0, 0.0, 1.0,   0.0, 1.0,  0.0  ] # 3rd triangle 

# Display rotation axis. 
rotate_y = 0.0 
rotate_x = 0.0 
#==================================================== 
# The Objects in the world - given by their vertex and normal arrays. 
starry3tri_vertices = len(starry3tri)/3  
print 'starry3tri_vertices : ', starry3tri_ vertices
starry3tri_norm = vector_2d3d_ops.array_triangle_normals(starry3tri) 
#============================================================== 

def InitGL(Width, Height): 
        """ Initialize and setup the Graphics Software/Hardware pipeline. 
        """  
        glClearColor(0.8, 0.8, 0.0, 0.0) 
        # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ 
        diffuse_lite_kula_white   = [  1.0, 1.0, 1.0, 0.0 ] 
        light0_position           = [ -5.0, 1.0, 5.0, 0.0 ] 
        # The 6 lines below create the lighting in the scene 
        glEnable(GL_NORMALIZE) 
        glEnable(GL_COLOR_MATERIAL) 
        glEnable(GL_LIGHTING) 
        glEnable(GL_LIGHT0)   # Create a light named "GL_LIGHT0" 
        glLightfv(GL_LIGHT0, GL_POSITION, light0_position) 
        glLightfv(GL_LIGHT0, GL_DIFFUSE,   diffuse_lite_kula_white) 
        #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ 
        glEnable(GL_DEPTH_TEST) 
        glMatrixMode(GL_PROJECTION) 
        glLoadIdentity() 
        gluPerspective(45.0, float(Width)/float(Height), 0.1, 100.0) 
        glMatrixMode(GL_MODELVIEW) 

def DrawObject(): 
        """ All the objects to be drawn should be in this function. 
                As far as possible there should be OpenGL instructions exclusively. 
                Any calls to Python functions will slow rendering significantly. 
            References to the names of vertex and normal arrays do not incur much of a penalty 
        """ 
        global rotate_x, rotate_y 
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) 

        # Control of World Coordinates - the following 3 instructions. 
        glLoadIdentity() 
        glTranslatef(0.0,-0.6,-6.0)  
        glRotatef(rotate_y, 0.0, 1.0, 0.0) 
        glRotatef(rotate_x, 1.0, 0.0, 0.0) 

        # Turn-on the vertex array processing   
        glEnableClientState(GL_VERTEX_ARRAY)     
        glEnableClientState(GL_NORMAL_ARRAY)  

        # Display of 3D object: starry3tri 
        glScale(2.0,  2.0,  2.0) 
        glColor3f(0.6, 0.6, 1.0)                       # Blue             
        glVertexPointer(3, GL_FLOAT, 0, starry3tri)            #Arguments:  (size, type, stride, pointer) .
        glNormalPointer(GL_FLOAT, 0, starry3tri_norm)    #Arguments:  (type, stride, pointer). 
        #glNormalPointer(GL_FLOAT, 0, starry3tri)    # Try this for blended shading.
        glDrawArrays(GL_TRIANGLES, 0, 3)  # Arguments: (primitive type, starting index, number of vertices to be rendered) 
        
        # Turn-off the Vertex Array processing.  
        glDisableClientState(GL_VERTEX_ARRAY)        
        glDisableClientState(GL_NORMAL_ARRAY)        
               
        rotate_y -= 0.05       # Rotation of the model world for display purposes. 
        rotate_x += 0.005   
        glutSwapBuffers() 
        

def main(): 
        ''' Main Program. 
        '''    
        glutInit(sys.argv) 
        glutInitWindowSize(400,400)    # Width,Height. The object gets scaled to the window. 
        glutCreateWindow('Draw any object: OpenGL Vertices vertex Arrays') 
        InitGL(400, 400) 
        glutIdleFunc(DrawObject)         # Prepare the next frame during CPU idle time. 
        glutMainLoop() 

main() 
