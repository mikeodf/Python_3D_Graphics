"""  ch14 No.3  
Program name: opengl_spot_lighting_1.py 
Objective: To demonstrate the effect of spotlight position settings. 

keywords: opengl, lighting, spot, spotlight, square, quads, quadrilateral. 
==============================================================================79 
From the book "Python Graphics for Games: Working in 3 Dimensions"

Comments: An exercise in spot lighting. 
Observe that the color of the spotlit area is dominated by the color of 
diffuse light on the tiles. 
Examples: 
1. If the tiles are colored green and then illuminated with red spotlight, 
 then the spotlight is invisible. A pure green tile is incapable of reflecting red light. 
2. If the tiles are colored yellow ( a mix of red and green) 
 and then illuminated with red spotlight, the spotlit ares is orange ( yellow with extra red). 

Tested on: Python 2.6, Python 2.7.3, Python 3.2.3       
Author:  Mike Ohlson de Fine 
""" 

from OpenGL.GL import * 
from OpenGL.GLUT import * 
from OpenGL.GLU import * 
import sys 

kula_spotlight     =  [ 1.0, 1.0, 0.0 ]  # Yellow 
kula_tiles =  [ 0.0, 1.0, 0.0 ]  # Red 
x_lite = 0.0            #x_lite = -4.0 
y_lite = 0.0 
z_lite = -10.0 
#  @@@@@@@@@  Spotlight alert !!!  @@@@@@@@@@@@@@@@@@@@@@@@@@@@ 
w_lite = 1.0   # NB!!! Positional: W =1.0 Directional: W = 0.0 
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

def InitGL(Width, Height):            # Set OpenGL up in the required state 
    light_position = [ x_lite, y_lite, z_lite, w_lite ] 
    glClearColor(0.0, 0.0, 0.0, 0.0)  # Set the background color to black .
    # ^^^^ Lighting and Materials ^^^^^^^^^^^^^^^^^^^^^^^^^^ 
    glEnable(GL_LIGHT0) 
    glEnable(GL_NORMALIZE) 
    glEnable(GL_COLOR_MATERIAL) 
    glEnable(GL_LIGHTING) 

    glLightfv(GL_LIGHT0, GL_POSITION, light_position) 
    glLightf(GL_LIGHT0, GL_SPOT_CUTOFF, 10.0) 
    glLightfv(GL_LIGHT0, GL_DIFFUSE,   kula_spotlight) 
    # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ 
    glShadeModel(GL_SMOOTH)          
    glMatrixMode(GL_PROJECTION) 
    glLoadIdentity()          
    gluPerspective(80.0, float(Width)/float(Height), 0.1, 100.0) # last 2: near, far 
    glMatrixMode(GL_MODELVIEW) 


def vert_quad_1(xx, yy, zz, x_width, y_hite, z_depth, kula): 
    """ Draw a VERTICAL BACK WALL (aligned with the X-axis), 
        quadrilateral in a variable position. 
        The shape and color parameters are supplied as arguments. 
    """ 
    glLoadIdentity() 
    glColor(kula[0], kula[1], kula[2] ) 
    glTranslatef(xx, yy, zz ) 
    glBegin(GL_QUADS) 
    glVertex3f( xx       ,  yy, zz) 
    glVertex3f(xx        ,  yy+y_hite, zz) 
    glVertex3f(xx+x_width,  yy+y_hite, zz) 
    glVertex3f(xx+x_width,  yy, zz) 
    glEnd() 

def horiz_quad_1(xx, yy, zz, x_width, y_hite, z_depth, kula): 
    """ Draw a HORIZONTAL (Ceiling and Floor) quadrilateral in a varaible position. 
        The shape and color parameters are supplied as arguments. 
    """ 
    glLoadIdentity() 
    glColor(kula[0], kula[1], kula[2] ) 
    glTranslatef(xx, yy, zz ) 
    glBegin(GL_QUADS) 
    glVertex3f( xx,        yy,  zz) 
    glVertex3f(xx,          yy, zz+z_depth) 
    glVertex3f(xx+x_width,  yy, zz+z_depth) 
    glVertex3f(xx+x_width,  yy, zz) 
    glEnd() 

