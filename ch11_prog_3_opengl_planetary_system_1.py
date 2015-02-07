"""  ch11 No.3
Program name: opengl_planetary_system_1.py 
Objective: Construct a simplified solar system with moon and spacecraft. 
 
Keywords: OpenGL, triangle, normals, lighting, sun, planets, orbits. 
============================================================================79 
From the book "Python Graphics for Games: Working in 3 Dimensions"

Comments: Control of multiple orbiting bodies, spinning independently. 

Tested on: Python 2.7.3, Python 3.2.3       
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
import itertools 
import math 
import copy 

cube_triangles_1 =  [1.0, 1.0, -1.0, 1.0, 1.0, 1.0, -1.0, 1.0, 1.0, -1.0, 1.0, -1.0, 1.0, 1.0, -1., -1.0, 1.0, 1.0, -1.0, -1.0, 1.0, -1.0, 1.0, -1.0, -1.0, 1.0, 1.0, -1.0, 1.0, -1.0, -1.0, -1.0, 1.0, -1.0, -1.0, -1.0, 1.0, -1.0, 1.0, -1.0, -1.0, 1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, 1.0, -1.0, -1.0, 1.0, -1.0, 1.0, 1.0, -1.0, 1.0, -1.0, -1.0, 1.0, -1.0, 1.0, 1.0, -1.0, 1.0, 1.0, 1., 1.0, 1.0, 1.0, -1.0, 1.0, -1.0, -1.0, -1.0, 1.0, -1.0, -1.0, 1.0, 1.0, -1.0, 1.0, 1.0, -1.0, -1.0, 1.0, -1.0, -1.0, -1.0, -1.0, 1.0, -1.0, -1.0, 1.0, 1.0, -1.0, 1.0, 1.0, 1.0, 1., 1.0, 1.0, 1.0, -1.0, 1.0, 1.0, -1.0, -1.0] 

rotation_orbit = 0.0 
rotation_spin = 0.0 
#==================================================== 
# Note -  the value of the fourth parameter is immaterial for diffuse light. 
diffuse_lite_kula_white   = [1.0, 1.0, 1.0, 0.0] 
light0_position   = [  5.0, 1.0, 5.0, 0.0 ] 
yellow_k    =  [ 1.0 ,1.0, 0.0] 
blue_k      =  [ 0.0 ,0.0, 1.0] 
moon_blue_k =  [ 0.4 ,0.4, 1.0] 
red_k       =  [ 1.0 ,0.4, 0.4] 
green_k     =  [ 0.4, 1.0, 0.4] 

def unit_normals(p,q,r): 
    """  Compute the vector cross-product of vectors drawn between three points. 
         Three points are given by their position vectors p, q, and r. 
         Compute the vector cross product from three vertices of a triangle. 
         The result returned: The position vector of the unit normal 
         to the plane containing the three points given. 
    """ 
    vx1 = p[0] - r[0]  # x1 - x3. 
    vy1 = p[1] - r[1]  # y1 - y3. 
    vz1 = p[2] - r[2]  # z1 - z3. 

    vx2 = q[0] - r[0]  # x2 - x3. 
    vy2 = q[1] - r[1]  # y2 - y3. 
    vz2 = q[2] - r[2]  # z2 - z3.   

    vnx = vy1*vz2 - vz1*vy2 
    vny = vz1*vx2 - vx1*vz2 
    vnz = vx1*vy2 - vy1*vx2 

    len_vn = math.sqrt(vnx*vnx + vny*vny + vnz*vnz) 
    if len_vn == 0: 
        vnx = 0 
        vny = 0 
        vnz = 0 
    else: 
        vnx = vnx/len_vn 
        vny = vny/len_vn 
        vnz = vnz/len_vn 
    return vnx, vny, vnz 

def array_triangle_normals(vertex_array): 
    """ Calculate the vertex normal for each face, repeat it three times to furnish a Normal for each 
        vertex of the triangle in the vertex array. The output is the target glNormaArray.       
    """ 
    norm_array = [] 
    for i in range (0, len(vertex_array), 9): # Number of triangles 
       # Each sequence of 9 floats from vertex_array supplies three vertices v1, v2, v3 
       a1 = vertex_array[i]          # first vertex. 
       a2 = vertex_array[i+1] 
       a3 = vertex_array[i+2] 
       v1 = [ a1,a2,a3] 

       b1 = vertex_array[i+3]      # second vertex. 
       b2 = vertex_array[i+4] 
       b3 = vertex_array[i+5] 
       v2 = [ b1,b2,b3] 

       c1 = vertex_array[i+6]      # third vertex. 
       c2 = vertex_array[i+7] 
       c3 = vertex_array[i+8] 
       v3 = [ c1,c2,c3] 

       vec_norm = unit_normals(v1, v2, v3) 
       norm_array.append(vec_norm)                           # Set stride to 0 to match each face to a normal. 
       norm_array.append(vec_norm) 
       norm_array.append(vec_norm) 
    norm_array = list(itertools.chain(*norm_array))     # Ensure the array has been flattened. 

    return norm_array 

#====================================================== 
# Cube planet made of triangles. 36 faces. 
cube_triangles_1_faces = len(cube_triangles_1)/3  
print ('cube_triangles_1_faces: ', cube_triangles_1_faces) 
cube_triangles_1_norm = array_triangle_normals(cube_triangles_1) 
#======================================================== 
def InitGL(Width, Height): 
        """ Initialize and setup the Graphics Software/Hardware pipeline. 
        """ 
        glClearColor(1.0, 1.0, 1.0, 0.0) 
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

def draw_planet(num_vertices, vertex_array, norm_array, kula): 
        glColor3f(kula[0], kula[1], kula[2] )      
        glEnableClientState(GL_VERTEX_ARRAY)        
        glEnableClientState(GL_NORMAL_ARRAY)               
        glVertexPointer(3, GL_FLOAT, 0, vertex_array)       # (size, type, stride, pointer) 
        glNormalPointer(GL_FLOAT, 0, vertex_array)         # (type, stride, pointer). 
        glDrawArrays(GL_TRIANGLES, 0, num_vertices)  # (primitive type, starting index, number of indices (vertices?) to be rendered) 
              
        glColor3f(kula[0], kula[1], kula[2])                                        
        glVertexPointer(3, GL_FLOAT, 0, vertex_array)     
        glNormalPointer(GL_FLOAT, 0, norm_array)   
        glDrawArrays(GL_TRIANGLES, 0, num_vertices) 

        glDisableClientState(GL_VERTEX_ARRAY)       
        glDisableClientState(GL_NORMAL_ARRAY)  
       

def DrawGLScene(): 
        """ Test each primitive. For each primitive to be tested, un-comment the relevant line. 
            Ensure all the others are commented out to keep the situation simple. 
        """ 
        global rotation_orbit, rotation_spin 
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) 

        # Sun - 1 
        glLoadIdentity() 
        glTranslatef(0.0,  0.0,  -18.0)   
        glRotatef(-rotation_spin*20.0, 0.0, 0.0, 1.0)    
        glScale(1.0,  1.0,  1.0) 
        draw_planet(24, cube_triangles_1,cube_triangles_1, yellow_k)     
        
        # 2: Earth Cube. 
        glLoadIdentity() 
        glRotatef(rotation_orbit*16.0, 0.0, 0.0, 1.0)  # Orbital rotation. 
        glTranslatef(5.0,  0.0,  -18.0)    
        glRotatef(-rotation_spin*120.0, 0.0, 0.0, 1.0) # Axis spin.    
        glScale(0.5,  0.5,  0.5) 
        draw_planet(36, cube_triangles_1, cube_triangles_1, blue_k) 

        # 2.2: Moon Cube. note order of execution is 1st translate then rotate (counterintuitive to instruction order 
        #      This is because it is achieved through matrix multiplication. 
        glRotatef(rotation_orbit*64.0, 0.0, 0.0, 1.0) # Orbital rotation moon orbits earth 4 times per solar year. 
        glTranslatef(4.0,  0.0,  0.0)   
        #glRotatef() # Axis spin - same as earth -> earth always sees te same side of the moon.    
        glScale(0.5,  0.5,  0.5) 
        draw_planet(36, cube_triangles_1, cube_triangles_1, moon_blue_k) 

        # Lunar module 1 orbiting around the moon. 
        glRotatef(rotation_orbit*128.0, 0.0, 0.0, 1.0) 
        glTranslatef(2.5,  0.0,  0.0)      
        glScale(0.5,  0.5,  0.5) 
        draw_planet(36, cube_triangles_1, cube_triangles_1, red_k) 

        # Lunar module 2 on opposite side of the moon. 
        glTranslatef(-9.5,  0.0,  0.0) 
        glRotatef(180.0, 0.0, 0.0, 1.0)     
        glScale(0.8,  0.8,  0.8) 
        draw_planet(36, cube_triangles_1, cube_triangles_1, green_k) 
     
        rotation_orbit -= 0.01  
        rotation_spin += 0.003 
        glutSwapBuffers() 
        
def main(): 
        ''' Main Program. 
        '''    
        glutInit(sys.argv) 
        glutInitWindowSize(600,600)    #    W,H. Line gets scaled to the window. 
        glutCreateWindow('OpenGL Vertex Arrays from Primitive Triangles: Sun, Planets and Spacecraft') 
        InitGL(600, 600) 
        glutIdleFunc(DrawGLScene)      # Update the frames when processor has spare time. 
        glutMainLoop() 

main()
