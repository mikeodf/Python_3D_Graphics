""" ch11 No.8
Program name: vector_2d_ops.py
Objective: Basic vector operations addition, subtraction, dot product, cross product.

Keywords: vectors
============================================================================79
Explanation: 
Author:          Mike Ohlson de Fine
License:         BSD
"""
import math
import itertools
#-----------------------------------------------------------------
# Vector 3D operations
#========================

def intersect(p1,p2, q1, q2):
    """ Intersection of 2 lines in 3D cartesian space. Lines are coplanar.
    Inputs are the position vectors of two points on each line.
    There should be a test to confirm the the the two lines are co-planar,
    prior to any solution being computed. For the time being
    we will assume the lines are coplanar.
    """
    
    px1 = p1[0]   
    py1 = p1[1]
    pz1 = p1[2]

    px2 = p2[0]   
    py2 = p2[1]
    pz2 = p2[2]

    qx1 = q1[0]   
    qy1 = q1[1]
    qz1 = q1[2]

    qx2 = q2[0]   
    qy2 = q2[1]
    qz2 = q2[2]

    # Slopes
    # Q1: Are any divisors zero? ie. are lines paralell?
    if (px2 - px1) == 0:
        divsr_mp_xy = 0.000000001
    else: divsr_mp_xy = (px2 - px1)

    if (pz2 - pz1) == 0:
        divsr_mp_zy = 0.000000001

    else: divsr_mp_zy = (pz2 - pz1)

    if (qx2 - qx1) == 0:
        divsr_mq_xy = 0.000000001
    else: divsr_mq_xy = (qx2 - qx1)

    if (qz2 - qz1) == 0:
        divsr_mq_zy = 0.000000001
    else: divsr_mq_zy = (qz2 - qz1)

    mp_xy = (py2 - py1)/divsr_mp_xy
    mp_zy = (py2 - py1)/divsr_mp_zy

    mq_xy = (qy2 - qy1)/divsr_mq_xy
    mq_zy = (qy2 - qy1)/divsr_mq_zy

    # Intercepts - constants.
    cp_xy = py1 -mp_xy*px1
    cp_zy = py1 -mp_zy*pz1

    cq_xy = qy1 -mq_xy*qx1
    cq_zy = qy1 -mq_zy*qz1

    # Intersection in the x-y plane.
    if (mp_xy - mq_xy) == 0:
        divsr_m = 0.000000001
    else: divsr_m = (mp_xy - mq_xy)

    xi = (cq_xy - cp_xy)/divsr_m

    yi = xi*mp_xy +cp_xy

    if (mp_zy - mq_zy) == 0:
        divsr_m = 0.000000001
    else: divsr_m = (mp_zy - mq_zy)
    zi = (cq_zy - cp_zy)/divsr_m

    return xi, yi, zi

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

def half_unit_normals(p,q,r):
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
        vnx = 0.5*vnx/len_vn
        vny = 0.5*vny/len_vn 
        vnz = 0.5*vnz/len_vn
    
    return vnx, vny, vnz


def array_triangle_normals(vertex_array):
    """ Calculate the vertex normal for each face, repeat it three times to furnish a Normal for each
        vertex of the triangle in the vertex array. The output is the target glNormaArray.      
    """
    #print 'vertex_array:', vertex_array
    norm_array = []
    for i in range (0, len(vertex_array), 9): # Number of triangles
       # Each sequence of 9 floats from vertex_array supplies three vertices v1, v2, v3
       a1 = vertex_array[i]        # first vertex.
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
       norm_array.append(vec_norm) # Set stride to 0 to match each face to a normal..
       norm_array.append(vec_norm)
       norm_array.append(vec_norm)
    norm_array = list(itertools.chain(*norm_array))     # Ensure the array has been flattened. 
    return norm_array
#================================================================
# Test for array_triangle_normals(vertex_array)
'''
octet4tri =  [
-0.0, 0.7, 0.7,    -0.0, 1.0, 0.0,    -0.7, 0.7, 0.0,  # 1st triangle
-0.7, 0.0, 0.7,    -0.0, 0.7, 0.7,    -0.7, 0.7, 0.0,  # 2nd triangle
-0.0, 0.7, 0.7,    -0.7, 0.0, 0.7,    -0.0, 0.0, 1.0,  # 3rd triangle
-1.0, 0.0, 0.0,    -0.7, 0.0, 0.7,    -0.7, 0.7, 0.0 ] # 4th triangle

get_normals =  array_triangle_normals(octet4tri)
print 'get_normals:', get_normals

Answer: get_normals: [-0.36650, 0.85518, 0.36650,    -0.36650, 0.85518, 0.36650,    -0.36650, 0.85518, 0.36650,
                      -0.57735, 0.57735, 0.57735,    -0.57735, 0.57735, 0.57735,    -0.57735, 0.57735, 0.57735,
                      -0.36650, 0.36650, 0.85518,    -0.36650, 0.36650, 0.85518,    -0.36650, 0.36650, 0.85518,
                      -0.85518, 0.36650, 0.36650,    -0.85518, 0.36650, 0.36650,    -0.85518, 0.366508, 0.36650  ]
'''
#================================================================

