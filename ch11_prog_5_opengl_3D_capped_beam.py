"""  ch11 No.5 
Program name: opengl_3D_capped_beam.py 
Objective: Construct the capped beam used to construct finger bones. 
 
Keywords: OpenGL, capped beam, finger, digit. 
============================================================================79 
From the book "Python Graphics for Games: Working in 3 Dimensions"

Comments: A generic beam is defined whose relative dimensions can be
adjusted for different purposes.

Tested on: Python 2.6, Python 2.7.3, Python 3.2.3       
Author:  Mike Ohlson de Fine 
================================ 
"""
# Capped Beam Function.
def capped_beam(beam): 
    ''' Draw a tapered tube with capped endpieces, from triangles. 
        Arguments: origin (bottom center), botton width (wb),  bottom z-depth(db), height of bottom pyramid(hbp) 
                    top width (wt), top z-depth (dt), height of top pyramid hPT) , total height (hite). 
    ''' 
    hite = beam[0] 
    wb = beam[1] 
    db = beam[2] 
    hpb = beam[3] 
    wt = beam[4] 
    dt = beam[5] 
    hpt = beam[6] 

    # Vertices 
    vt1 = [         0,    0,          0.0  ] 
    vt2 = [   -wb/2.0,    hpb,          db   ] 
    vt3 = [   -wb/2.0,    hpb,         -db   ] 
    vt4 = [    wb/2.0,    hpb,         -db   ] 
    vt5 = [    wb/2.0,    hpb,          db   ] 
    vt6 = [   -wt/2.0,    hite-hpt,     dt   ] 
    vt7 = [   -wt/2.0,    hite-hpt,    -dt   ] 
    vt8 = [    wt/2.0,    hite-hpt,    -dt   ] 
    vt9 = [    wt/2.0,    hite-hpt,     dt   ] 
    vt10 = [        0,    hite,        0.0  ] 
   
    # 1 - 2 - 5 etc. Bottom cap. 
    tri1 = [ vt1, vt2, vt5 ] 
    tri2 = [ vt1, vt2, vt3 ] 
    tri3 = [ vt1, vt3, vt4 ] 
    tri4 = [ vt1, vt4, vt5 ] 

    # 10 - 6 - 9 etc. Top cap. 
    tri5 = [ vt10, vt6, vt9 ] 
    tri6 = [ vt10, vt6, vt7 ] 
    tri7 = [ vt10, vt7, vt8 ] 
    tri8 = [ vt10, vt8, vt9 ] 

    # Front 
    tri9  = [ vt2, vt9, vt5 ] 
    tri10 = [ vt2, vt6, vt9 ] 
    # Back 
    tri11 = [ vt3, vt8, vt4 ] 
    tri12 = [ vt3, vt7, vt8 ] 
    #  Right side 
    tri13 = [ vt2, vt7, vt3 ] 
    tri14 = [ vt2, vt6, vt7 ] 
    # Left side 
    tri15 = [ vt5, vt8, vt4 ] 
    tri16 = [ vt5, vt9, vt8 ] 

    return tri1, tri9,  tri10, tri5,  tri2, tri13, tri14, tri6, tri3, tri11, tri12, tri7, tri4, tri15, tri16, tri8
