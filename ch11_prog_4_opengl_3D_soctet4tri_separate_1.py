"""  ch11 No.4 
Program name: opengl_3D_soctet4tri_separate_1.py 
Objective: Construct an enclosed solid from an one-eighth segment using symmetry. 
 
Keywords: OpenGL, triangle, sphere, octets, separate, normals, lighting. 
============================================================================79 
From the book "Python Graphics for Games: Working in 3 Dimensions"

Comments: Each octet-sector is derived from the same vertex array and
is positioned, scaled and rotated independently from the others. 

Tested on: Python 2.6, Python 2.7.3, Python 3.2.3       
Author:  Mike Ohlson de Fine 
================================ 
"""
# To get this to work with python3.x 
import sys 
sys.path.append("/usr/local/lib/python2.7/dist-packages/PyOpenGL-3.1.0-py2.7.egg/")  
from OpenGL.GL import * 
from OpenGL.GLUT import * 
from OpenGL.GLU import * 
import vector_2d3d_ops 

rotation_y = 0.0 
rotation_x = 0.0 

octet4tri =  [ 
-0.0, 0.7, 0.7,    -0.0, 1.0, 0.0,    -0.7, 0.7, 0.0,  # 1st triangle 
-0.7, 0.0, 0.7,    -0.0, 0.7, 0.7,    -0.7, 0.7, 0.0,  # 2nd triangle 
-0.0, 0.7, 0.7,    -0.7, 0.0, 0.7,    -0.0, 0.0, 1.0,  # 3rd triangle 
-1.0, 0.0, 0.0,    -0.7, 0.0, 0.7,    -0.7, 0.7, 0.0 ] # 4th triangle 

#==================================================== 
octet4tri_faces = len(octet4tri)/3  
print 'octet4tri_faces: ', octet4tri_faces 
octet4tri_norm =vector_2d3d_ops. array_triangle_normals(octet4tri) 
#====================================================
def InitGL(Width, Height): 
        """ Initialize and setup the Graphics Software/Hardware pipeline. 
        """ 
        # Note -  the value of the fourth parameter is immaterial for diffuse light. 
        diffuse_lite_kula_white   = [1.0, 1.0, 1.0, 0.0] 
        light0_position   = [  5.0, 1.0, 5.0, 0.0 ] 
        glClearColor(0.6, 0.6, 1.0, 0.0) 
        # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ 
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

