"""  ch10 No.4  
Program name: tri_centroid.py 
Objective: Locate the centroid of a triangle. 
 
Keywords: OpenGL, triangle, centroid. 
============================================================================79 
From the book "Python Graphics for Games: Working in 3 Dimensions"

Comments: This is a precursor to making unit normals visible as directed
arrow-tips. 

Tested on: Python 2.7.3, Python 3.2.3       
Author:  Mike Ohlson de Fine 
================================ 
""" 
# Centriod of triangle
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
