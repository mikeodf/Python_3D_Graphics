"""  ch11 No.2 
Program name: opengl_dogsworld_vertex_arrays_1.py 
Objective: Assemble and move a miniature world made of several objects. 
 
Keywords: OpenGL, triangle, objects, world model, normals, lighting. 
============================================================================79 
From the book "Python Graphics for Games: Working in 3 Dimensions"

Tested on: Python 2.6, Python 2.7.3, Python 3.2.3       
Author:  Mike Ohlson de Fine 
================================ 
""" 
from OpenGL.GL import * 
from OpenGL.GLUT import * 
from OpenGL.GLU import * 
import vector_2d3d_ops 
#==================================================== 
# Lighting parameters. -  the value of the fourth parameter is immaterial for diffuse light. 
diffuse_lite_kula_white   = [1.0, 1.0, 1.0, 0.0] 
light0_position   = [  5.0, 1.0, 5.0, 0.0 ] 
#==================================================== 
# Model (world) rotation variables. 
rotate_angle_y = 0.0 
rotate_angle_x = 0.0 
#====================================================== 
# Objects in the world. Determine how many triangles and create normals. 
dog3_faces = len(dog3)/3  
print 'len dog3:', dog3_faces 
dog3_norm = vector_2d3d_ops.array_triangle_normals(dog3) 

kennelroof3_faces = len(kennelroof3)/3  
print 'len kennelroof3:', kennelroof3_faces 
kennelroof3_norm = vector_2d3d_ops.array_triangle_normals(kennelroof3) 

kennelwalls3_faces = len(kennelwalls3)/3 
print 'len kennelwalls3:', kennelwalls3_faces 
kennelwalls3_norm = vector_2d3d_ops.array_triangle_normals(kennelwalls3) 

treetop3_faces = len(treetop3)/3  
print 'len treetop3:' ,treetop3_faces 
treetop3_norm = vector_2d3d_ops.array_triangle_normals(treetop3) 

backwall3_faces = len(backwall3)/3  
print 'len backwall3:' ,backwall3_faces 
backwall3_norm = vector_2d3d_ops.array_triangle_normals(backwall3) 

floor3_faces = len(floor3)/3  
print 'len floor3:' ,floor3_faces 
floor3_norm = vector_2d3d_ops.array_triangle_normals(floor3) 
#============================================================== 
def InitGL(Width, Height): 
        """ Initialize and setup the Graphics Software/Hardware pipeline. 
        """ 
        glClearColor(0.0, 0.0, 0.0, 0.0) 
        # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ 
        # The 6 lines below create the lighting (from a single light "LIGHT0") in the model scene. 
        glEnable(GL_NORMALIZE) 
        glEnable(GL_COLOR_MATERIAL) 
        glEnable(GL_LIGHTING) 

        glEnable(GL_LIGHT0) 
        glLightfv(GL_LIGHT0, GL_POSITION, light0_position) 
        glLightfv(GL_LIGHT0, GL_DIFFUSE,   diffuse_lite_kula_white) 
        #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ 
        glEnable(GL_DEPTH_TEST) 
        glMatrixMode(GL_PROJECTION) 
        glLoadIdentity() 
        gluPerspective(45.0, float(Width)/float(Height), 0.1, 100.0) 
        glMatrixMode(GL_MODELVIEW) 

