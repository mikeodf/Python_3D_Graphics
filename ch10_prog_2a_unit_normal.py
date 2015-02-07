"""  ch10 No.2  
Program name: unit_normal.py 
Objective: From vertices of a triangle, use the vector cross-product 
to calculate the unit normal. 
 
Keywords: OpenGL, triangle, unit normal, vector cross product. 
============================================================================79 
From the book "Python Graphics for Games: Working in 3 Dimensions"

Comments: This is a precursor to making unit normals visible as directed
arrow-tips. 

Tested on: Python 2.7.3, Python 3.2.3       
Author:  Mike Ohlson de Fine 
================================ 
""" 
# Unit normal function
def unit_normals(p,q,r): 
    """  Compute the vector cross product from three vertices of a triangle. 
               Three points are given by their position vectors p, q, and r. 
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
    vnx = vnx/len_vn 
    vny = vny/len_vn 
    vnz = vnz/len_vn 

    return vnx, vny, vnz
