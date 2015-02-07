"""  ch13 No.3 
Program name: opengl_transparency_moons_1.py 
Objective: Vary transparency on colored moon images. 

keywords: opengl, transparency, opacity, moon, alpha, animation 
==============================================================================79 
From the book "Python Graphics for Games: Working in 3 Dimensions"

Comments: Transparency achieved through blending. 
             Blending combines the color of a pixel that is about to be drawn 
             with the color of the pixel that is already on the screen.  

Tested on: Python 2.6, Python 2.7.3
Test failed with Python 3.2.3       
Author:          Mike Ohlson de Fine 
""" 
from OpenGL.GL import * 
from OpenGL.GLUT import * 
from OpenGL.GLU import * 
import sys 
from Image import * 

#==================================================
texture_1 = 0, 1, 2, 3 
image_proto = open("/home/mikeodf/constr/images_opengl/blue_moon256.jpg")   
ix = image_proto.size[0]      # image.size is a PIL function. 
iy = image_proto.size[1] 
print 'ix:', ix                           # Just checking. 
print 'iy:', iy 

# Make four independent opacity variables. 
opacity_full = 1.0   # Initialization - zero transparency. 
opacity_1 = 1.0 
delta_opacity_1 = 0.01 
opacity_2 = 0.01 
delta_opacity_2 = -0.001 
opacity_3 = 0.7 
delta_opacity_3 = -0.001 
opacity_4 = 0.3 
delta_opacity_4 = 0.001 

def texture_setup(image_name, texture_num, ix, iy): 
    """  Map jpg images to a square. 
    """ 
    glBindTexture(GL_TEXTURE_2D, texture_1[texture_num])   
    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_MODULATE) 
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST) 
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP) 
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP) 
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT) 
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT) 
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST) 
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT) 
    glPixelStorei(GL_UNPACK_ALIGNMENT,1) 
    glEnable(GL_TEXTURE_2D) 
    glTexImage2D(GL_TEXTURE_2D, 0, 3, ix, iy, 0, GL_RGBA, GL_UNSIGNED_BYTE, image_name) 

def LoadTextures(): 
    """  Open texture images and convert them to "raw" pixel maps and 
         bind or associate each image with and integer refernece number. 
    """ 
    image_1 = open("/home/mikeodf/constr/images_opengl/blue_moon256.jpg")  
    image_2 = open("/home/mikeodf/constr/images_opengl/red_moon256.jpg")   
    image_3 = open("/home/mikeodf/constr/images_opengl/green_moon256.jpg")   
    image_4 = open("/home/mikeodf/constr/images_opengl/white_moon256.jpg")      

    image_1 = image_1.tostring("raw", "RGBX", 0, -1)   # convert jpg to the type needed for textures .
    image_2 = image_2.tostring("raw", "RGBX", 0, -1)   
    image_3 = image_3.tostring("raw", "RGBX", 0, -1)  
    image_4 = image_4.tostring("raw", "RGBX", 0, -1)   

    glGenTextures(4, texture_1)                     # Create texture index numbers and array name. 
    
    texture_setup(image_1, 0, ix, iy)               # Map image (texture) to a square shape. 
    texture_setup(image_2, 1, ix, iy) 
    texture_setup(image_3, 2, ix, iy) 
    texture_setup(image_4, 3, ix, iy) 


def InitGL(Width, Height):           
    """ A general OpenGL initialization function.  Sets all of the initial parameters. 
        glEnable(GL_BLEND) - important for transparency .
    """ 
    glClearColor(0.0, 0.0, 0.0, 0.0)           # Set the background color to black. 
    glClearDepth(1.0)                               # Clear the Depth buffer. 
    glDepthFunc(GL_LESS)                    # Type of depth test to do. 
    glEnable(GL_DEPTH_TEST)           # Cancel this Depth Testing and observe the visual weirdness. 
 
    glColor4f(1.0,1.0,1.0,opacity_full)                    # Full Brightness, Alpha will be varied later. 
    glEnable(GL_BLEND) 
    glBlendFunc(GL_SRC_ALPHA,GL_ONE)     #  Blending function for translucency. 

    glMatrixMode(GL_PROJECTION) 
    glLoadIdentity()                                                                      # Reset The Projection Matrix.   
    gluPerspective(30.0, float(Width)/float(Height), 0.1, 100.0) # Aspect ratio. 
    glMatrixMode(GL_MODELVIEW) 

