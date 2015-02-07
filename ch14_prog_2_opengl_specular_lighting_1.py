"""  ch14 No.2  
Program name: opengl_specular_lighting_1.py 
Objective: Experiment with the dynamic movement of specular lights. 

keywords: opengl, lighting, specualar, source rotation.. 
==============================================================================79 
From the book "Python Graphics for Games: Working in 3 Dimensions"

Comments: An exercise in lighting and materials. 

Tested on: Python 2.6, Python 2.7.3, Python 3.2.3       
Author:  Mike Ohlson de Fine 
""" 
from OpenGL.GL import * 
from OpenGL.GLUT import * 
from OpenGL.GLU import * 

# Lighting Parmeters 
position_light_0    = [ 2.0, 5.0, 5.0, 0.0 ] 
position_light_1    = [ 2.0, -5.0, 5.0, 0.0 ] 

light_specular_red  = [ 1.0, 0.0, 0.0, 1.0 ] 
light_specular_blue = [ 0.0, 0.0, 1.0, 1.0 ] 
material_specular   = [ 1.0, 1.0, 1.0, 1.0 ] 
high_shininess = [ 128.0 ]                   # Highest value. 

def InitGL(Width, Height):             # Set OpenGL up in the required state .
    glClearColor(0.0, 0.0, 0.0, 0.0)   # Background color To black .
    glClearDepth(1.0)                       # Clear the Depth buffer .
    glDepthFunc(GL_LESS)            # Type of Depth test to be applied. 
    glEnable(GL_DEPTH_TEST)    # Enables depth testing .
    glEnable(GL_COLOR_MATERIAL) 
    #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ 
    # Lighting.
    glEnable(GL_LIGHT0)  # First light = LIGHT0 
    glEnable(GL_LIGHT1)  # Second light = LIGHT1 

    glEnable(GL_NORMALIZE) 
    glEnable(GL_COLOR_MATERIAL) 
    glEnable(GL_LIGHTING) 
 
    glLightfv(GL_LIGHT0, GL_SPECULAR, light_specular_red) # LIGHT0 
    glLightfv(GL_LIGHT0, GL_POSITION, position_light_0) 

    glLightfv(GL_LIGHT1, GL_SPECULAR, light_specular_blue) # LIGHT1 
    glLightfv(GL_LIGHT1, GL_POSITION, position_light_1) 
 
    glMaterialfv(GL_FRONT, GL_SPECULAR,  material_specular) 
    glMaterialfv(GL_FRONT, GL_SHININESS, high_shininess) 
    #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^        
    glMatrixMode(GL_PROJECTION) 
    glLoadIdentity()          
    gluPerspective(45.0, float(Width)/float(Height), 0.1, 100.0) 
    glMatrixMode(GL_MODELVIEW) 
#===================================================== 
# Set up the rotation parameters 
angular_position = 0.0   # Position of light. 
rradius = 0.5            # Radius of glutSolidSphere 
sslices = 30            
sstacks = 30 

kula_1 =  [ 0.01, 0.01, 0.01 ] # Dark charcoal. 
kula_2 =  [  0.8, 0.94, 0.0  ]   # Yellow 
kula_3 =  [  1.0,  1.0, 1.0  ]    # White 

def group_4spheres(xx, yy, zz, kula): 
    """ Draw a group of four spheres in a square formation. 
          The position and color parameters are supplied as arguments. 
    """ 
    glLoadIdentity() 
    glColor(kula[0], kula[1], kula[2] ) 
    glTranslatef(xx,  yy,  zz  ) 
    glutSolidSphere(rradius, sslices, sstacks ) 


def DrawGLScene(): 
    “””   The main drawing function. 
    “””
    global angular_position 
    light_position = [ 2.0, 5.0, 5.0, 0.0 ] 
    glLightfv(GL_LIGHT0, GL_POSITION, light_position) 
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  

    group_4spheres(-1.0,  0.0, -2.0, kula_1)   # Dark charcoal. 
    group_4spheres( 0.0,  0.0, -6.0, kula_2)   # Yellow. 
    group_4spheres( 1.0, -1.0, -4.0, kula_3)   # White.
