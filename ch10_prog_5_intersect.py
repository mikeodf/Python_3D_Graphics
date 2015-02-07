"""  ch10 No.5  
Program name: intersect.py 
Objective: Locate the point of intersection of two lines in 3D space.
 
Keywords: OpenGL, triangle, line intersection, normals. 
============================================================================79 
From the book "Python Graphics for Games: Working in 3 Dimensions"

Comments: The lines have to be coplanar. No test is done to verify that the
lines are coplanar. Since this is designed only to be used to work with 
lines in the plane of the same triangle, the test is not necessary. 

Tested on: Python 2.7.3, Python 3.2.3       
Author:  Mike Ohlson de Fine 
================================ 
""" 
# Intersection of two lines
def intersect(p1,p2, q1, q2): 
    """ Intersection of 2 lines in 3D cartesian space. The lines should be coplanar. 
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

    # Intersection in the x-y plane (ie. Projection onto the x-y plane.). 
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
