"""   ch8 No.1 
Program name: opengl_one_line_1.py 
Objective: Using openGL draw a single line which is specified by means of 
variables passed to a vertex 'glBegin/glEnd' set.  
 
Keywords: OpenGL, line, linewidth 
============================================================================79 
From the book "Python Graphics for Games: Working in 3 Dimensions"

Comments: glLineWidth(float width); 
Sets the width in pixels for rendered lines; width must be greater than 0.0
and by default is 1.0. 

Tested on:  Python 2.7.3, Python 3.2.3       
Author:  Mike Ohlson de Fine 
================================ 
""" 
# To get this to work with python3.x .  Also see Appendix:Solving the Broken Path Problem.
#import sys 
#sys.path.append("/usr/local/lib/python2.7/dist-packages/PyOpenGL-3.1.0-py2.7.egg/") 
from OpenGL.GL import * 
from OpenGL.GLUT import * 
from OpenGL.GLU import * 
window = 0 

x0 =  1.0    # Line start 
y0 =  1.0 
x1 = -1.0    # Line finish 
y1 =  1.0 

def InitGL(Width, Height): 
        """ Initialize and setup the Graphics Software/Hardware pipeline. 
        """ 
        glClearColor(0.0, 0.0, 0.0, 0.0) 
        glMatrixMode(GL_PROJECTION) 
        glLoadIdentity() 
        gluPerspective(45.0, float(Width)/float(Height), 0.1, 100.0) 
        glMatrixMode(GL_MODELVIEW) 

def any_line(x0,y0,x1,y1, kula): 
        """ Specification of the line position and color. 
        """      
        glBegin(GL_LINES) 
        glVertex3f(x0, y0,-1.0) 
        glVertex3f(x1, y1,-1.0) 
        glEnd() 

def DrawGLScene(): 
        """ Specification of the line position and color. 
        """      
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) 
        glLoadIdentity() 
        glTranslatef(0.0,0.0,-6.0) 
        glLineWidth(10.0) 
        any_line(x0,y0,x1,y1, glColor3f(1.0,1.0,0.0) ) # Our line to be drawn. 
        glutSwapBuffers() 
 
def main(): 
        """ Main Program. 
        """      
        glutInit(sys.argv) 
        glutInitWindowSize(300,80)           # Width,Height. The line gets scaled to the window. 
        glutInitWindowPosition(10,30)      # Controls where the window starts - top-left corner of screen. 
        window = glutCreateWindow('OpenGL-Python Line') 
        glutDisplayFunc(DrawGLScene)   # Drawing. 
        InitGL(5, 5)                                    # Starting position of window on computer screen (top-left corner). 
        glutMainLoop() 
 
main()
