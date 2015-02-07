"""  ch12 No.3 
Program name: textured_cubes_rotation_1.py 
Objective: Fully cover two cubes with photo images. 
Observe the result of ignoring pixel depth. 

keywords: opengl, polygon, color control 
==============================================================================79 
From the book "Python Graphics for Games: Working in 3 Dimensions"

comments: There are six 256 x 256 bmp images on the faces of a cube. 
Usable image types:    bmp  and jpg work fine, but png does not.  
Attempting to use png we get: "SystemError: unknown raw mode"  

Tested on: Python 2.6, Python 2.7.3, Python 3.2.3       
Author:          Mike Ohlson de Fine 
""" 
from OpenGL.GL import * 
from OpenGL.GLUT import * 
from OpenGL.GLU import * 
from Image import * 

# Rotation angles for each cube. 
xrot1 = yrot1 = zrot1 = 0.0 
xrot2 = yrot2 = zrot2 = 0.0 
#================================================================= 
texture_1 = 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 
image_proto = open("/home/mikeodf/constr/images_opengl/firesky_6821.jpg")   
ix = image_proto.size[0]      # image.size is a PIL function. 
iy = image_proto.size[1] 
print 'ix:', ix                          # Just checking. 
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
    image_12 = open("/home/mikeodf/constr/images_opengl/tree_7723.jpg")   
    image_11 = open("/home/mikeodf/constr/images_opengl/sea_0049.jpg")   
    image_10 = open("/home/mikeodf/constr/images_opengl/realowl_7958.jpg")   
    image_9  = open("/home/mikeodf/constr/images_opengl/owl_1070.jpg")  
    image_8  = open("/home/mikeodf/constr/images_opengl/blusset_0036.jpg")   
    image_7  = open("/home/mikeodf/constr/images_opengl/green_0986.jpg") 
   
    image_6 = open("/home/mikeodf/constr/images_opengl/weaver_1047.jpg")   
    image_5 = open("/home/mikeodf/constr/images_opengl/watson_6202.jpg")   
    image_4 = open("/home/mikeodf/constr/images_opengl/mount_morn1.jpg")   
    image_3 = open("/home/mikeodf/constr/images_opengl/marys_1026.jpg")  
    image_2 = open("/home/mikeodf/constr/images_opengl/rainbow_6754adj.jpg")   
    image_1 = open("/home/mikeodf/constr/images_opengl/firesky_6821.jpg")   

    image_1 = image_1.tostring("raw", "RGBX", 0, -1)   # convert bmp to the type needed for textures 
    image_2 = image_2.tostring("raw", "RGBX", 0, -1)   
    image_3 = image_3.tostring("raw", "RGBX", 0, -1) 
    image_4 = image_4.tostring("raw", "RGBX", 0, -1) 
    image_5 = image_5.tostring("raw", "RGBX", 0, -1) 
    image_6 = image_6.tostring("raw", "RGBX", 0, -1) 

    image_7  = image_7.tostring( "raw", "RGBX", 0, -1)   # convert bmp to the type needed for textures 
    image_8  = image_8.tostring( "raw", "RGBX", 0, -1)   
    image_9  = image_9.tostring( "raw", "RGBX", 0, -1) 
    image_10 = image_10.tostring("raw", "RGBX", 0, -1) 
    image_11 = image_11.tostring("raw", "RGBX", 0, -1) 
    image_12 = image_12.tostring("raw", "RGBX", 0, -1) 

    glGenTextures(11, texture_1)   # Create texture number and names and sizw. 
    #===================================== 
    texture_setup(image_1, 0, ix, iy) 
    texture_setup(image_2, 1, ix, iy) 
    texture_setup(image_3, 2, ix, iy) 
    texture_setup(image_4, 3, ix, iy) 
    texture_setup(image_5, 4, ix, iy) 
    texture_setup(image_6, 5, ix, iy) 

    texture_setup(image_7, 6, ix, iy) 
    texture_setup(image_8, 7, ix, iy) 
    texture_setup(image_9, 8, ix, iy) 
    texture_setup(image_10, 9, ix, iy) 
    texture_setup(image_11, 10, ix, iy) 
    texture_setup(image_12, 11, ix, iy) 
    