def side_wall_1(xx, yy, zz, x_width, y_hite, z_depth, kula): 
    """ Draw a VERTICAL quadrilateral( aligned with the Z-axis), in a varaible position. 
        The shape and color parameters are supplied as arguments. 
    """ 
    glLoadIdentity() 
    glColor(kula[0], kula[1], kula[2] ) 
    glTranslatef(xx, yy, zz ) 
    glBegin(GL_QUADS) 
    glVertex3f( xx, yy,  zz) 
    glVertex3f(xx,  yy+y_hite, zz) 
    glVertex3f(xx,  yy+y_hite, zz+z_depth) 
    glVertex3f(xx,  yy       , zz+z_depth) 
    glEnd() 
    

def row_of_vert_quads(xx,yy,zz, x_incr, y_incr, z_incr):    
    for i in range(12): 
        vert_quad_1(xx, yy, zz, x_incr, y_incr, z_incr, kula_tiles) 
        xx = xx + x_incr 

def row_of_horiz_quads(xx,yy,zz, x_incr, y_incr, z_incr): 
    for i in range(12): 
        horiz_quad_1(xx, yy, zz, x_incr, y_incr, z_incr, kula_tiles) 
        xx = xx + x_incr 

def row_of_side_walls(xx,yy,zz, x_incr, y_incr, z_incr): 
    for i in range(12): 
        side_wall_1(xx, yy, zz, x_incr, y_incr, z_incr, kula_tiles) 
        zz = zz + z_incr 


# The main drawing function. 
def DrawGLScene(): 
    """ The main drawing function. 
    """ 
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  # Clear The Screen And The Depth Buffer 
   
    # Left Side_wall 
    xx = -5.0      # Starting position - where the tiling starts.          
    yy = 3.0 
    zz = -17.0 
    x_incr = 0.0  
    y_incr = 1.0 
    z_incr = 1.0     
    for i in range(7): 
        row_of_side_walls(xx,yy,zz, x_incr, y_incr, z_incr) 
        yy -= 1.0 
        zz = -17.0 

    # Right Side_wall 
    xx = 6.5 
    yy = 3.0 
    zz = -17.0 
    for i in range(7):    
        row_of_side_walls(xx,yy,zz, x_incr, y_incr, z_incr)   
        yy -= 1.0 

    # Horizontal Quads (Ceiling) 
    xx = -5.0 
    yy = 4.0 
    zz = -6.0 
    x_incr = 1.0 
    y_incr = 0.0   
    for i in range(12): 
        row_of_horiz_quads(xx,yy,zz, x_incr, y_incr, z_incr)      
        zz -= 1.0 

    # Horizontal Quads (Floor) 
    xx = -5.0 
    yy = -3.5 
    zz = -6.0     
    for i in range(12): 
        row_of_horiz_quads(xx,yy,zz, x_incr, y_incr, z_incr)     
        zz -= 1.0 

    # Vertical Quads (Back wall)  
    xx = -5.0 
    yy = 3.3 
    zz = -18.0 
    y_incr = 1.0 
    z_incr = 0.0     
    for i in range(8): 
        row_of_vert_quads(xx,yy,zz, x_incr, y_incr, z_incr)      
        yy -= 1.0 

    glutSwapBuffers() 

def main(): 
    glutInit(sys.argv) 
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)   
    glutInitWindowSize(1200, 800) 
    glutInitWindowPosition(0, 0)  
    window = glutCreateWindow("Spotlight. Red tiles, yrellow light") 
    glutDisplayFunc(DrawGLScene)  
    InitGL(1200, 800)                
    glutMainLoop()                 

main()
