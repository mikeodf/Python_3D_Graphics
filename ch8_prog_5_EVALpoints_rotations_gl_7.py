"""   ch8 No.6  
Program name: EVALpoints_rotations_gl_7.py 
Objective: Draws a complex shape from a Python list of (x,y) coordinates using "eval". 

keywords: eval, points, liness, rotate, draw 
==============================================================================79 
From the book "Python Graphics for Games: Working in 3 Dimensions"

Comments: Convert a Python list of (x,y) coordinates into a glVertex3f(x,y,z) 
list of vertices. The OpenGL vertex statements are assembled for the Python 
list as strings of the form "glVertex3f(x,y,z)" and transformed into OpenGL 
statements using the eval() function. 

Author:          Mike Ohlson de Fine 
""" 
# To get this to work with python3.x 
#import sys 
#sys.path.append("/usr/local/lib/python2.7/dist-packages/PyOpenGL-3.1.0-py2.7.egg/")
from OpenGL.GL import * 
from OpenGL.GLUT import * 
from OpenGL.GLU import * 
import shape_sun_face_1     # This the file that contains the complex Pyton list of (x, y) coordinates.

vts = shape_sun_face_1.sun_shape                             # Short name for convenience. 

rot_angle = 0.0                                                            # Rotation angle for the quadrilateral. 

def InitGL(Width, Height):          
    """  A general OpenGL initialization function that sets the initial parameters. 
         It should be called immediately after our OpenGL window is created. 
    """ 
    glClearColor(0.0, 0.0, 0.0, 0.0)                                         # This clears the background color to black .
    glMatrixMode(GL_PROJECTION) 
    glLoadIdentity()                                                        # Reset the projection matrix. 
    gluPerspective(45.0, float(Width)/float(Height), 0.1, 100.0) 
    glMatrixMode(GL_MODELVIEW) 


def yield_vertex(string_vertex, i, j): 
    """ Assembles a "glVertex3f(x,y,z)" string then converts it to an OpenGL compatible 
        glVertex3f(x,y,z) statement. 
        Note that this function must not have an explicit 'return' statement. 
    """ 
    str_vt = 'glVertex3f(' 
    string_vert = str_vt + str(string_vertex[i][j]) +' , '+str(string_vertex[i][j+1]) +', -1.0 )'           
    eval(string_vert) 

def DrawCube(): 
  """ Assembles the correct vertex list for the " glBegin(GL_LINE_STRIP)" 
      sequence of vertices. 
  """ 
  glColor3f(1.0, 1.0, 0.0)  
  glLineWidth(3.0)    
  glBegin(GL_LINE_STRIP)                       # Start line.  
  for i in range(len(vts)): 
      for j in range(0, len(vts[i]), 2):       # Synthesize vertices from Python list. 
          yield_vertex(vts, i, j) 
  glEnd()                                      # End line.


def DrawGLScene(): 
    “”” The main drawing function.
    “””
    global rot_angle 
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);  # Clear screen depth buffer .
    glLoadIdentity(); 
    glTranslatef( -13.0, -13.0, -18.0) 
    glScale(0.06,  0.06,  0.06) 
    #glRotatef(30.0, 0.0, 0.0, 1.0);                  # Single rotation of the shape. 
    glRotatef(rot_angle*0.6, 1.0, 1.0, 0.0);          # Continuous animated rotation. 
    DrawCube() 
    rot_angle += 1.0                            # Increment of angle for continuous rotation. 
    glutSwapBuffers() 

def main(): 
  “”” Main event processing function.
  “””
  global window 
  glutInit(sys.argv) 
  glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH) 
  glutInitWindowSize(400, 400) 
  glutInitWindowPosition(0, 0)  
  window = glutCreateWindow("Python/OpengGL Rotate Complex Shapes") 
  glutDisplayFunc(DrawGLScene) 
  glutIdleFunc(DrawGLScene)                                     # When we are doing nothing, redraw the scene. 
  InitGL(400, 400)                                              # Initialize our window. 
  glutMainLoop()                                                # Start event processing. engine  

main() 
