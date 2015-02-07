"""  ch13 No.4  
Program name: opengl_transparency_bouncing_balls_1.py 
Objective: Vary transparency on the bouncing balls. 

keywords: opengl, transparency, ball textures, animation 
======================================================================79 
From the book "Python Graphics for Games: Working in 3 Dimensions"

Comments: Transparency achieved through blending. 
             Blending combines the color of a pixel that is about to be drawn 
             with the color of the pixel that is already on the screen.  

Tested on: Python 2.7.3
Test failed with Python 3.2.3        
Author:          Mike Ohlson de Fine 
""" 
from OpenGL.GL import * 
from OpenGL.GLUT import * 
from OpenGL.GLU import * 
import sys 
from Image import * 

# Position and Velocity of the cube. 
# ball_1 
xpos_1 = ypos_1 = 0.0 
zpos_1 = -10.0 
xvel_1 = 0.02 
yvel_1 = 0.03 
zvel_1 = 0.01 

# ball_2 
xpos_2 = ypos_2 = 0.0 
zpos_2 = -10.0 
xvel_2 = -0.025 
yvel_2 = -0.03 
zvel_2 = -0.01 

# ball_3 
xpos_3 = ypos_3 = 0.0 
zpos_3 = -20.0 
xvel_3 = 0.015 
yvel_3 = 0.02 
zvel_3 = 0.02 

# ball_4 
xpos_4 = ypos_4 = 0.0 
zpos_4 = -15.0 
xvel_4 = -0.02 
yvel_4 = -0.025 
zvel_4 = -0.015 

#================================================================= 
texture_1 = 0, 1, 2, 3, 4, 5 
image_proto = open("/home/mikeodf/constr/images_opengl/steel_ball3.jpg")   
ix = image_proto.size[0]      # image.size is a PIL function. 
iy = image_proto.size[1] 
print 'ix:', ix             # Just checking. 
print 'iy:', iy 
opacity = 0.0 
del_opacity = 0.001 

def timerCB(millisec): 
    glutTimerFunc(millisec, timerCB, millisec) 
    glutPostRedisplay() 


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
    image_1 = open("/home/mikeodf/constr/images_opengl/steel_ball3.jpg")  
    image_2 = open("/home/mikeodf/constr/images_opengl/steel_green_ball3.jpg")   
    image_3 = open("/home/mikeodf/constr/images_opengl/steel_blue_ball3.jpg")   
    image_4 = open("/home/mikeodf/constr/images_opengl/steel_red_ball3.jpg")    

    image_1 = image_1.tostring("raw", "RGBX", 0, -1)   # convert bmp to the type needed for textures 
    image_2 = image_2.tostring("raw", "RGBX", 0, -1)   # convert bmp to the type needed for textures 
    image_3 = image_3.tostring("raw", "RGBX", 0, -1)   # convert bmp to the type needed for textures 
    image_4 = image_4.tostring("raw", "RGBX", 0, -1)   # convert bmp to the type needed for textures 
    glGenTextures(11, texture_1)   # Create texture number and names and sizw. 
    #===================================== 
    texture_setup(image_1, 0, ix, iy) 
    texture_setup(image_2, 1, ix, iy) 
    texture_setup(image_3, 2, ix, iy) 
    texture_setup(image_4, 3, ix, iy) 


def InitGL(Width, Height):           
    """ A general OpenGL initialization function.  Sets all of the initial parameters. 
        We call this right after our OpenGL window is created. 
     glEnable(GL_BLEND); 
     glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA); 
     or glBlendFunc(GL_ONE, GL_ONE_MINUS_SRC_ALPHA) 
    """ 
    glClearColor(0.0, 0.0, 0.0, 0.0)  # Clear the background color to black. 
    glClearDepth(1.0)                 # Clear the Depth buffer. 
    glDepthFunc(GL_LESS)              # The type Of depth test to do. 
    glEnable(GL_DEPTH_TEST)           # Leave this Depth Testing and observe the visual weirdness. 
 
    glColor4f(1.0,1.0,1.0,opacity)        # Full Brightness, variable Alpha 
    glEnable(GL_BLEND) 
    glBlendFunc(GL_SRC_ALPHA,GL_ONE) #  Blending function for translucency based on source alpha value. 

    glMatrixMode(GL_PROJECTION) 
    glLoadIdentity()                  # Reset The Projection Matrix.   
    gluPerspective(30.0, float(Width)/float(Height), 0.1, 100.0) # Aspect Ratio Of The Window, makes it resizable. 
    glMatrixMode(GL_MODELVIEW) 

