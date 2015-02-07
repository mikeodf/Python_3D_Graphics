""" ch8 No.4  
Program name: glut_wireshapes_1.py 
Objective: Draw all the GLUT predefined shapes. 

keywords: opengl, cube, hexagon, teapot, cone, platonics, extrusion shapes. 
==============================================================================79 
From the book "Python Graphics for Games: Working in 3 Dimensions"

Tested on: Python 2.6, Python 2.7.3, Python 3.2.3       
Author:  Mike Ohlson de Fine 
===============================
"""


# To get this to work with python3.x 
#import sys 
#sys.path.append("/usr/local/lib/python2.7/dist-packages/PyOpenGL-3.1.0-py2.7.egg/")
from OpenGL.GL import * 
from OpenGL.GLUT import * 
from OpenGL.GLU import * 

# Rotation angle for the shapes. 
rangle = 0.0 
rot_axis = [1.0, 1.0, 0.0 ] 

 
def InitGL(Width, Height):                    
    """ Initialize our OpenGL window. Sets all of the initial parameters. 
    """ 
    glClearColor(0.0, 0.0, 0.0, 0.0)             # Set the background to black  
    glMatrixMode(GL_PROJECTION) 
    glLoadIdentity()                                             
    gluPerspective(45.0, float(Width)/float(Height), 0.1, 100.0)  # Aspect ratio. 
    glMatrixMode(GL_MODELVIEW) 
#===================================================================== 
# Variable position variables. 
location_1 = [2.0, -3.0, -5.0] 
location_2 = [-1.0, 0.0, -1.0] 
location_3 = [4.0, 0.0, -4.0] 
location_4 = [-2.0, 0.0, -2.0] 

def DrawGLScene(): 
  """ The drawing function 
  """ 
  global rangle  # Angular rotation 
  global location_1, location_2, location_3, location_4 
  glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);  # Clear The Screen And The Depth Buffer. 
  rot_axis = [ 0.0, 1.0, 1.0 ] 
 
  # Draw a cube, Icosahedron and torus 
  glLoadIdentity(); 
  location_1[1] += 0.001 
  location_1[2] -=0.05 
  glTranslatef(location_1[0], location_1[1], location_1[2]) 
  glRotatef(rangle , rot_axis[0], rot_axis[1], rot_axis[2] )  
  glutWireCube(2.5) 
  glutWireIcosahedron() 
  glutWireTorus(0.4, 4.4, 12, 8) 
  
  # Draw octahedron and sphere. 
  glLoadIdentity(); 
  location_2[0] += 0.01 
  location_2[2] -= 0.03 
  glTranslatef(location_2[0], location_2[1], location_2[2]) 
  glRotatef(rangle , rot_axis[0], rot_axis[1], rot_axis[2] ) 
  glutWireOctahedron() 
  glutWireSphere(2.0, 4, 3) 
 
  # Draw cone and dodecahedron 
  glLoadIdentity(); 
  location_3[0] -= 0.001 
  location_3[2] -= 0.01 
  glTranslatef(location_3[0], location_3[1], location_3[2]) 
  glRotatef(rangle , rot_axis[0], rot_axis[1], rot_axis[2] )  
  glutWireCone(2.5, 2.0, 6, 6) 
  glutWireDodecahedron() 

  # Draw Teapot 
  glLoadIdentity(); 
  location_4[0] += 0.05 
  location_4[2] -= 0.5 
  glTranslatef(location_4[0], location_4[1], location_4[2]) 
  glRotatef(rangle , rot_axis[0], rot_axis[1], rot_axis[2] ) 
  glutWireTeapot(1.5) 

  rangle += 0.5 
  glutSwapBuffers() 

def main(): 
  """ Main Program. 
  """     
  glutInit(sys.argv) # initialization openGL window. Must be first GLUT function called. 
  glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)   # Display mode 
  glutInitWindowSize(800, 800) 
  glutInitWindowPosition(0, 0)  
  window = glutCreateWindow("GLUT Wireshapes") 
  glutDisplayFunc(DrawGLScene) 
  glutIdleFunc(DrawGLScene)  # When we are doing nothing, redraw the scene. No animation without this. 
  InitGL(800, 800)                # Call our custom initialization function. 
  glutMainLoop()                  # Start GLUT's Event Processing Engine  

main()
