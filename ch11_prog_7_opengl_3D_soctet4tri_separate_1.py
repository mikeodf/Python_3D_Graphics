"""  ch11 No.7 
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
# Draw Scene Code
def DrawGLScene(): 
        """ Test each primitive. For each primitive to be tested, un-comment the relevant line. 
            Ensure all the others are commented out to keep the situation simple. 
        """ 
        global rot_grande       
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)         

        glEnableClientState(GL_VERTEX_ARRAY)        # Enable Vertex Array. 
        glEnableClientState(GL_NORMAL_ARRAY)       # Enable Normals Array. 

        # Final Transform. This needs to be applied to each dog, after the dog has been positiond correctly. 
        glLoadIdentity()                                         # Clear the Modelview stack .
        glTranslatef(0.0, -0.5,-8.0)                         # Shift entire model to a convenient view position. 
        glRotatef(rot_grande*3.0, 0.0, 1.0, 0.0);    # Continuous animated rotation of the whole model.
        glScale(3.0,  3.0,  2.0)                                # Scale-up x2 of the entire model, including dogs. 
       
        # Why are there 2 Pushes? 
        ''' There are three dogs that have to be placed on the same patch of earth, but in different positions. 
            Once in place they must each be operated of the same three transformations above. 
            So we preserve three "clean" copies. 
            As soon as each dog has been sized, rotated and translated into position, 
            the transformation matrix that was used must be discarded and replaced by the 'Final Transform' that 
            must be applied to each. 
            The unwanted transformations are deleted by each glPopMatrix() which happens after the dog has been positioned. 
        ''' 
        glPushMatrix()                                                      # Preserve the common patch transform. 
        glPushMatrix()                                                       # Preserve a second copy of the common patch. 
       
        # GROUND PATCH - No extra positioning transformations needed. 
        ''' Base floor vertex array - not to be altered. 
           The three dogs will be placed on this platform. 
        ''' 
        glEnableClientState(GL_COLOR_ARRAY)                 # Enable COLOR Array. 
        glColorPointer(4, GL_FLOAT, 0, kula)                          # (type, stride, pointer).  
        glVertexPointer(3, GL_FLOAT, 0, base_patch)              # (size, type, stride, pointer) .
        glNormalPointer(GL_FLOAT, 0, flat_base_norm)         # (type, stride, pointer). 
        glDrawArrays(GL_TRIANGLES, 0, 24)  # (primitive type, starting index, number of vertices to be rendered).    
        glDisableClientState(GL_COLOR_ARRAY)   

        # DOG 1 - Old Yaller 
        '''  tilt the dog up by 40 degrees, scale him down by 50%, shift him forward by 0.5. 
        ''' 
        glTranslatef(0.0, 0.52, 0.6)                # Shift the dog 1 up and forward. 
        glRotatef(-40.0, 0.0, 0.0, 1.0)            # Tilt the dog 1 to make it horizontal. 
        glScale(0.5,  0.5,  0.5)                        # Scale the yellow dog to 50% of full size. 
  
        glColor3f(0.8, 0.8, 0.1)                     # Yellow.       
        glVertexPointer(3, GL_FLOAT, 0, dog3_world.dog40tiltz) 
        glNormalPointer(GL_FLOAT, 0, dog40tiltz_norm)               
        glDrawArrays(GL_TRIANGLES, 0, 174)                            
.
        glPopMatrix()    # Pop No.1 
        # DOG 2 - Rufus 
        glTranslatef(0.0, 0.31, 0.0)                 # Shift the dog 2 up. 
        glRotatef(90.0, 0.0, 1.0, 0.0)              # Rotate the dog 2 to point down the z-axis. 
        glRotatef(-40.0, 0.0, 0.0, 1.0)             # Tilt the dog 2 to make it horizontal. 
        glScale(0.3,  0.3,  0.3)                         # Scale the yellow dog 2 to 30% of full size. 

        glColor3f(0.8, 0.2, 0.1)                        # Rufus coloring.       
        glVertexPointer(3, GL_FLOAT, 0, dog3_world.dog40tiltz)    
        glNormalPointer(GL_FLOAT, 0, dog40tiltz_norm)              
        glDrawArrays(GL_TRIANGLES, 0, 174)  
   
        
        glPopMatrix()    # Pop No.2 
        # DOG 3 - Bluey      
        glTranslatef(0.0, 0.21, -0.5)                # Shift the dog 3 up and back. 
        glRotatef(-90.0, 0.0, 1.0, 0.0);             # Rotate the dog 3 to face dog 2. 
        glRotatef(-40.0, 0.0, 0.0, 1.0);             # Tilt the dog 3 to make it horizontal. 
        glScale(0.3,  0.2,  0.3)                          # Scale the same as the red dog but with shorter legs. 
   
        glColor3f(0.3, 0.3, 0.8)                     # Blue.       
        glVertexPointer(3, GL_FLOAT, 0, dog3_world.dog40tiltz)      
        glNormalPointer(GL_FLOAT, 0, dog40tiltz_norm)              
        glDrawArrays(GL_TRIANGLES, 0, 174)  
        
        glDisableClientState(GL_VERTEX_ARRAY)          # disable the Vertex Array.   
        glDisableClientState(GL_NORMAL_ARRAY)        # disable the Normal Array.           
        rot_grande += 0.01 
        glutSwapBuffers() 
        

def main(): 
        glutInit(sys.argv) 
        glutInitWindowSize(1000,1000)   
        glutCreateWindow('OpenGL: Three dog family model.') 
        InitGL(1000, 1000) 
        glutIdleFunc(DrawGLScene)     
        glutMainLoop() 
main() 
