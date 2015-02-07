"""   ch9 No.3  
Program name: glut_timer_animation_wireshapes_1.py 
Objective: Demonstrate animation frame-rate control. 

keywords: opengl, animation, sphere, dodecahedron, extrusion shapes. 
==============================================================================79 
From the book "Python Graphics for Games: Working in 3 Dimensions"

Comments:  "glutTimerFunc registers a timer callback to be triggered in a 
specified number of milliseconds." GLUT attempts to deliver the timer callback 
as soon as possible after the expiration of the callback's time interval. 
Parameters (msec, callback, data): 
 - msec Milliseconds till invocation. 
 - callback Client function for timer event. 
 - data Arbitrary data; passed to callback .  

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

# Rotation angle for the shapes. 
rotation_angle = 0.0 
rotation_axis = [1.0, 1.0, 0.0 ] 
# Location of the shapes. 
location_sphere = [-20.0, 0.0, -110.0] 
location_dodec = [3.0, 0.0, -3.0] 

# A general OpenGL initialization function.  Sets all of the initial parameters. 
def InitGL(Width, Height):                      # Initialize our OpenGL window. 
    glClearColor(0.0, 0.0, 0.0, 0.0)            # Set The Background To Black  
    glMatrixMode(GL_PROJECTION) 
    glLoadIdentity()                           # Reset The Projection Matrix. 
    gluPerspective(45.0, float(Width)/float(Height), 0.1, 100.0)  # Calculate Aspect Ratio. 
    glMatrixMode(GL_MODELVIEW) 

# The main drawing function. 
def DrawGLScene(): 
  """ The pure drawing function - no animation control here. 
  """ 
  global rotation_angle  # Angular rotation 
  global location_sphere, location_dodec 
  glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);  
  rot_axis = [ 0.0, 1.0, 1.0 ] 

  # Draw sphere. 
  glLoadIdentity(); 
  glColor3f(0.0, 0.0, 0.7) 
  glTranslatef(location_sphere[0], location_sphere[1], location_sphere[2]) 
  glRotatef(rotation_angle , rotation_axis[0], rotation_axis[1], rotation_axis[2] ) 
  glutWireSphere(5.0, 8, 8) # (radius, slices, stacks) 
  
  # Draw dodecahedron 
  glLoadIdentity(); 
  glColor3f(1.0, 0.0, 0.7) 
  glTranslatef(location_dodec[0], location_dodec[1], location_dodec[2]) 
  glRotatef(rotation_angle , rotation_axis[0], rotation_axis[1], rotation_axis[2] )  
  glutWireDodecahedron() 

  glutSwapBuffers() 

def Freshframe(a): 
    """ Interrupt driven animation control. 
        This function does 3 things: 
           1. Sets a start/callback time for itself 20 millisec in the future. 
           2. Increments/decrements the position variables of the objects. 
           3. executes the opengl 'draw objects' function. 
    """ 
    global rotation_angle, location_sphere, location_dodec 
    rotation_angle += 0.5 
    location_sphere[0] += 0.008 
    location_sphere[2] += 0.03 
    location_dodec[0]  -= 0.001 
    location_dodec[2]  -= 0.01 
    DrawGLScene() 
    glutTimerFunc(20,Freshframe,0)  # After 20 milliseconds "Freshframe" is called. 
  
def main(): 
  glutInit(sys.argv)# initialization openGL window. Must be first GLUT function called. 
  glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)   # Display mode 
  glutInitWindowSize(800, 800) 
  window = glutCreateWindow("GLUT Animated Wireshapes") 
  glutTimerFunc(1, Freshframe, 0) # The initial time delay need only be token. 
  InitGL(800, 800)                          # Call our custom initialization function. 
  glutMainLoop()                            # Start GLUT's Event Processing Engine  
 

main()
