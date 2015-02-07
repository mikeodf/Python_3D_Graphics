"""  ch13 No.1  
Program name: opengl_fog_material_lighting_1.py 
Objective: Explore fog design. 

keywords: opengl, fog, lighting, materials, sphere, icosahedron. 
==============================================================================79 
From the book "Python Graphics for Games: Working in 3 Dimensions"

Comments: Experimentation with fog. 

fog properties: 
  glFogi(GL_FOG_MODE, GL_LINEAR)           # Fog linear gradient calculated using (Near-Far) 
  glFogf(GL_FOG_START, 1.0);               # Near distance in the fog equation: f =  (Near-c)/(Near-Far)  
  glFogf(GL_FOG_END, 17.0);                # Far distance in the fog equation 

  glFogi(GL_FOG_MODE, GL_EXP)        #   f = 1/e**(distance*density) 
  glFogi(GL_FOG_MODE, GL_EXP2)       #   f = 1/(e**(distance*density))**2 
  glFogf(GL_FOG_DENSITY, 0.5)              # Exponent multiplier in fog equation f = 1/e**(distance*density) 

Tested on: Python 2.6
 Python 2.7.3
Test failed with Python 3.2.3         
Author:  Mike Ohlson de Fine 
""" 
from OpenGL.GL import * 
from OpenGL.GLUT import * 
from OpenGL.GLU import * 
import sys 
import math 

# material colors. 
kula_red      =  [ 1.0,0.0, 0.0 ]        # Red 
kula_green    =  [ 0.0,1.0, 0.0 ]      # Green 
kula_blue     =  [ 0.0,0.0, 1.0 ]       # Blue 
kula_white    =  [ 1.0,1.0,1.0 ]       # White 
kula_charcoal =  [ 0.1,0.1,0.1 ]      # Dark charcoal 

# Lighting Parameters. 
light_specular = [ 1.0, 1.0, 1.0, 1.0 ] 
light_position_1 = [ 10.0, 5.0, 5.0, 1.0 ] 

# Material Parmeters. 
material_specular   = [ 1.0, 1.0, 1.0, 1.0 ] 
high_shininess = [ 127.0 ] 

def InitGL(Width, Height):               # Set OpenGL up in the required state .
    glClearColor(0.6, 0.6, 0.6, 1.0)     # Set the background color to Black .
    glClearDepth(1.0)                         # Clear the Depth buffer .
    glDepthFunc(GL_LESS)              # Type of depth test. 
    glEnable(GL_DEPTH_TEST)      # Enable depth testing .
    #----------------------------- 
    # Lighting and materials 
    glEnable(GL_LIGHT0) 
    glEnable(GL_NORMALIZE) 
    glEnable(GL_COLOR_MATERIAL) 
    glEnable(GL_LIGHTING) 
 
    glLightfv(GL_LIGHT0, GL_SPECULAR, light_specular) 
    glLightfv(GL_LIGHT0, GL_POSITION, light_position_1) 
    glMaterialfv(GL_FRONT, GL_SPECULAR,  material_specular) 
    glMaterialfv(GL_FRONT, GL_SHININESS, high_shininess) 
    #########  FOG  parameters start ################################################# 
    # Fog Parameters 
    glEnable(GL_FOG)                                         # Enable fog    
    fogColor=(0.6, 0.6, 0.6, 1.0)                            # fog color 
    glFogfv(GL_FOG_COLOR, fogColor)          # Set fog color (grey). 

    glFogi(GL_FOG_MODE, GL_LINEAR)      # Linear Fog settings: GL_LINEAR. 
    glFogf(GL_FOG_START, 1.0)                       # Near distance in the fog equation: f =  (near-c)/(near-far)   
    glFogf(GL_FOG_END, 17.0)                         # Far distance in the fog equation: 

    #glFogi(GL_FOG_MODE, GL_EXP)              # Exponential fog 
    #glFogi(GL_FOG_MODE, GL_EXP2)            # Exponential squared fog   
    #glFogf(GL_FOG_DENSITY, 0.5)             # Fog density exponent for both GL_EXP and GL_EXP2 
    #########  FOG  parameters end ################################################## 
    glShadeModel(GL_SMOOTH)          
    glMatrixMode(GL_PROJECTION) 
    glLoadIdentity()          
    gluPerspective(40.0, float(Width)/float(Height), 1.0, 30.0) 
    glMatrixMode(GL_MODELVIEW) 
