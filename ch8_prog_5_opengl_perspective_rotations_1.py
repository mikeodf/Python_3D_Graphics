"""   ch8 No.5 
Program name: opengl_perspective_rotations_1.py 
Objective: Construct a general cube. Demonstrate independent rotation of multiple 
instances of the cubes. 

keywords: opengl, points, lines, variable cube, independent rotation 
==============================================================================79 
From the book "Python Graphics for Games: Working in 3 Dimensions"

Comments: A wire cube is defined interms of variables inside vertices. 

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
import sys 

x0 =  -1.0    # Line start .
y0 =  -1.0 
z0 =  1.0 
rangle = 0.0 

def InitGL(Width, Height):       
    """  initial parameters. This is called right after the OpenGL window is created. 
    """ 
    glClearColor(0.0, 0.0, 0.0, 0.0)  # Clear background to black .
    glMatrixMode(GL_PROJECTION) 
    glLoadIdentity()                         # Reset projection matrix.                   
    gluPerspective(45.0, float(Width)/float(Height), 0.1, 100.0) 
    glMatrixMode(GL_MODELVIEW) 

def any_cube(x0,y0,z0, hite): 
        """ Specification of the line and point positions and their color. 
        """ 
        glColor3f(1.0,0.0,0.0)   
        glLineWidth(8.0)           
        glBegin(GL_LINE_STRIP) 
        glVertex3f( x0     , y0      , z0)      # 1 
        glVertex3f( x0     , y0+hite , z0)      # 2    
        glVertex3f( x0+hite, y0+hite , z0)      # 3 
        glVertex3f( x0+hite, y0      , z0)      # 4 
        glVertex3f( x0     , y0      , z0)      # 1 
        glEnd() 
        
        glPointSize( 20.0) 
        glColor3f(1.0, 1.0, 0.0) 
        glBegin(GL_POINTS);            # Every vertex specified is a point. 
        glVertex3f( x0     , y0      , z0)  # 1 
        glEnd() 

        glPointSize( 12.0) 
        glColor3f(0.0, 1.0, 0.0) 
        glBegin(GL_POINTS);      
        glVertex3f( x0     , y0+hite , z0)     # 2    
        glVertex3f( x0+hite, y0+hite , z0)     # 3 
        glVertex3f( x0+hite, y0      , z0)     # 4 
        glEnd() 
        
        glLineWidth(2.0) 
        glColor3f(0.1,0.1, 1.0) 
        glBegin(GL_LINE_STRIP) 
        glVertex3f( x0         , y0      , z0-hite)     # 5 
        glVertex3f( x0         , y0+hite , z0-hite)     # 6    
        glVertex3f( x0+hite    , y0+hite , z0-hite)     # 7 
        glVertex3f( x0+hite    , y0      , z0-hite)     # 8 
        glVertex3f( x0         , y0      , z0-hite)     # 5 
        glEnd() 
        
        glColor3f(1.0,0.0,0.5) 
        glBegin(GL_LINES) 
        glVertex3f( x0, y0+hite,      z0)      # 2 
        glVertex3f( x0, y0+hite, z0-hite)      # 6  
        glEnd() 

        glBegin(GL_LINES) 
        glVertex3f( x0+hite, y0+hite, z0     )    # 3 
        glVertex3f( x0+hite, y0+hite, z0-hite)    # 7 
        glEnd() 

        glColor3f(0.5,0.0,1.0) 
        glBegin(GL_LINES) 
        glVertex3f( x0+hite, y0     , z0     )    # 4 
        glVertex3f( x0+hite, y0     , z0-hite)    # 8  
        glEnd() 

        glColor3f(1.0,1.0,0.0) 
        glBegin(GL_LINES) 
        glVertex3f( x0, y0  , z0     )     # 1 
        glVertex3f( x0, y0  , z0-hite)     # 5  
        glEnd() 
         
def DrawGLScene(): 
    """ Specification of the line and point positions and their color. 
    """ 
    global rangle 
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  # Clear screen and depth buffer. 
    size      = [ 1.0,  1.0,   1.0 ]                    # Change size if desired. 
    location  = [ 0.0,  0.0,  -5.0 ]   
    glLoadIdentity(); 
    glTranslatef(location[0], location[1], location[2]) # Shift to convenient position. 
    glScale(size[0],size[1],size[2])                    # Change size if desired. 
    glRotatef(rangle*0.4, 1.0, 0.0, 0.0);               # Rotate cube around X. 
    any_cube(-1.0,-1.0, 1.0, 2.0 )                      # Largest cube. 

    glLoadIdentity(); 
    glTranslatef(location[0], location[1], location[2]) # Shift to convenient position. 
    glScale(size[0],size[1],size[2])                    # Change size if desired. 
    glRotatef(rangle*0.4, 0.0, 1.0, 0.0);               # Rotate cube around X. 
    any_cube(-0.9,-0.9, 0.9, 1.8 )                      # Intermediate size cube. 

    glLoadIdentity(); 
    glTranslatef(location[0], location[1], location[2]) # Shift to convenient position. 
    glScale(size[0],size[1],size[2])                    # Change size if desired. 
    glRotatef(rangle*0.4, 0.0, 0.0, 1.0);               # Rotate cube around X.  
    any_cube(-0.8,-0.8, 0.8, 1.6 )                      # Smallest cube. 
    rangle += 1.0           
    glutSwapBuffers() 
#============================================================== 
def main(): 
    """ Specification of the line and point positions and their color. 
    """ 
    glutInit(sys.argv) 
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH) 
    glutInitWindowSize(1000, 1000) 
    glutInitWindowPosition(0, 0)  
    window = glutCreateWindow("Perspective: 45.0, float(Width)/float(Height), 0.1, 100.0") 
    glutDisplayFunc(DrawGLScene) 
    glutIdleFunc(DrawGLScene)  
    InitGL(1000, 1000)  
    glutMainLoop()  

main() 