def DrawDogsWorld(): 
        """ Dog's World is composed of a floor with a sunrise mural backdrop. 
            within it a dog, his house and a fir tree. The whole world rotates 
            as a unit - as if it were on the surface of a planet. 
        """ 
        global rotate_angle_x, rotate_angle_y 
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) 

        # Control of the Model Coordinates (Dog's World Coordinates) 
        # - the following 5 instructions: 
        glLoadIdentity() 
        glTranslatef(0.5,0.4,-6.0) 
        glRotatef(90.0, 1.0, 0.0, 0.0)    
        glRotatef(rotate_angle_y,  0.0, 0.0, 1.0) 
        glRotatef(rotate_angle_x,  1.0, 0.0, 0.0) 

        # Turn-on the vertex array processing   
        glEnableClientState(GL_VERTEX_ARRAY)     
        glEnableClientState(GL_NORMAL_ARRAY)  
        
        # 1 - Sunrise_rays 
        glColor3f(1.0, 1.0, 0.1)                    # Yellow           
        glVertexPointer(3, GL_FLOAT, 0, backwall3)     
        glNormalPointer(GL_FLOAT, 0, backwall3_norm)   
        glDrawArrays(GL_TRIANGLES, 0, 24) 
        
        # 2 - Grass_floor 
        glColor3f(0.4, 0.6, 0.1)                    # Green          
        glVertexPointer(3, GL_FLOAT, 0, floor3)     
        #glNormalPointer(GL_FLOAT, 0, floor3_norm)   
        glNormalPointer(GL_FLOAT, 0, floor3)  
        glDrawArrays(GL_TRIANGLES, 0, 6) 

        # 3 -  Dog 
        glRotatef(-90.0, 1.0, 0.0, 0.0)    
        glTranslatef(0.5, -0.4, 1.8) 
        glScale(0.6,  0.6,  0.6) 
        glColor3f(0.8, 0.1, 0.1)                     # Brown      
        glVertexPointer(3, GL_FLOAT, 0, dog3)     
        glNormalPointer(GL_FLOAT, 0, dog3) 
        #glNormalPointer(GL_FLOAT, 0, dog3_norm)  
        glDrawArrays(GL_TRIANGLES, 0, 33) 
        
        # 4 – Kennel roof  
        glTranslatef(0.0, -0.1, -1.6) 
        glScale(1.0,  1.0,  1.0) 
        glColor3f(0.5, 0.5, 1.0)                    # Blue       
        glVertexPointer(3, GL_FLOAT, 0, kennelroof3)     
        glNormalPointer(GL_FLOAT, 0, kennelroof3)   
        #glNormalPointer(GL_FLOAT, 0, kennelroof3_norm)   
        glDrawArrays(GL_TRIANGLES, 0, 12)  
        
        # 5 – kennel walls  
        glColor3f(0.8, 0.8, 0.8)                     # White    
        glVertexPointer(3, GL_FLOAT, 0, kennelwalls3)     
        glNormalPointer(GL_FLOAT, 0, kennelwalls3)  
        #glNormalPointer(GL_FLOAT, 0, kennelwalls3_norm)  
        glDrawArrays(GL_TRIANGLES, 0, 18)  
         
        # 6 - Treetop (foliage) 
        glTranslatef(-2.1, 0.5, 1.0) 
        glScale(2.0,  2.0,  2.0) 
        glColor3f(0.0, 1.0, 0.1)                    # Green            
        glVertexPointer(3, GL_FLOAT, 0, treetop3)     
        glNormalPointer(GL_FLOAT, 0, treetop3)  
        #glNormalPointer(GL_FLOAT, 0, treetop3_norm)   
        glDrawArrays(GL_TRIANGLES, 0, 18) 
        
        # 7 - Tree-trunk (similar shape to foliage) 
        glColor3f(0.9, 0.3, 0.3)                    # Brown 
        glTranslatef(0.0, -0.75, 0.0)  
        glScale(0.2,  1.0,  0.2)  
        glVertexPointer(3, GL_FLOAT, 0, treetop3)     
        glNormalPointer(GL_FLOAT, 0, treetop3)   
        #glNormalPointer(GL_FLOAT, 0, treetop3_norm)   
        glDrawArrays(GL_TRIANGLES, 0, 18) 
        
        # Turn-off the Vertex Array processing.  
        glDisableClientState(GL_VERTEX_ARRAY)       
        glDisableClientState(GL_NORMAL_ARRAY)        
               
        rotate_angle_y += 0.05    # Rotation of the model world. 
        rotate_angle_x += 0.001 
        glutSwapBuffers() 
        

def main(): 
        ''' Main Program. 
        '''    
        glutInit(sys.argv) 
        glutInitWindowSize(1000,1000)    # W,H. Line gets scaled to the window. 
        glutCreateWindow('Draw DogsWorld using OpenGL Vertex Arrays. Normals enabled') 
        InitGL(1000, 1000) 
        glutIdleFunc(DrawDogsWorld)      # When we are doing nothing, redraw the scene. 
        glutMainLoop() 

main()
