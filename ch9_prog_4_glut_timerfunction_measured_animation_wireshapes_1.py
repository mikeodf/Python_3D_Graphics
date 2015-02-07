"""   ch9 No.4 
Program name: glut_timerfunction_measured_animation_wireshapes_1.py 
Objective: Measure graphics frame-rate for glutIdleFunc or the glutTimerFunc. 

keywords: opengl, animation, framerate, time measure, sphere, dodecahedron. 
==============================================================================79 
From the book "Python Graphics for Games: Working in 3 Dimensions"

Comments: The glutGet(GLUT_ELAPSED_TIME) gives the millisecond count since 
the very first time it was called. Thus the difference between the last time 
and the time before that provide a measure of the intervening time.

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
location_sphere = [-20.0, 0.0, -105.0] 
location_dodec = [3.0, 0.0, -3.0] 
frame_count = 0 
start_time = 0 


# A general OpenGL initialization function.  Sets all of the initial parameters. 
def InitGL(Width, Height):                  # Initialize our OpenGL window. 
    global start_time 
    glLineWidth(20.0)
    glClearColor(0.2, 0.4, 0.0, 0.0)        # Set The Background To Green  
    glMatrixMode(GL_PROJECTION) 
    glLoadIdentity()                        # Reset The Projection Matrix. 
    gluPerspective(45.0, float(Width)/float(Height), 0.1, 100.0) 
    glMatrixMode(GL_MODELVIEW) 
    start_time = glutGet(GLUT_ELAPSED_TIME) 

# The main drawing function. 
def DrawGLScene(): 
  """ The pure drawing function - no animation control here. 
  """ 
  global rotation_angle, frame_count, start_time  # Angular rotation 
  global location_sphere, location_dodec 
  glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);  
  rot_axis = [ 0.0, 1.0, 1.0 ] 

  # Draw sphere. 
  glLoadIdentity(); 
  glColor3f(0.8, 0.8, 0.0) 
  glTranslatef(location_sphere[0], location_sphere[1], location_sphere[2]) 
  glRotatef(rotation_angle , rotation_axis[0], rotation_axis[1], rotation_axis[2] ) 
  glutWireSphere(10.0, 8, 8) # (radius, slices, stacks) 
  
  # Draw dodecahedron 
  glLoadIdentity(); 
  glColor3f(0.4, 0.0, 0.8) 
  glTranslatef(location_dodec[0], location_dodec[1], location_dodec[2]) 
  glRotatef(rotation_angle , rotation_axis[0], rotation_axis[1], rotation_axis[2] )  
  glutWireDodecahedron() 

  glutSwapBuffers() 

  # Advance the variables. 
  rotation_angle += 0.5 
  location_sphere[0] += 0.008 
  location_sphere[2] += 0.03 
  location_dodec[0]  -= 0.001 
  location_dodec[2]  -= 0.01 
  frame_count += 1 
  if frame_count >= 1000: # Get fps averaged over 1000 frames. 
       frame_count = 0 
       end_time = glutGet(GLUT_ELAPSED_TIME) 
       time_interval = end_time - start_time 
       start_time = end_time 
       fps = time_interval/1000.0    # Frames per second. 
       print 'fps: ', fps, '  time_interval (millisec): ' , time_interval   
       # Typical answer: "fps"  16.632   time_interval:  16632" 


def Freshframe(a):             # One argment is demanded by the system. 
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
    glutTimerFunc(1,Freshframe,0)  # After 20 milliseconds "Freshframe" is called. 

def main(): 
  glutInit()                                   # Must be first GLUT function called. 
  glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)   # Display mode 
  glutInitWindowSize(600, 600) 
  window = glutCreateWindow("GLUT Animated Wireshapes") 
  #glutIdleFunc(DrawGLScene) 
  glutTimerFunc(30, Freshframe, 0) # The initial time delay need only be small token. 
  InitGL(600, 600)                            # Call our custom initialization function. 
  glutMainLoop()                              # Start GLUT's Event Processing Engine  

main()
