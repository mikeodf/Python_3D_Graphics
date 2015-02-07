"""  ch11 No.6 
Program name: opengl_3D_clenching_hand.py 
Objective: Construct a set of falanges that clench and unclench. 
 
Keywords: OpenGL, triangle, sphere, octets, separate, normals, lighting. 
============================================================================79 
From the book "Python Graphics for Games: Working in 3 Dimensions"

Comments: Each bone of each finger is constructed using the capped beam
and movements are coordinated relative to the bones closest to the wrist. 

Tested on: Python 2.6, Python 2.7.3, Python 3.2.3       
Author:  Mike Ohlson de Fine 
================================ 
"""
# Hand Clenching - unclenching function.
def all_displays(): 
    '''  A  Five Fingered hand that clenches and unclenches while simultaneously rotating around the wrist.
    ''' 
    global shift_1, shift_2, shift_3, shift_4, shift_5 
    global rotate_angle_1, rotate_axis_1, rotation_speed_1 
    global rotate_angle_2, rotation_speed_2,  rotate_angle_3, rotation_speed_3 

    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT) # Clear the colour and depth buffer       
    glEnableClientState(GL_VERTEX_ARRAY) 
    glEnableClientState(GL_NORMAL_ARRAY) 


    #=========================================================== 
    # First Finger 
    #=========================================================== 
    glLoadIdentity()                                                          # Clear matrix stack 
    glTranslate( shift_1[0], shift_1[1], shift_1[2])            # Each object's origin. 
    glRotate(rotate_angle_3, 0.0, 1.0, 0.0)                        # Common rotation around wrist (y-axis).   
    glScale(0.91, 0.91, 0.91)                                        # Relative size of each finger (wrt longest finger). 
    glScale(3.0, 3.0, 3.0)                                              # Overall amplification applied to all fingers. 
    #glColor(0.5, 0.5,  0.5)  
  
    # Bone_1 
    glColor(0.8, 0.0,  0.0)  
    for i in range(0,len(bone_1)):               
        glVertexPointer(3, GL_FLOAT, 0, bone_1[i]) 
        glNormalPointer(GL_FLOAT, 0, bone_1[i])    #Arguments:  (type, stride, pointer). 
        glDrawArrays(GL_TRIANGLES, 0, 4 ) # 16 = number of triangles. 
    
    # Bone_2 
    glTranslate(0.0, 1.0, 0.0)                                 # Each object's origin. 
    glRotate(rotate_angle_2, 1.0, 0.0, 0.0)           # Rotate joint relative to previous - an additive process. 
    glColor(0.0, 0.0,  0.8)  
    for i in range(0,len(bone_1)):                
        glVertexPointer(3, GL_FLOAT, 0, bone_2[i]) 
        glNormalPointer(GL_FLOAT, 0, bone_2[i])           #Arguments:  (type, stride, pointer). 
        glDrawArrays(GL_TRIANGLES, 0, 4 )                 # 16 = number of triangles. 

    # Bbone_3 
    glTranslate(0.0, 0.75, 0.0)                              # Each object's origin. 
    glRotate(rotate_angle_2, 1.0, 0.0, 0.0)           # Rotate joint relative to previous. 
    glColor(0.0, 0.8,  0.0)  
    for i in range(0,len(bone_1)):                
        glVertexPointer(3, GL_FLOAT, 0, bone_3[i]) 
        glNormalPointer(GL_FLOAT, 0, bone_3[i])           # Arguments:  (type, stride, pointer). 
        glDrawArrays(GL_TRIANGLES, 0, 4 )                  # 16 = number of triangles. 

    # Bone_4 
    glTranslate(0.0, 0.40, 0.0)                               # Each object's origin. 
    glRotate(rotate_angle_2, 1.0, 0.0, 0.0)           #Rotate joint relative to previous. 
    glColor(0.6, 0.0,  0.6)  
    for i in range(0,len(bone_1)):               
        glVertexPointer(3, GL_FLOAT, 0, bone_4[i]) 
        glNormalPointer(GL_FLOAT, 0, bone_4[i])         # Arguments:  (type, stride, pointer). 
        glDrawArrays(GL_TRIANGLES, 0, 4 )               # 16 = number of triangles. 

    
    #=========================================================== 
    # Second Finger 
    #=========================================================== 
    glLoadIdentity()                                          # Clear matrix stack and start afresh. 
    glTranslate(0.0, 0.0, shift_2[2])                  # Each object's origin. 
    glRotate(rotate_angle_3, 0.0, 1.0, 0.0)       # common rotation around wrist (y-axis). 
    glTranslate(shift_2[0],shift_2[1], 0.0) 
    glRotate(-3.0, 0.0,  0.0, 1.0)                       # Splay the finger slightly  - 3 degrees. 
    glScale(3.0, 3.0, 3.0)                                  # Overall amplification applied to all fingers. 

    glColor(0.8, 0.0,  0.0)  
    # bone_1 
    for i in range(0,len(bone_1)):              
        glVertexPointer(3, GL_FLOAT, 0, bone_1[i]) 
        glNormalPointer(GL_FLOAT, 0, bone_1[i])    #Arguments:  (type, stride, pointer). 
        glDrawArrays(GL_TRIANGLES, 0, 4 ) # 16 = number of triangles. 
    
    # bone_2 
    glTranslate(0.0, 1.0, 0.0)                                 # Each object's origin. 
    glRotate(rotate_angle_2, 1.0, 0.0, 0.0)           # rotate joint relative to previous. 
    glColor(0.0, 0.0,  0.8)  
    for i in range(0,len(bone_1)):               
        glVertexPointer(3, GL_FLOAT, 0, bone_2[i]) 
        glNormalPointer(GL_FLOAT, 0, bone_2[i])    
        glDrawArrays(GL_TRIANGLES, 0, 4 ) 

    # bone_3 
    glTranslate(0.0, 0.75, 0.0)                               # Each object's origin. 
    glRotate(rotate_angle_2, 1.0, 0.0, 0.0)           # Rotate joint relative to previous. 
    glColor(0.0, 0.8,  0.0)  
    for i in range(0,len(bone_1)):               
        glVertexPointer(3, GL_FLOAT, 0, bone_3[i]) 
        glNormalPointer(GL_FLOAT, 0, bone_3[i])    
        glDrawArrays(GL_TRIANGLES, 0, 4 ) 

    # bone_4 
    glTranslate(0.0, 0.40, 0.0)                               # Each object's origin. 
    glRotate(rotate_angle_2, 1.0, 0.0, 0.0)           # rotate joint relative to previous. 
    glColor(0.6, 0.0,  0.6)  
    for i in range(0,len(bone_1)):              
        glVertexPointer(3, GL_FLOAT, 0, bone_4[i]) 
        glNormalPointer(GL_FLOAT, 0, bone_4[i])    

        glDrawArrays(GL_TRIANGLES, 0, 4 ) 
    
    #=========================================================== 
    # Third Finger 
    #=========================================================== 
    glLoadIdentity()                                       # Clear matrix stack 
    glTranslate(0.0, 0.0, shift_3[2])               # Each object's origin. 
    glRotate(rotate_angle_3, 0.0, 1.0, 0.0)                  # common rotation around wrist (y-axis). 
    glTranslate(shift_3[0],shift_3[1], 0.0) 
    glRotate(-6.0, 0.0,  0.0, 1.0)  # Splay the finger slightly. 
    glScale(3.0, 3.0, 3.0) 
    glScale(0.93, 0.93, 0.93) 
    
    # bone_1 
    glColor(0.8, 0.0,  0.0)  
    for i in range(0,len(bone_1)):               
        glVertexPointer(3, GL_FLOAT, 0, bone_1[i]) 
        glNormalPointer(GL_FLOAT, 0, bone_1[i])   
        glDrawArrays(GL_TRIANGLES, 0, 4 )
    
    # bone_2 
    glTranslate(0.0, 1.0, 0.0)              
    glRotate(rotate_angle_2, 1.0, 0.0, 0.0)          
    glColor(0.0, 0.0,  0.8)  
    for i in range(0,len(bone_1)):              
        glVertexPointer(3, GL_FLOAT, 0, bone_2[i]) 
        glNormalPointer(GL_FLOAT, 0, bone_2[i])   
        glDrawArrays(GL_TRIANGLES, 0, 4 ) 

    # bone_3 
    glTranslate(0.0, 0.75, 0.0)              
    glRotate(rotate_angle_2, 1.0, 0.0, 0.0)           
    glColor(0.0, 0.8,  0.0)  
    for i in range(0,len(bone_1)):               
        glVertexPointer(3, GL_FLOAT, 0, bone_3[i]) 
        glNormalPointer(GL_FLOAT, 0, bone_3[i])   
        glDrawArrays(GL_TRIANGLES, 0, 4 ) 

    # bone_4 
    glTranslate(0.0, 0.40, 0.0)              
    glRotate(rotate_angle_2, 1.0, 0.0, 0.0)           
    glColor(0.6, 0.0,  0.6)  
    for i in range(0,len(bone_1)):                
        glVertexPointer(3, GL_FLOAT, 0, bone_4[i]) 
        glNormalPointer(GL_FLOAT, 0, bone_4[i])    
        glDrawArrays(GL_TRIANGLES, 0, 4 )
    
    #=========================================================== 
    # Fourth Finger 
    #=========================================================== 
    glLoadIdentity()         
    glTranslate(0.0, 0.0, shift_4[2])             
    glRotate(rotate_angle_3, 0.0, 1.0, 0.0)                  
    glTranslate(shift_4[0],shift_4[1], 0.0) 
    glRotate(-9.0, 0.0,  0.0, 1.0)  
    glScale(3.0, 3.0, 3.0) 
    glScale(0.78, 0.78, 0.78) 

    # bone_1 
    glColor(0.8, 0.0,  0.0)  
    for i in range(0,len(bone_1)):               
        glVertexPointer(3, GL_FLOAT, 0, bone_1[i]) 
        glNormalPointer(GL_FLOAT, 0, bone_1[i])    
        glDrawArrays(GL_TRIANGLES, 0, 4 ) 
    
    # bone_2 
    glTranslate(0.0, 1.0, 0.0)               # Each object's origin. 
    glRotate(rotate_angle_2, 1.0, 0.0, 0.0)           # rotate joint relative to previous. 
    glColor(0.0, 0.0,  0.8)  
    for i in range(0,len(bone_1)):               
        glVertexPointer(3, GL_FLOAT, 0, bone_2[i]) 
        glNormalPointer(GL_FLOAT, 0, bone_2[i])   
        glDrawArrays(GL_TRIANGLES, 0, 4 ) 

    # bone_3 
    glTranslate(0.0, 0.75, 0.0)               
    glRotate(rotate_angle_2, 1.0, 0.0, 0.0)         
    glColor(0.0, 0.8,  0.0)  
    for i in range(0,len(bone_1)):                
        glVertexPointer(3, GL_FLOAT, 0, bone_3[i]) 
        glNormalPointer(GL_FLOAT, 0, bone_3[i])   
        glDrawArrays(GL_TRIANGLES, 0, 4 ) 

    # bone_4 
    glTranslate(0.0, 0.40, 0.0)              
    glRotate(rotate_angle_2, 1.0, 0.0, 0.0)       
    glColor(0.6, 0.0,  0.6)  
    for i in range(0,len(bone_1)):                 
        glVertexPointer(3, GL_FLOAT, 0, bone_4[i]) 
        glNormalPointer(GL_FLOAT, 0, bone_4[i])   
        glDrawArrays(GL_TRIANGLES, 0, 4 ) 

    #=========================================================== 
    # Thumb 
    #=========================================================== 
    glLoadIdentity()           
    glTranslate(0.0, 0.0, shift_5[2])              
    glRotate(rotate_angle_3, 0.0, 1.0, 0.0)                  
    glTranslate(shift_5[0],shift_5[1], 0.0) 
    glRotate(20.0, 0.0,  0.0, 1.0)                   # Splay the thumb by 30 degrees from the fingers. 
    glRotate(-30.0, 0.0,  1.0,  0.0)                 # Angle thumb toward palm (Rotate about y). 
    glScale(3.0, 3.0, 3.0) 
    glScale(0.78, 0.78, 0.78) 

    # bone_1 
    glColor(0.8, 0.0,  0.0)  
    for i in range(0,len(bone_1)):               
        glVertexPointer(3, GL_FLOAT, 0, bone_1[i]) 
        glNormalPointer(GL_FLOAT, 0, bone_1[i])    
        glDrawArrays(GL_TRIANGLES, 0, 4 ) 
    
    # bone_2 
    glTranslate(0.0, 1.0, 0.0)              
    glRotate(rotate_angle_2, 1.0, 0.0, 0.0)           
    glColor(0.0, 0.0,  0.8)  
    for i in range(0,len(bone_1)):               
        glVertexPointer(3, GL_FLOAT, 0, bone_2[i]) 
        glNormalPointer(GL_FLOAT, 0, bone_2[i])   
        glDrawArrays(GL_TRIANGLES, 0, 4 ) 

    # bone_3 
    glTranslate(0.0, 0.75, 0.0)               
    glRotate(rotate_angle_2, 1.0, 0.0, 0.0)         
    glColor(0.0, 0.8,  0.0)  
    for i in range(0,len(bone_1)):                
        glVertexPointer(3, GL_FLOAT, 0, bone_3[i]) 
        glNormalPointer(GL_FLOAT, 0, bone_3[i])    
        glDrawArrays(GL_TRIANGLES, 0, 4 ) 

    glDisableClientState(GL_VERTEX_ARRAY) 
    glDisableClientState(GL_NORMAL_ARRAY) 

    glFlush() # Makes sure that we output the model to the graphics card 
    glutSwapBuffers() 
    glutPostRedisplay() 

    rotate_angle_1 += rotation_speed_1 
    rotate_angle_3 += rotation_speed_3 
    if rotate_angle_2 >= 90.0 or rotate_angle_2 <= -5.0 : rotation_speed_2 = - rotation_speed_2 
    rotate_angle_2 += rotation_speed_2