def InitGL(Width, Height):           
    """ A general OpenGL initialization function.  Sets all of the initial parameters. 
        We call this right after our OpenGL window is created. 
    """ 
    glClearColor(0.0, 0.0, 0.0, 0.0)          # Clear the background color to black. 
    glClearDepth(1.0)                              # Clear the Depth buffer. 
    glDepthFunc(GL_LESS)                   # The type Of depth test to do. 
    glEnable(GL_DEPTH_TEST)           # Leave this Depth Testing and observe the visual weirdness. 
    glMatrixMode(GL_PROJECTION) 
    glLoadIdentity()                                 # Reset The Projection Matrix.                   
    gluPerspective(45.0, float(Width)/float(Height), 0.1, 100.0) # Aspect ratio. Make window resizable. 
    glMatrixMode(GL_MODELVIEW) 
    
#============================================================== 
def make_cube_1(texture, texture_index): 
        """   A generic cube. A texture binding created with glBindTexture remains active until a different 
                texture is bound to the same target, or until the bound texture is deleted with glDeleteTextures.      
        """ 
        glBindTexture(GL_TEXTURE_2D,texture[texture_index])	 
        # Front Face (Each texture's corner is matched a quad's corner.) 
        glBegin(GL_QUADS)	 
	glTexCoord2f(0.0, 0.0); glVertex3f(-1.0, -1.0,  1.0)	# Bottom Left of The Texture and Quad 
	glTexCoord2f(1.0, 0.0); glVertex3f( 1.0, -1.0,  1.0)	# Bottom Right of The Texture and Quad 
	glTexCoord2f(1.0, 1.0); glVertex3f( 1.0,  1.0,  1.0)	              # Top Right of The Texture and Quad 
	glTexCoord2f(0.0, 1.0); glVertex3f(-1.0,  1.0,  1.0)	# Top Left of The Texture and Quad	 
	glEnd(); 

        glBindTexture(GL_TEXTURE_2D,texture[texture_index+1])	 
	# Back Face 
	glBegin(GL_QUADS)			   
	glTexCoord2f(1.0, 0.0); glVertex3f(-1.0, -1.0, -1.0)	# Bottom Right 
	glTexCoord2f(1.0, 1.0); glVertex3f(-1.0,  1.0, -1.0)	# Top Rightn
	glTexCoord2f(0.0, 1.0); glVertex3f( 1.0,  1.0, -1.0)	# Top Left 
	glTexCoord2f(0.0, 0.0); glVertex3f( 1.0, -1.0, -1.0)	# Bottom Left 
	glEnd() 
       
        glBindTexture(GL_TEXTURE_2D,texture[texture_index+2])	 
	# Top Face 
	glBegin(GL_QUADS)			    
	glTexCoord2f(0.0, 1.0); glVertex3f(-1.0,  1.0, -1.0)	# Top Left 
	glTexCoord2f(0.0, 0.0); glVertex3f(-1.0,  1.0,  1.0)             # Bottom Left 
	glTexCoord2f(1.0, 0.0); glVertex3f( 1.0,  1.0,  1.0)	             # Bottom Right 
	glTexCoord2f(1.0, 1.0); glVertex3f( 1.0,  1.0, -1.0)	# Top Right 
        glEnd();				 
       
        glBindTexture(GL_TEXTURE_2D,texture[texture_index+3])	 
        # Bottom Face 
	glBegin(GL_QUADS)			    
	glTexCoord2f(1.0, 1.0); glVertex3f(-1.0, -1.0, -1.0)	# Top Right 
	glTexCoord2f(0.0, 1.0); glVertex3f( 1.0, -1.0, -1.0)	# Top Left 
	glTexCoord2f(0.0, 0.0); glVertex3f( 1.0, -1.0,  1.0)	# Bottom Left 
	glTexCoord2f(1.0, 0.0); glVertex3f(-1.0, -1.0,  1.0)	# Bottom Right 
	glEnd(); 
        
        glBindTexture(GL_TEXTURE_2D,texture[texture_index+4])	 
	# Right face 
	glBegin(GL_QUADS)			   
	glTexCoord2f(1.0, 0.0); glVertex3f( 1.0, -1.0, -1.0)	# Bottom Right 
	glTexCoord2f(1.0, 1.0); glVertex3f( 1.0,  1.0, -1.0)	# Top Right 
	glTexCoord2f(0.0, 1.0); glVertex3f( 1.0,  1.0,  1.0)	              # Top Left
	glTexCoord2f(0.0, 0.0); glVertex3f( 1.0, -1.0,  1.0)	# Bottom Left
	glEnd(); 
        
        glBindTexture(GL_TEXTURE_2D,texture[texture_index+5])	 
	# Left Face 
	glBegin(GL_QUADS)			    
	glTexCoord2f(0.0, 0.0); glVertex3f(-1.0, -1.0, -1.0)	# Bottom Left
	glTexCoord2f(1.0, 0.0); glVertex3f(-1.0, -1.0,  1.0)	# Bottom Right 
	glTexCoord2f(1.0, 1.0); glVertex3f(-1.0,  1.0,  1.0)	# Top Right 
	glTexCoord2f(0.0, 1.0); glVertex3f(-1.0,  1.0, -1.0)	# Top Left 
        glEnd();				  


