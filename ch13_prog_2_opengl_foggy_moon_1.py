"""  ch13 No.2  
Program name: opengl_foggy_moon_1.py 
Objective: Demonstrate fog. 

keywords: opengl, cube, moon, fog 
==========================================================================79 
From the book "Python Graphics for Games: Working in 3 Dimensions"

Comments: Fog blends a fog color with each rasterized pixel. 
             The fog is applied an top of the texture image. 
             The fog "density" is controlled by a blending factor f. 
             Factor f is computed in one of three ways, 
             depending on the fog mode (linear or exponentials). 
             Let c be either the distance in eye coordinate from the origin, then 
             the equation for GL_LINEAR fog is f =  (near-c)/(near-far).   

Tested on: Python 2.7.3
Test failed with Python 3.2.3  - problem using Image.py module.       
Author:          Mike Ohlson de Fine           
""" 
from OpenGL.GL import * 
from OpenGL.GLUT import * 
from OpenGL.GLU import * 
import sys 
from Image import * 
#sys.path.append("/usr/lib/python2.7/dist-packages/PIL/") # Failed with python3
xrot = yrot = zrot = 0.0              # Rotations for cube. 
fogColor=(0.0, 0.0, 0.2, 1.0)         # Fog color (dark blue).

def LoadTextures(): 
    image = open("/home/mikeodf/constr/images_opengl/Moon.jpg")     
    ix = image.size[0] 
    iy = image.size[1] 
    image = image.tostring("raw", "RGBX", 0, -1) 
    
    # Create Texture    
    glBindTexture(GL_TEXTURE_2D, glGenTextures(1))   # 2D texture. 
    glPixelStorei(GL_UNPACK_ALIGNMENT,1) 
    glTexImage2D(GL_TEXTURE_2D, 0, 3, ix, iy, 0, GL_RGBA, GL_UNSIGNED_BYTE, image) 
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP) 
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP) 
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT) 
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT) 
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST) 
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST) 
    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL) 

def InitGL(Width, Height):               # OpenGL initialization function. 
    LoadTextures() 
    glEnable(GL_TEXTURE_2D) 
    glClearDepth(1.0)                    # Clear the Depth buffer. 
    glDepthFunc(GL_LESS)                 # Type Of Depth test. 
    glEnable(GL_DEPTH_TEST)              # Enable Depth testing  
    glMatrixMode(GL_PROJECTION) 
    glLoadIdentity()                     # Reset The projection Matrix                                        
    gluPerspective(45.0, float(Width)/float(Height), 0.1, 100.0) 
    glMatrixMode(GL_MODELVIEW) 


def DrawGLScene(): # The main drawing function. 
    global xrot, yrot, zrot, texture 

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  # Clear screen and Depth buffer. 
    glLoadIdentity()                                                                                     # Reset The View    
    glClearColor(0.0,0.0,0.1,1.0)                                                                 # Background color. Dark blue 
    
    glEnable(GL_FOG)                  # Enable fog    
    glFogi(GL_FOG_MODE, GL_LINEAR)    # Fog settings: GL_LINEAR, GL_EXP, or GL_EXP2. 
    glFogfv(GL_FOG_COLOR, fogColor)   # Set fog color (blue).    
    glFogf(GL_FOG_DENSITY, 1.0)       # Set fog density 
    glFogf(GL_FOG_START, 0.2)         # Near distance in the fog equation: f =  (near-c)/(near-far)   
    glFogf(GL_FOG_END, 5.0)           # Far distance in the fog equation.
   
    glTranslatef(0.0,0.0,-4.8)        # Move cube into the screen - negative z-direction. 
    glRotatef(xrot,1.0,0.0,0.0)       # Rotate The Cube On It's X Axis 
    glRotatef(yrot,0.0,1.0,0.0)       # Rotate The Cube On It's Y Axis 
    glRotatef(zrot,0.0,0.0,1.0)       # Rotate The Cube On It's Z Axis 

    glBegin(GL_QUADS)   # Three faces of a cube.   
    # Front Face. The texture's corners have to match the quad's corners .
    glTexCoord2f(0.0, 0.0); glVertex3f(-1.0, -1.0,  1.0)    # Bottom Left Of The Texture and Quad 
    glTexCoord2f(1.0, 0.0); glVertex3f( 1.0, -1.0,  1.0)    # Bottom Right Of The Texture and Quad 
    glTexCoord2f(1.0, 1.0); glVertex3f( 1.0,  1.0,  1.0)    # Top Right Of The Texture and Quad 
    glTexCoord2f(0.0, 1.0); glVertex3f(-1.0,  1.0,  1.0)    # Top Left Of The Texture and Quad 

    # Top Face 
    glTexCoord2f(0.0, 1.0); glVertex3f(-1.0,  1.0, -1.0)    # Top Left Of The Texture and Quad 
    glTexCoord2f(0.0, 0.0); glVertex3f(-1.0,  1.0,  1.0)    # Bottom Left Of The Texture and Quad 
    glTexCoord2f(1.0, 0.0); glVertex3f( 1.0,  1.0,  1.0)    # Bottom Right Of The Texture and Quad 
    glTexCoord2f(1.0, 1.0); glVertex3f( 1.0,  1.0, -1.0)    # Top Right Of The Texture and Quad 

    # Right face 
    glTexCoord2f(1.0, 0.0); glVertex3f( 1.0, -1.0, -1.0)    # Bottom Right Of The Texture and Quad 
    glTexCoord2f(1.0, 1.0); glVertex3f( 1.0,  1.0, -1.0)    # Top Right Of The Texture and Quad 
    glTexCoord2f(0.0, 1.0); glVertex3f( 1.0,  1.0,  1.0)    # Top Left Of The Texture and Quad 
    glTexCoord2f(0.0, 0.0); glVertex3f( 1.0, -1.0,  1.0)    # Bottom Left Of The Texture and Quad.
    glEnd();               
    
    xrot  = xrot + 0.2                # X rotation 
    yrot = yrot + 0.1                 # Y rotation 
    zrot = zrot + 0.1                 # Z rotation 

    glutSwapBuffers() 

def main(): 
    glutInit(sys.argv) 
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH) # Select display mode.
    glutInitWindowSize(640, 480) 
    glutInitWindowPosition(0, 0) 
    window = glutCreateWindow("Blue Moon and Fog")   
    glutDisplayFunc(DrawGLScene) 
    glutIdleFunc(DrawGLScene) 
    InitGL(640, 480)  
    glutMainLoop() 

main()