def Octocapsule(): 
        """ Draw an enclose eight segmented solid by suitably rotating the 
            same segment into position using matrix operations.
        """ 
        global rotation_y, rotation_x 
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) 

        # Enable vertex arrays 
        glEnableClientState(GL_VERTEX_ARRAY)        
        glEnableClientState(GL_NORMAL_ARRAY) 
        
        # 1 first octant of Vertex arrays  
        glLoadIdentity() 
        glTranslatef(0.0,  0.4,  -5.0) 
        glRotatef(rotation_y, 0.0, 1.0, 0.0)          
        glScale(1.0,  1.0,  1.0) 
        glColor3f(1.0, 0.0, 0.0)                     # Red              
        glVertexPointer(3, GL_FLOAT, 0, octet4tri)             # (size, type, stride, pointer) .
        glNormalPointer(GL_FLOAT, 0, octet4tri_norm)    # (type, stride, pointer). 
        glDrawArrays(GL_TRIANGLES, 0, 12)  # (primitive type, starting index, number of indices (vertices?) to be rendered). 
              
        # 2 -  second octant 
        glLoadIdentity() 
        glTranslatef(-0.0,  0.4,  -5.0) 
        glRotatef(rotation_y, 0.0, 1.0, 0.0)  
        glRotatef(90.0, 0.0, 1.0, 0.0)   
        glScale(1.0,  1.0,  1.0)  
        glColor3f(0.0, 0.0, 1.0)                     # Blue                             
        glVertexPointer(3, GL_FLOAT, 0, octet4tri)     
        glNormalPointer(GL_FLOAT, 0, octet4tri_norm)    
        glDrawArrays(GL_TRIANGLES, 0, 12)  
        
        # 3 -  third octant 
        glLoadIdentity() 
        glTranslatef(-0.0,  0.4,  -5.0) 
        glRotatef(rotation_y, 0.0, 1.0, 0.0) 
        glRotatef(180.0, 0.0, 1.0, 0.0)           
        glScale(1.0,  1.0,  1.0)   
        glColor3f(1.0, 0.0, 1.0)                     # Purple                              
        glVertexPointer(3, GL_FLOAT, 0, octet4tri)     
        glNormalPointer(GL_FLOAT, 0, octet4tri_norm)    
        glDrawArrays(GL_TRIANGLES, 0, 12) 
        
        # 4 -  fourth octant 
        glLoadIdentity() 
        glTranslatef(-0.0,  0.4,  -5.0) 
        glRotatef(rotation_y, 0.0, 1.0, 0.0) 
        glRotatef(-90.0, 0.0, 1.0, 0.0) 
        glScale(1.0,  1.0,  1.0)      
        glColor3f(0.0, 1.0, 0.0)                     # Green                              
        glVertexPointer(3, GL_FLOAT, 0, octet4tri)     
        glNormalPointer(GL_FLOAT, 0, octet4tri_norm)   
        glDrawArrays(GL_TRIANGLES, 0, 12)  
                
        # 5 -  fifth octant  
        glLoadIdentity() 
        glTranslatef(-0.0,  0.4,  -5.0) 
        glRotatef(rotation_y, 0.0, 1.0, 0.0) 
        glRotatef(90.0, 0.0, 1.0, 0.0) 
        glRotatef(-180.0, 0.0, 0.0, 1.0) 
        glScale(1.0,  1.0,  1.0)         
        glColor3f(0.0, 1.0, 1.0)                     # Lilac                            
        glVertexPointer(3, GL_FLOAT, 0, octet4tri)    
        glNormalPointer(GL_FLOAT, 0, octet4tri_norm)   
        glDrawArrays(GL_TRIANGLES, 0, 12)     
           
        # 6 -  sixth octant  
        glLoadIdentity() 
        glTranslatef(-0.0,  0.4,  -5.0) 
        glRotatef(rotation_y, 0.0, 1.0, 0.0) 
        glRotatef(180.0, 0.0, 1.0, 0.0) 
        glRotatef(-180.0, 0.0, 0.0, 1.0) 
        glScale(1.0,  1.0,  1.0)                 
        glColor3f(1.0, 1.0, 0.0)                     # Yellow                           
        glVertexPointer(3, GL_FLOAT, 0, octet4tri)   
        glNormalPointer(GL_FLOAT, 0, octet4tri_norm)   
        glDrawArrays(GL_TRIANGLES, 0, 12)  
        
        # 7 -  seventh octant 
        glLoadIdentity() 
        glTranslatef(-0.0,  0.4,  -5.0) 
        glRotatef(rotation_y, 0.0, 1.0, 0.0)  
        glRotatef(-180.0, 0.0, 0.0, 1.0) 
        glScale(1.0,  1.0,  1.0) 
        glRotatef(-270.0, 0.0, 1.0, 0.0) 
        glColor3f(1.0, 0.6, 0.0)                     # Orange                            
        glVertexPointer(3, GL_FLOAT, 0, octet4tri)    
        glNormalPointer(GL_FLOAT, 0, octet4tri_norm)    
        glDrawArrays(GL_TRIANGLES, 0, 12)  
                
        # 8 -  eigth octant 
        glLoadIdentity() 
        glTranslatef(-0.0,  0.4,  -5.0) 
        glRotatef(rotation_y, 0.0, 1.0, 0.0) 
        glRotatef(-180.0, 0.0, 0.0, 1.0)    
        glScale(1.0,  1.0,  1.0)   
        glColor3f(1.0, 1.0, 1.0)                        # Grey-white                        
        glVertexPointer(3, GL_FLOAT, 0, octet4tri)     
        glNormalPointer(GL_FLOAT, 0, octet4tri_norm)   
        glDrawArrays(GL_TRIANGLES, 0, 12)  
              
        # Disable vertex arrays. 
        glDisableClientState(GL_VERTEX_ARRAY)       
        glDisableClientState(GL_NORMAL_ARRAY) 
        
        rotation_y += 0.1  
        rotation_x += 0.05 
        glutSwapBuffers() 
        
        
def main(): 
        ''' Main Program. 
        '''    
        glutInit(sys.argv) 
        glutInitWindowSize(600,600)    # Width, Height. Line gets scaled to the window. 
        glutCreateWindow('OpenGL Vertex Arrays from Primitive Triangles: PsuedoSphere. 144 vertices') 
        InitGL(600, 600) 
        glutIdleFunc(Octocapsule)      # During idle time redraw the frame. 
        glutMainLoop() 

main()
