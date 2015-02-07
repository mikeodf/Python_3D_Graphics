"""  ch12 No.1  
Program name: textured_rectangle_1.py 
Objective: Experiment with different texture mappings settings. 

keywords: opengl, transparency, ball textures, animation 
==============================================================================79 
From the book "Python Graphics for Games: Working in 3 Dimensions"

Comments: A texture binding created with glBindTexture remains active until a new or 
different texture is bound to the same target, or until the bound texture is 
deleted with glDeleteTextures.
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
NB – tHIS Does not work with Python 3.3
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Tested on: Python 2.6, Python 2.7.3, Python 3.2.3       
Author:          Mike Ohlson de Fine 
""" 
from OpenGL.GL import * 
from OpenGL.GLUT import * 
from OpenGL.GLU import * 
from Image import * 

texture_1 = 0   # An integer label associated with the texture.

def texture_setup(image_name, texture_num, ix, iy): 
    """  Assign texture attributes to specific images. 
    """ 
    glBindTexture(GL_TEXTURE_2D, texture_1)    
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
    image_1 = open("/home/mikeodf/constr/images_opengl/RECT_test_pattern.jpg")   
    ix = image_1.size[0]                           # image.size is a PIL function. 
    iy = image_1.size[1] 
    print 'ix:', ix                                        # Just checking. 
    print 'iy:', iy 
    image_1 = image_1.tostring("raw", "RGBX", 0, -1)   # Convert jpg to the 'string' for textures. 
    texture_setup(image_1, 0, ix, iy) 

def InitGL(Width, Height):           
    """ A general OpenGL initialization function.  Sets all of the initial parameters. 
        We call this right after our OpenGL window is created. 
    """ 
    glClearColor(0.0, 0.0, 0.0, 0.0)                                              # Clear the background color to black. 
    glMatrixMode(GL_PROJECTION) 
    glLoadIdentity()                                                                      # Reset The Projection Matrix.   
    gluPerspective(30.0, float(Width)/float(Height), 0.1, 100.0) # Aspect Ratio Of The Window, makes it resizable. 
    glMatrixMode(GL_MODELVIEW) 

#============================================================== 
def make_rectangle_1(texture): 
        """   A generic rectangle. 
        """ 
        glBindTexture(GL_TEXTURE_2D,texture)	 
        # Rectangle Face (Each texture's corner is matched a quad's corner.) 
        glBegin(GL_QUADS)	 
	glTexCoord2f(0.0, 0.0); glVertex3f(-1.0, -1.0,  1.0)	# Bottom Left Of The Texture and Quad .
	glTexCoord2f(1.0, 0.0); glVertex3f( 1.0, -1.0,  1.0)	# Bottom Right Of The Texture and Quad .
	glTexCoord2f(1.0, 1.0); glVertex3f( 1.0,  1.0,  1.0)	             # Top Right Of The Texture and Quad .
	glTexCoord2f(0.0, 1.0); glVertex3f(-1.0,  1.0,  1.0)	# Top Left Of The Texture and Quad.	 
	glEnd(); 
        
def DrawFrontFace(): 
        """   A texture binding created with glBindTexture remains active until a different texture 
              is bound to the same target, or until the bound texture is deleted with glDeleteTextures.      
        """ 
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  # Clear the screen and Depth buffer 
	glLoadIdentity()			            # Reset the geometry matrix. 
	glTranslatef(0.0, 0.0, -5.0)			 
              make_rectangle_1(texture_1) 
	glutSwapBuffers() 

def main(): 
  glutInit("") 
  glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH) 
  glutInitWindowSize(650, 650) 
  window = glutCreateWindow("Textured rectangle.") 
  LoadTextures()   
  glutDisplayFunc(DrawFrontFace) 
  InitGL(650, 650)                 # Initialize our window. 
  glutMainLoop()                   # Start the event processing engine.  

main()