#===================================================== 
# Planetary parameters and Controls 
#================================ 
sun_location   = [0.0, 1.0, -9.0 ]  # Position of the Sun. 
sun_earth = 6.0                            # Distances between planet and sun. 
earth_orbit_angle = 0                  # Planet orbit position in path around sun. 

def orbit_yz_plane(radius, angle): 
    """ GetrRelative coordinates wrt sun due to orbital rotation. 
        Distance of planet = radius, angle = radian distance around orbit. 
    """ 
    yy = radius * math.cos(angle) 
    zz = radius * math.sin(angle) 
    return [yy, zz] 

def add_vectors(loc1, loc2): 
    """ Vector addition of 3D vectors. 
        Solar system position is sum af sun's position 
        added to position relative to the sun. 
    """ 
    xx = loc1[0] + loc2[0] 
    yy = loc1[1] + loc2[1] 
    zz = loc1[2] + loc2[2] 
    return [ xx, yy, zz ] 
#===================================================== 
# Rows of Spheres 
#================== 
rradius = 0.5 
sslices = 30 
sstacks = 30 
shape = [ rradius, sslices, sstacks ] # Shape of sphere 

def sphereic(xx, yy, zz, x_incr, y_incr, z_incr, kula): 
    """ Draw a group of four spheres in a row formation. 
        The position and color parameters are supplied as arguments. 
    """ 
    glLoadIdentity() 
    glColor(kula[0], kula[1], kula[2] ) 
    xyz = [ xx+x_incr,  yy+y_incr,  zz+z_incr ] 
    glTranslatef(xyz[0], xyz[1], xyz[2] ) 
    glutSolidSphere(shape[0], shape[1], shape[2]) 

def row_spheres( xx, yy, zz, x_incr, y_incr, z_incr): 
    """  Draw a row of five colored spheres. 
         Charcoal, red, green, blue, white. 
    """ 
    xx = -1.0 
    yy = -3.0 
    zz = -4.0 
    sphereic(xx, yy, zz, x_incr, y_incr, z_incr, kula_charcoal) 
    x_incr = 0.0     
    sphereic(xx, yy, zz, x_incr, y_incr, z_incr, kula_red) 
    x_incr = 1.0 
    sphereic(xx, yy, zz, x_incr, y_incr, z_incr, kula_green) 
    x_incr = 2.0 
    sphereic(xx, yy, zz, x_incr, y_incr, z_incr, kula_blue) 
    x_incr = 3.0 
    sphereic(xx, yy, zz, x_incr, y_incr, z_incr, kula_white) 

# The main drawing function. 
def DrawGLScene(): 
    global sun_location, sun_earth, earth_orbit_angle 
   
    glLightfv(GL_LIGHT0, GL_POSITION, light_position_1 ) 
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  # Clear Screen and Depth buffer 

    xx = -1.0 
    yy = -3.0 
    zz = -4.0 
    row_spheres( xx, yy, zz, -1.0, 2.0, 0.0)           # First row.
    row_spheres( xx, yy, zz, -1.0, 2.0, -4.0)          # Second row.
    row_spheres( xx, yy, zz, -1.0, 2.0, -8.0)          # Third row.
    row_spheres( xx, yy, zz, -1.0, 2.0, -12.0)        # Fourth row.
    
    # Draw Icosahedron - Planet 
    glLoadIdentity() 
    earth_orbit_angle += 0.01 
    new_zx = orbit_yz_plane(sun_earth, earth_orbit_angle) 
    temp_earth_loc = [0.0, new_zx[0], new_zx[1] ]           # New planet position relative to sun. 
    temp_earth_loc = add_vectors(sun_location, temp_earth_loc) 
    glTranslatef(temp_earth_loc[0], temp_earth_loc[1], temp_earth_loc[2])  
    glColor(1.0,0.2, 0.2)  # Reddish. 
    glutSolidIcosahedron() 

    glutSwapBuffers() 

def main(): 
    glutInit(sys.argv) 
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)   
    glutInitWindowSize(1000, 600) 
    glutInitWindowPosition(0, 0)  
    window = glutCreateWindow("Fog. linear:color: grey(0.6, 0.6, 0.6, 1.0). start-end:1-17 ") 
    glutDisplayFunc(DrawGLScene) 
    glutIdleFunc(DrawGLScene)  
    InitGL(1000, 600)                
    glutMainLoop()                 

main()
