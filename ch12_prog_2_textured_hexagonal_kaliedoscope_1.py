"""  ch12 No.2 
Program name: textured_hexagonal_kaliedoscope_1.py 
Objective: Experiment with triangular texture mappings settings. 

keywords: opengl, kaliedoscope, triangle, animation 
==============================================================================79 
From the book "Python Graphics for Games: Working in 3 Dimensions"

Tested on: Python 2.6, Python 2.7.3, Python 3.2.3       
Author:          Mike Ohlson de Fine 
""" 
from OpenGL.GL import * 
from OpenGL.GLUT import * 
from OpenGL.GLU import * 
from Image import * 

texture_1 = 0   

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
    image_1 = open("/home/mikeodf/constr/images_opengl/poppies_30.jpg")   
    ix = image_1.size[0]                           # image.size is a PIL function. 
    iy = image_1.size[1] 
    print 'ix:', ix                                        # Just checking. 
    print 'iy:', iy 
    image_1 = image_1.tostring("raw", "RGBX", 0, -1)   # Convert jpg to the 'string' for textures. 
    texture_setup(image_1, 0, ix, iy) 

def InitGL(Width, Height):           
    """ A general OpenGL initialization function.  Sets all of the initial parameters. 
          Called immediately after the OpenGL window is created. 
    """ 
    glClearColor(0.0, 0.0, 0.0, 0.0)  # Clear the background color to black. 
    glMatrixMode(GL_PROJECTION) 
    glLoadIdentity()                  # Reset The Projection Matrix.   
    gluPerspective(30.0, float(Width)/float(Height), 0.1, 100.0) # Aspect Ratio Of The Window, makes it resizable. 
    glMatrixMode(GL_MODELVIEW) 


def make_triangular_rectangle_1(texture): 
        """   Two Triangluar areas composed of two halves of an equilateral triangle.
                The second triangle will displat a horizontally inverted copy of the same image on the first triangle.     
                The apex of both triangles are on the ( 0, 0, 0 ) position in 3d space. This simplifies positioning
                after rotation.
        """ 
        glBindTexture(GL_TEXTURE_2D,texture)	 
        # Rectangle Face (Each texture's corner is matched a quad's corner.) 
        glBegin(GL_QUADS)	 
	glTexCoord2f(0.0, 0.0), glVertex3f( -1.0, -1.732,  0.0)	# Bottom Left Of The Texture and Quad 
	glTexCoord2f(1.0, 0.0), glVertex3f(  0.0, -1.732,  0.0)	# Bottom Right Of The Texture and Quad 
	glTexCoord2f(1.0, 1.0), glVertex3f(  0.00,  0.0,  0.0)	# Texture Top Right to Quad-narrow end. 
	glTexCoord2f(0.0, 1.0), glVertex3f(  0.00,  0.0,  0.0)	# Texture Top Left to Quad-narrow end.	 
	glEnd() 

        glBegin(GL_QUADS)	 
	glTexCoord2f(1.0, 0.0), glVertex3f(  0.0, -1.732,  0.0)	
	glTexCoord2f(0.0, 0.0), glVertex3f(  1.0, -1.732,  0.0)	
	glTexCoord2f(0.0, 1.0), glVertex3f(  0.00,  0.0,  0.0)	
	glTexCoord2f(1.0, 1.0), glVertex3f(  0.00,  0.0,  0.0)	 
	glEnd() 
        
def DrawFrontFace(): 
        """   A texture binding created with glBindTexture remains active until a different texture 
              is bound to the same target, or until the bound texture is deleted with glDeleteTextures.      
        """ 
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  
	glLoadIdentity()			            
	glTranslatef(0.0, 0.0, -5.0) 
              glScalef(0.6, 0.6, 0.6)        			 
              make_triangular_rectangle_1(texture_1) 
              glRotatef(60.0, 0.0, 0.0, 1.0) 
             make_triangular_rectangle_1(texture_1)        
             glRotatef(60.0, 0.0, 0.0, 1.0) 
             make_triangular_rectangle_1(texture_1) 
             glRotatef(60.0, 0.0, 0.0, 1.0) 
             make_triangular_rectangle_1(texture_1) 
             glRotatef(60.0, 0.0, 0.0, 1.0) 
           make_triangular_rectangle_1(texture_1) 
           glRotatef(60.0, 0.0, 0.0, 1.0) 
           make_triangular_rectangle_1(texture_1) 
           glRotatef(60.0, 0.0, 0.0, 1.0) 
           make_triangular_rectangle_1(texture_1) 
             	 
          glutSwapBuffers() 
#==============================================================
def main(): 
  glutInit("") 
  glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH) 
  glutInitWindowSize(650, 650) 
  window = glutCreateWindow("Textured rectangle: Kaleidoscopic 60 degree rotations.") 
  LoadTextures()   
  glutDisplayFunc(DrawFrontFace) 
  InitGL(650, 650)                 # Initialize our window. 
  glutMainLoop()                   # Start the event processing engine  

main()