def tri_centroid(p,q,r):
    """ Locate the centroid of a triangle.     
        The intersection of the lines joining a vertex
        with the mid-point of the opposite side is computed.
        Arguments: three vertices of a triangle.
    """
    # Mid-points of p-q and p-r.
    # Distances point-to-point.
    vx1 = r[0] - p[0]  # x1 - x3.
    vy1 = r[1] - p[1]  # y1 - y3.
    vz1 = r[2] - p[2]  # z1 - z3.

    vx2 = q[0] - p[0]  # x2 - x1.
    vy2 = q[1] - p[1]  # y2 - y1.
    vz2 = q[2] - p[2]  # z2 - z1. 

    # Mid-points of p-q (position vector).
    pqx_mp = p[0] + vx2/2.0 
    pqy_mp = p[1] + vy2/2.0 
    pqz_mp = p[2] + vz2/2.0    
    pq_mp = [pqx_mp, pqy_mp, pqz_mp ]

    # Mid-points of p-r (position vector).
    prx_mp = p[0] + vx1/2.0 
    pry_mp = p[1] + vy1/2.0 
    prz_mp = p[2] + vz1/2.0 

    pr_mp = [prx_mp, pry_mp, prz_mp ]

    # Intersection.
    xi, yi, zi = intersect(r,pq_mp, q, pr_mp)
    return xi, yi, zi

def centroid_normals(vertex_array, dxy):
    """ Calculate the vertex normal for each face, repeat it three times to furnish a Normal for each
        vertex of the triangle in the vertex array. The output is the target glNormaArray.      
    """
    norm_arrows = []
    #for i in range (len(vertex_array)/9): # Number of triangles
    for i in range (0, len(vertex_array), 9): # Number of triangles
           # Each sequence of 9 floats from vertex_array supplies three vertices v1, v2, v3
           a1 = vertex_array[i]        # first vertex.
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

           vnor = half_unit_normals(v1, v2, v3)
           vcen = tri_centroid(v1, v2, v3)
           vsum  = [vnor[0]+vcen[0], vnor[1]+vcen[1], vnor[2]+vcen[2] ] 
           # Now we produce twl triangles thatpoint in the direction of the normal.
           # each must be added to an array of normal spikes - which are visible normals.
       
           tris = [ vcen[0], vcen[1], vcen[2],    vcen[0]+dxy, vcen[1], vcen[2],    vsum[0], vsum[1], vsum[2],
                vcen[0], vcen[1], vcen[2],    vcen[0], vcen[1]+dxy, vcen[2],    vsum[0], vsum[1], vsum[2 ]  ]
           norm_arrows.append(tris)
    norm_arrows = list(itertools.chain(*norm_arrows))     # Ensure the array has been flattened. 

    return norm_arrows

def vec_sum(p,q):
    """ Sum of two vectors.     
        Sum the components of two vectors.
        The difference is obtained by negating one of the vectors.
    """
    xs = p[0] + q[0]
    ys = p[1] + q[1]
    zs = p[2] + q[2]

    return xs, ys, zs


#=============================================================
# Test Vectors and results.
#p = [1.0, 0.0, 0.0]
p = [1.0, 0.0, 0.0]
q = [0.0, 1.0, 0.0]
r = [0.0, 0.0, 1.0]

s = [1.0, 1.0, 1.0]
t = [1.0, 1.0, 0.0]
u = [1.0, 0.0, 1.0]
v = [0.0, 1.0, 1.0]


#print 'unit_normals(p,q,r): ', unit_normals(p,q,r)
'''
Answer: unit_normals(p,q,r):  (0.5773502691896258, 0.5773502691896258, 0.5773502691896258)
'''
#print '================================='
a = [ 1,0,0 ]
b = [ 2,1,0 ]
c = [1.5, 1, 0]
d = [2.5, 0,0]

e = [ 1,0,0 ]
f = [ 1.5,1.0,0 ]
g = [ 2,0,0 ]


#print 'intersect(a,b, c, d): ', intersect(a,b, c, d)
'''
Answer: intersect(a,b, c, d):  (1.75, 0.75, 5e-10)
'''
#print '================================================='
#print 'tri_centroid(e,f,g): ', tri_centroid(e,f,g)
#print '..............................'
'''Answer: (1.5000000006666667, 0.3333333328888888, 6.666666666666667e-10)
'''
#print '================================================='
#print 'intersect(a,b, c, d): ', intersect(a,b, c, d)
#===============================================================
def plot_vector(origin, vector, scale, kula, width):
    chart_1.create_line(org[0], org[1], org[0] + vector[0]* scale, org[1] - vector[1]* scale, width = width, fill = kula)    

