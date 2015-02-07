"""   ch8 No.3  
Program name: opengl_wirecube_1.py 
Objective: Simplified Example. 

keywords: opengl, wirecube 
============================================================================79 
From the book "Python Graphics for Games: Working in 3 Dimensions"

Tested on:  Python 2.7.3, Python 3.2.3       
Author:  Mike Ohlson de Fine 
================================ 
""" 
# To get this to work with python3.x 
#import sys 
#sys.path.append("/usr/local/lib/python2.7/dist-packages/PyOpenGL-3.1.0-py2.7.egg/")
from OpenGL.GL import * 
from OpenGL.GLUT import * 

def init(): 
   glClearColor(1.0, 1.0, 1.0, 0) 
   glLoadIdentity() 
   

def display_1(): 
   glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) 
   glColor3f(1.0, 0.0, 0.0) 
   glutWireCube(1.0) 
   glFlush() 

glutInit('') 
glutInitWindowSize(300, 300) 
glutCreateWindow('Wire Cube') 
glutDisplayFunc(display_1) 
init() 
glutMainLoop()
