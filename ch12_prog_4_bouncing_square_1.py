"""  ch12 No.4  
Program name: bouncing_square_1.py 
Objective: Animate a square covered with a steel ball texture.. 
OpenGL will not accept .gif images. 

keywords: opengl, square, animation 
==============================================================================79 
From the book "Python Graphics for Games: Working in 3 Dimensions" 

Tested on: Python 2.6, Python 2.7.3, Python 3.2.3       
Author:          Mike Ohlson de Fine 
""" 
from OpenGL.GL import * 
from OpenGL.GLUT import * 
from OpenGL.GLU import * 
from Image import * 

# Position and Velocity of the cube. 
# ball_1 
xpos_1 = ypos_1 = 0.0 
zpos_1 = -10.0 
xvel_1 = 0.02 
yvel_1 = 0.03 
zvel_1 = 0.01 
#================================================================= 
texture_1 = 0, 1, 2, 3, 4, 5 
image_proto = open("/home/mikeodf/constr/images_opengl/steel_ball3.jpg")   
ix = image_proto.size[0]      # image.size is a PIL function. 
iy = image_proto.size[1] 
print 'ix:', ix             # Just checking. 
print 'iy:', iy 

def texture_setup(image_name, texture_num, ix, iy): 
    """  Assign texture attributes to specific images. 
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
    image_1 = open("/home/mikeodf/constr/images_opengl/steel_blue_ball3.jpg")  
    image_1 = image_1.tostring("raw", "RGBX", 0, -1)   # convert bmp to the type needed for textures 
    glGenTextures(11, texture_1)   # Create texture number and names and size. 
    texture_setup(image_1, 0, ix, iy) 

def InitGL(Width, Height):           
    """ A general OpenGL initialization function.  Sets all of the initial parameters. 
        We call this right after our OpenGL window is created. 
    """ 
    glClearColor(0.0, 0.0, 0.0, 0.0)  # Clear the background color to black. 
    glClearDepth(1.0)                 # Clear the Depth buffer. 
    glDepthFunc(GL_LESS)              # The type Of depth test to do. 
    glEnable(GL_DEPTH_TEST)           # Leave this Depth Testing and observe the visual weirdness. 
    glMatrixMode(GL_PROJECTION) 
    glLoadIdentity()                  # Reset The Projection Matrix.   
    gluPerspective(30.0, float(Width)/float(Height), 0.1, 100.0) # Aspect Ratio Of The Window, makes it resizable. 
    glMatrixMode(GL_MODELVIEW) 
    
#============================================================== 
def make_cube_1(texture, texture_index): 
        """   A generic swuare. A texture binding created with glBindTexture remains active until 
               a different texture is bound to the same target, or until the bound texture is 
               deleted with glDeleteTextures.      
        """ 
        glBindTexture(GL_TEXTURE_2D,texture[texture_index])	 
        # Front Face (Each texture's corner is matched a quad's corner.) 
        glBegin(GL_QUADS)	 
	glTexCoord2f(0.0, 0.0); glVertex3f(-1.0, -1.0,  1.0)	# Bottom Left Of The Texture and Quad 
	glTexCoord2f(1.0, 0.0); glVertex3f( 1.0, -1.0,  1.0)	# Bottom Right Of The Texture and Quad 
	glTexCoord2f(1.0, 1.0); glVertex3f( 1.0,  1.0,  1.0)   	#  Top Right Of The Texture and Quad 
	glTexCoord2f(0.0, 1.0); glVertex3f(-1.0,  1.0,  1.0)	# Top Left Of The Texture and Quad	 
	glEnd(); 
        

def DrawFrontFace(): 
        """   A texture binding created with glBindTexture remains active until a different texture 
              is bound to the same target, or until the bound texture is deleted with glDeleteTextures.      
        """ 
	global xpos_1, ypos_1, zpos_1, xvel_1, yvel_1, zvel_1 
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)   
        #The textured square. 
	glLoadIdentity()					              # Reset The View 
	glTranslatef(xpos_1, ypos_1, zpos_1)			# Shift cube left and back. 
        make_cube_1(texture_1, 0)  # "0" is the first index no. of a six member sequence - images.  

        # Ball_1 - blue    
        xpos_1 = xpos_1 + xvel_1 
        ypos_1 = ypos_1 + yvel_1 
        zpos_1 = zpos_1 + zvel_1 
        if xpos_1 >= 3.0 or xpos_1 <= -2.0: 
            xvel_1 = -xvel_1 
        if ypos_1 >= 3.0 or ypos_1 <= -3.0: 
            yvel_1 = -yvel_1         
        if zpos_1 >= -5.01 or zpos_1 <= -30.0: 
            zvel_1 = -zvel_1   

	glutSwapBuffers() 
#========================================================================== 
def main(): 
  glutInit("") 
  glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH) 
  glutInitWindowSize(500, 500) 
  window = glutCreateWindow("Textured rectangle bouncing") 
  LoadTextures()   
  glutDisplayFunc(DrawFrontFace) 
  glutIdleFunc(DrawFrontFace)            # When we are doing nothing, redraw the scene. 
  InitGL(500, 500)                                # Initialize our window. 
  glutMainLoop()                                   # Start the event processing engine  

main()