def vec_add(vec_a, vec_b):
    vec_sum = [vec_a[0] + vec_b[0], vec_a[1] + vec_b[1]]
    return vec_sum

def vec_sub(vec_a, vec_b):
    vec_sum = [vec_a[0] - vec_b[0], vec_a[1] - vec_b[1]]
    return vec_sum

def vec_dot_product(vec_a, vec_b):
    ''' Vector dot product is product of magnitudes x cosine of angle between the vectors.
        Result is a scalar quantity.
    '''
    magn_a = math.sqrt(vec_a[0]*vec_a[0] + vec_a[1]*vec_a[1])
    magn_b = math.sqrt(vec_b[0]*vec_b[0] + vec_b[1]*vec_b[1])
    theta = math.atan2(vec_a[0], vec_a[1]) - math.atan2(vec_b[0], vec_b[1])
    vec_dot_product = magn_a * magn_b * math.cos(theta)
    return vec_dot_product

def vec_cross_product(vec_a, vec_b):
    ''' Vector cross product is product of magnitudes x sine of angle between the vectors.
        Result is a vector whose direction is mutually at right angles to the plane 
        containing the two vectors. The direction given by the right-hand screw rule.
        Alternate method: Used in the "unit_normals(p,q,r)" function above it uses the determinant 
        derived formula, with values from three points in a triangle.
        vx1 = p[0] - r[0]  # x1 - x3.
        vy1 = p[1] - r[1]  # y1 - y3.
        vz1 = p[2] - r[2]  # z1 - z3.

        vx2 = q[0] - r[0]  # x2 - x3.
        vy2 = q[1] - r[1]  # y2 - y3.
        vz2 = q[2] - r[2]  # z2 - z3.   

        vnx = vy1*vz2 - vz1*vy2
        vny = vz1*vx2 - vx1*vz2
        vnz = vx1*vy2 - vy1*vx2
    '''
    magn_a = math.sqrt(vec_a[0]*vec_a[0] + vec_a[1]*vec_a[1])
    magn_b = math.sqrt(vec_b[0]*vec_b[0] + vec_b[1]*vec_b[1])
    theta = math.atan2(vec_a[0], vec_a[1]) - math.atan2(vec_b[0], vec_b[1])
    vec_cross_product = magn_a * magn_b * math.sin(theta)
    ''' This answer is merely the magnitude of the cross product. We need three a
        three dimensional coordinate system to be able to provide the vector.
        For this case it is directed parallel to the negative z-axis.
    '''
    return vec_cross_product
#-----------------------------------------------------------------
'''
from Tkinter import *
import time
import math
root = Tk()

cw = 600                                      # canvas width
ch = 600                                      # canvas height

GRAVITY = 1.5                             
chart_1 = Canvas(root, width=cw, height=ch, background="white")
chart_1.grid(row=0, column=0)


vec_1 = [10.0, 10,0]    # red
vec_2 = [5.0, -8.0]     # blue
vec_3 = [-10.0, 15,0]   # orange
vec_4 = [5.0, -8.0]     # green
vec_5 = [-7.0, -20,0]   # magenta
vec_6 = [-25.0, -6.0]   # yellow

#Origin
org_x = 300.0

org_y = 200.0
org = [org_x, org_y]
scale = 5.0

# Plot the vectors
plot_vector(org, vec_1, scale,  '#ee0000', 1)
plot_vector(org, vec_2, scale,  '#0000ee', 1)
#plot_vector(org, vec_3, scale,  '#cccc00', 1)
#plot_vector(org, vec_4, scale,  '#00ee00', 1)
#plot_vector(org, vec_5, scale,  '#dd00dd', 1)
#plot_vector(org, vec_6, scale,  '#00eeee', 1)

sum_1 = vec_add(vec_1, vec_2)
diff_1 = vec_sub(vec_1, vec_2)
dot_1 = vec_dot_product(vec_1, vec_2)
cross_1 = vec_cross_product(vec_1, vec_2)

#plot_vector(org, sum_1, scale,  '#000000', 1)
plot_vector(org, diff_1, scale,  '#000000', 1)


chart_1.create_line(org_x, org_y, org_x + vec_1[0]* scale, org_y - vec_1[1]* scale, fill = '#ee0000')
chart_1.create_line(org_x, org_y, org_x + vec_2[0]* scale, org_y - vec_2[1]* scale, fill = '#0000ee')
chart_1.create_line(org_x, org_y, org_x + vec_3[0]* scale, org_y - vec_3[1]* scale, fill = '#cccc00')
chart_1.create_line(org_x, org_y, org_x + vec_4[0]* scale, org_y - vec_4[1]* scale, fill = '#00ee00')
chart_1.create_line(org_x, org_y, org_x + vec_5[0]* scale, org_y - vec_5[1]* scale, fill = '#dd00dd')
chart_1.create_line(org_x, org_y, org_x + vec_6[0]* scale, org_y - vec_6[1]* scale, fill = '#00eeee')

root.mainloop()
'''
