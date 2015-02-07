"""  ch12 No.5  
Program name: multiple_bouncing_balls_1.py 
Objective: Animate a set of bouncing textured balls. 

keywords: opengl, balls, bouncing, texture 
==============================================================================79 
From the book "Python Graphics for Games: Working in 3 Dimensions"

Tested on: Python 2.6, Python 2.7.3, Python 3.2.3       
Author:          Mike Ohlson de Fine 
""" 
from OpenGL.GL import * 
from OpenGL.GLUT import * 
from OpenGL.GLU import * 
from Image import * 

# Starting position and Velocity of the cube. 
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
print 'ix:', ix                            
print 'iy:', iy 


def texture_setup(image_name, texture_num, ix, iy): 
    """  Assign texture attributes to specific images. 
    """ 
   {{ code identical to previous example (bouncing_square_1.py ) }}

def LoadTextures(): 
    """  Open texture images and convert them to "raw" pixel maps and 
         bind or associate each image with and integer refernece number. 
    """ 
    image_1 = open("/home/mikeodf/constr/images_opengl/steel_ball3.jpg")  
    image_2 = open("/home/mikeodf/constr/images_opengl/steel_green_ball3.jpg")   
    image_3 = open("/home/mikeodf/constr/images_opengl/steel_blue_ball3.jpg")   
    image_4 = open("/home/mikeodf/constr/images_opengl/steel_red_ball3.jpg")    

    image_1 = image_1.tostring("raw", "RGBX", 0, -1)   # Convert bmp to the type needed for textures .
    image_2 = image_2.tostring("raw", "RGBX", 0, -1)   
    image_3 = image_3.tostring("raw", "RGBX", 0, -1)  
    image_4 = image_4.tostring("raw", "RGBX", 0, -1)   
    glGenTextures(3, texture_1)                                        # Create texture number and names and size. 
    
    texture_setup(image_1, 0, ix, iy) 
    texture_setup(image_2, 1, ix, iy) 
    texture_setup(image_3, 2, ix, iy) 
    texture_setup(image_4, 3, ix, iy) 


def InitGL(Width, Height):           
    """ A general OpenGL initialization function.  Sets all of the initial parameters. 
        We call this right after our OpenGL window is created. 
    """ 
    {{ code identical to previous example (bouncing_square_1.py ) }}


def DrawFrontFace(): 
        """   A texture binding created with glBindTexture remains active until a different texture 
              is bound to the same target, or until the bound texture is deleted with glDeleteTextures.      
        """ 
	global xpos_1, ypos_1, zpos_1, xvel_1, yvel_1, zvel_1 
	global xpos_2, ypos_2, zpos_2, xvel_2, yvel_2, zvel_2 
	global xpos_3, ypos_3, zpos_3, xvel_3, yvel_3, zvel_3 
	global xpos_4, ypos_4, zpos_4, xvel_4, yvel_4, zvel_4 

	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)	

               # Textured cube 1 (grey). 
	glLoadIdentity()					             #  Reset the view. 
	glTranslatef(xpos_1, ypos_1, zpos_1)			# Shift cube incrementally. 
              make_cube_1(texture_1, 0)  # "0" is the first index no. of a four member sequence - images.  

             # Textured cube 2 (green). 
	glLoadIdentity()					              # Reset the view. 
	glTranslatef(xpos_2, ypos_2, zpos_2)			# Shift cube incrementally. 
              make_cube_1(texture_1, 1)   # "1" is the second index no. of a four member sequence - images. 

             # Textured cube 3 (blue). 
	glLoadIdentity()					             # Reset the view. 
	glTranslatef(xpos_3, ypos_3, zpos_3)			# Shift cube incrementally. 
              make_cube_1(texture_1, 2)  # "2" is the third  index no. of a four member sequence - images. 

             # Textured cube 4 (red). 
	glLoadIdentity()					             # Reset the view. 
	glTranslatef(xpos_4, ypos_4, zpos_4)			# Shift cube incrementally. 
              make_cube_1(texture_1, 3)  # "3" is the fourth index no. of a four member sequence - images.  

        # Ball_1 - grey : crude bounce simulation.   
        xpos_1 = xpos_1 + xvel_1 
        ypos_1 = ypos_1 + yvel_1 
        zpos_1 = zpos_1 + zvel_1 
        if xpos_1 >= 3.0 or xpos_1 <= -2.0: 
            xvel_1 = -xvel_1 
        if ypos_1 >= 3.0 or ypos_1 <= -3.0: 
            yvel_1 = -yvel_1         
        if zpos_1 >= -5.01 or zpos_1 <= -30.0: 
            zvel_1 = -zvel_1   

        # Ball_2 - green : crude bounce simulation.     
        xpos_2 = xpos_2 + xvel_2 
        ypos_2 = ypos_2 + yvel_2 
        zpos_2 = zpos_2 + zvel_2 
        if xpos_2 >= 3.0 or xpos_2 <= -2.0: 
            xvel_2 = -xvel_2 
        if ypos_2 >= 3.0 or ypos_2 <= -3.0: 
            yvel_2 = -yvel_2         
        if zpos_2 >= -5.01 or zpos_2 <= -30.0: 
            zvel_2 = -zvel_2     

        # Ball_3 - blue : crude bounce simulation.     
        xpos_3 = xpos_3 + xvel_3 
        ypos_3 = ypos_3 + yvel_3 
        zpos_3 = zpos_3 + zvel_3 
        if xpos_3 >= 3.0 or xpos_3 <= -2.0: 
            xvel_3 = -xvel_3 
        if ypos_3 >= 3.0 or ypos_3 <= -3.0: 
            yvel_3 = -yvel_3         
        if zpos_3 >= -5.01 or zpos_3 <= -30.0: 
            zvel_3 = -zvel_3     

        # Ball_4 - red : crude bounce simulation.    
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
#========================================================= 
def main(): 
  {{ code identical to previous example (bouncing_square_1.py ) }}
main()