#============================================================== 
def make_square(texture, texture_index): 
        """   A generic square. 
              A texture binding created with glBindTexture remains active 
              until a different texture is bound to the same target, 
              or until the bound texture is deleted with glDeleteTextures.      
        """ 
        glBindTexture(GL_TEXTURE_2D,texture[texture_index])	 
        # Front Face (Each texture's corner is matched a quad's corner.) 
        glBegin(GL_QUADS)	 
	glTexCoord2f(0.0, 0.0); glVertex3f(-1.0, -1.0,  1.0)	# Bottom Left Of The Texture and Quad 
	glTexCoord2f(1.0, 0.0); glVertex3f( 1.0, -1.0,  1.0)	# Bottom Right Of The Texture and Quad 
	glTexCoord2f(1.0, 1.0); glVertex3f( 1.0,  1.0,  1.0)	             # Top Right Of The Texture and Quad 
	glTexCoord2f(0.0, 1.0); glVertex3f(-1.0,  1.0,  1.0)	# Top Left Of The Texture and Quad	 
	glEnd(); 
       
def DrawFrontFace(): 
        """   Repeated Shape drawing function. 
              Includes opacity control.      
        """ 
	#global opacity, delta_opacity 
        # We need the valuse of opacity to persist between graphic image update cycles. 
	global opacity_1, delta_opacity_1 
	global opacity_2, delta_opacity_2 
	global opacity_3, delta_opacity_3 
	global opacity_4, delta_opacity_4 

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # Clear screen and Depth buffer 

        # Incremental cycling of four indepencent opacity controls. 
        if opacity_1 >= 1.0: 
            delta_opacity_1 = -0.002 
        if opacity_1 <= 0.0: 
            delta_opacity_1 = 0.002   
        opacity_1 = opacity_1 + delta_opacity_1   
             
        if opacity_2 >= 1.0: 
            delta_opacity_2 = -0.002 
        if opacity_2 <= 0.0: 
            delta_opacity_2 = 0.002   
        opacity_2 = opacity_2 + delta_opacity_2   

        if opacity_3 >= 1.0: 
            delta_opacity_3 = -0.002 
        if opacity_3 <= 0.0: 
            delta_opacity_3 = 0.002   
        opacity_3 = opacity_3 + delta_opacity_3   

        if opacity_4 >= 1.0: 
            delta_opacity_4 = -0.002 
        if opacity_4 <= 0.0: 
            delta_opacity_4 = 0.002   
        opacity_4 = opacity_4 + delta_opacity_4   
 
        # Moon shots 
        glLoadIdentity()					 
        glTranslatef(-0.5, 1.0, -8.3)			 
         glColor4f(1.0,1.0,1.0,opacity_1)          # cycling opacity 
        make_square(texture_1, 0)                 # "0" is blue 
        
        glLoadIdentity()					 
        glTranslatef(0.5, 1.0, -8.2)			 
        glColor4f(1.0,1.0,1.0,opacity_2)          # cycling  opacity 
        make_square(texture_1, 1)                 # "1" is red 

       glLoadIdentity()					 
        glTranslatef(-0.5, -0.2, -8.1)			 
        glColor4f(1.0,1.0,1.0,opacity_3)          # cycling  opacity 
        make_square(texture_1, 2)                 # "2" is green 

        glLoadIdentity()		 
        glTranslatef(0.5, -0.2, -8.0)	 		 
        glColor4f(1.0,1.0,1.0,opacity_4)          # cycling  opacity	 
        make_square(texture_1, 3)                 # "3" is white  
             
    glutSwapBuffers() 
#================================
def main(): 
  glutInit("") 
  glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH) 
  glutInitWindowSize(1000, 1000) 
  glutInitWindowPosition(0, 0)      # the window starts at the upper left corner of the screen. 
  window = glutCreateWindow("Transparency - Opacity cycling.") 
  LoadTextures()   
  glutDisplayFunc(DrawFrontFace) 
  glutIdleFunc(DrawFrontFace)       # Redraw the scene each frame cycle. 
  InitGL(1000, 1000)                        # Initialize our window. 
  glutMainLoop()                              # Start the continuous event processing. 

main() 