#============================================================== 
def make_cube_1(texture, texture_index): 
        """   A generic cube. A texture binding created with glBindTexture remains active 
                until a different texture is bound to  the same target, or until the bound texture 
               is deleted with glDeleteTextures.      
        """ 
        glBindTexture(GL_TEXTURE_2D,texture[texture_index])	 
        # Front Face (Each texture's corner is matched a quad's corner.) 
        glBegin(GL_QUADS)	 
	glTexCoord2f(0.0, 0.0); glVertex3f(-1.0, -1.0,  1.0)	# Bottom Left Of The Texture and Quad 
	glTexCoord2f(1.0, 0.0); glVertex3f( 1.0, -1.0,  1.0)	# Bottom Right Of The Texture and Quad 
	glTexCoord2f(1.0, 1.0); glVertex3f( 1.0,  1.0,  1.0)	# Top Right Of The Texture and Quad 
	glTexCoord2f(0.0, 1.0); glVertex3f(-1.0,  1.0,  1.0)	# Top Left Of The Texture and Quad	 
	glEnd(); 
        

def DrawFrontFace(): 
        """   A texture binding created with glBindTexture remains active until a different texture 
              is bound to the same target, or until the bound texture is deleted with glDeleteTextures.      
        """ 
	global xpos_1, ypos_1, zpos_1, xvel_1, yvel_1, zvel_1 
	global xpos_2, ypos_2, zpos_2, xvel_2, yvel_2, zvel_2 
	global xpos_3, ypos_3, zpos_3, xvel_3, yvel_3, zvel_3 
	global xpos_4, ypos_4, zpos_4, xvel_4, yvel_4, zvel_4 
	global opacity, del_opacity 

	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) 
        glColor4f(1.0,1.0,1.0, opacity)        # Full Brightness Alphawill vary. 
        if opacity >= 1.0: 
            del_opacity = -0.001 
        if opacity <= 0.0: 
            del_opacity = 0.001   
        opacity = opacity + del_opacity         
        # Textured square. 
       glLoadIdentity()					# Reset The View 
       glTranslatef(xpos_1, ypos_1, zpos_1)		#  Shift cube left and back. 
        make_cube_1(texture_1, 0)  # "0" is the first index no. of a four images.  

        glLoadIdentity()					
        glTranslatef(xpos_2, ypos_2, zpos_2)			
        make_cube_1(texture_1, 1)  # "1" is the second index no. of a four images. 
 
        glLoadIdentity()					
        glTranslatef(xpos_3, ypos_3, zpos_3)			
        make_cube_1(texture_1, 2)  # "2" is the third index no. of a four  images'
        glLoadIdentity()					
        glTranslatef(xpos_4, ypos_4, zpos_4)			
        make_cube_1(texture_1, 3)  # "3" is the fourth index no. of a four images.  
 
        # Ball_1 - grey    
        xpos_1 = xpos_1 + xvel_1 
        ypos_1 = ypos_1 + yvel_1 
        zpos_1 = zpos_1 + zvel_1 
        if xpos_1 >= 3.0 or xpos_1 <= -2.0: 
            xvel_1 = -xvel_1 
        if ypos_1 >= 3.0 or ypos_1 <= -3.0: 
            yvel_1 = -yvel_1         
        if zpos_1 >= -5.01 or zpos_1 <= -30.0: 
            zvel_1 = -zvel_1   

        # Ball_2 - green    
        xpos_2 = xpos_2 + xvel_2 
        ypos_2 = ypos_2 + yvel_2 
        zpos_2 = zpos_2 + zvel_2 
        if xpos_2 >= 3.0 or xpos_2 <= -2.0: 
            xvel_2 = -xvel_2 
        if ypos_2 >= 3.0 or ypos_2 <= -3.0: 
            yvel_2 = -yvel_2         
        if zpos_2 >= -5.01 or zpos_2 <= -30.0: 
            zvel_2 = -zvel_2     

        # Ball_3 - blue    
        xpos_3 = xpos_3 + xvel_3 
        ypos_3 = ypos_3 + yvel_3 
        zpos_3 = zpos_3 + zvel_3 
        if xpos_3 >= 3.0 or xpos_3 <= -2.0: 
            xvel_3 = -xvel_3 
        if ypos_3 >= 3.0 or ypos_3 <= -3.0: 
            yvel_3 = -yvel_3         
        if zpos_3 >= -5.01 or zpos_3 <= -30.0: 
            zvel_3 = -zvel_3     

        # Ball_4 - red   
        xpos_4 = xpos_4 + xvel_4 
        ypos_4 = ypos_4 + yvel_4 
        zpos_4 = zpos_4 + zvel_4 
        if xpos_4 >= 3.0 or xpos_4 <= -2.0: 
            xvel_4 = -xvel_4 
        if ypos_4 >= 3.0 or ypos_4 <= -3.0: 
            yvel_4 = -yvel_4         
        if zpos_4 >= -5.01 or zpos_4 <= -30.0: 
            zvel_4 = -zvel_4       
	glutSwapBuffers() 
#=============================================================
def main(): 
  glutInit("") 
  glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH) 
  glutInitWindowSize(1000, 1000) 
  glutInitWindowPosition(0, 0)      # the window starts at the upper left corner of the screen 
  window = glutCreateWindow("Textured rectangles bouncing") 
  LoadTextures()   
  glutDisplayFunc(DrawFrontFace) 
  glutIdleFunc(DrawFrontFace)      # Redraw the scene each cycle. 
  InitGL(1000, 1000)                       # Initialize our window. 
  glutMainLoop()                             # Start the event processing engine. 

main()