def DrawFrontFace(): 
        """   A texture binding created with glBindTexture remains active until a different texture 
              is bound to the same target, or until the bound texture is deleted with glDeleteTextures.      
        """ 
	global xrot1, yrot1, zrot1, xrot2, yrot2, zrot2 
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # Clear the screen and Depth buffer 

        # First textured cube. 
	glLoadIdentity()					# Reset The View 
	glTranslatef(-2.0,0.0,-5.0)			# Shift cube left and back. 
	glRotatef(xrot1,1.0,0.0,0.0)			# Rotate the cube on It's X axis. 
	glRotatef(yrot1,0.0,1.0,0.0)			# Rotate the cube on It's Y axis. 
	glRotatef(zrot1,0.0,0.0,0.0)			# Rotate the cube on It's Z axis. 
            make_cube_1(texture_1, 0)  # "0" is the first index no. of a six member sequence - images.        
	xrot1  = xrot1 + 0.2                # X rotation of first cube. 
	yrot1 = yrot1 - 0.1                 # Y rotation 
	zrot1 = zrot1 + 0.1                 # Z rotation 
  
        # Second textured cube. 
	glLoadIdentity()					# Reset The view 
	glTranslatef(1.5,0.0,-5.0)			             # Shift cube right and back. 
	glRotatef(xrot2,1.0,0.0,0.0)			# Rotate the cube on It's X axis. 
	glRotatef(yrot2,0.0,1.0,0.0)			# Rotate the cube on It's Y axis. 
	glRotatef(zrot2,0.0,0.0,0.0)			# Rotate the cube on It's Z axis 
        make_cube_1(texture_1, 6)  # "6" is the first index no. of a different six member sequence - images. 
	xrot2  = xrot2 - 0.1                 # X rotation of second cube. 
	yrot2 = yrot2 + 0.2                 # Y rotation 
	zrot2 = zrot2 + 0.4                 # Z rotation 

	glutSwapBuffers() 
#=================================================================
def main(): 
  glutInit("") 
  glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH) 
  glutInitWindowSize(1000, 480) 
  window = glutCreateWindow("Textured rotating cubes") 
  LoadTextures()   
  glutDisplayFunc(DrawFrontFace) 
  glutIdleFunc(DrawFrontFace)             # When we are doing nothing, redraw the scene. 
  InitGL(1000, 480)                               # Initialize our window. 
  glutMainLoop()                                   # Start the event processing engine  

main()
