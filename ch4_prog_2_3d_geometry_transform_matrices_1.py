"""   ch4 No.2 
Program name: 3d_geometry_transform_matrices_1.py 
Objective: List code for matrix transfoems

Keywords: 3d shape, transforms, matrices, function. 
==================================================================79 
From the book "Python Graphics for Games: Working in 3 Dimensions"

Tested on: Python 2.6, Python 2.7.3, Python 3.2.3       
Author:  Mike Ohlson de Fine 
================================ 
""" 
# Geometry Transformation Matrices

# a) Rotation around the X-axis
# Usage:  Rotated_vector = [x y z 1] * T_rotx(theta)

def T_rotx(theta): 
    """ Rotate points theta (radians)around the X-axis. 
    """ 
    T  = np.matrix([[1.0,              0.0,              0.0,    0.0],
                    [0.0,  math.cos(theta), -math.sin(theta),    0.0], 
                    [0.0,  math.sin(theta),  math.cos(theta),    0.0], 
                    [0.0,              0.0,              0.0,    1.0] ]) 
    return T
#========================================================================
# b) Rotation around the Y-axis
# Usage:  Rotated_vector = [x y z 1] * T_roty(theta)

def T_roty(theta): 
    """ Rotate points theta (radians)around the Y-axis. 
    """ 
    T  = np.matrix([[  math.cos(theta),  0.0, math.sin(theta),  0.0],
                    [              0.0,  1.0,             0.0,  0.0], 
                    [ -math.sin(theta),  0.0, math.cos(theta),  0.0], 
                    [              0.0,  0.0,             0.0,  1.0] ]) 
    return T
#========================================================================
# c) Rotation around the Z-axis
# Usage:  Rotated_vector = [x y z 1]*T_rotz(theta)

def T_rotz(theta): 
    """ Rotate points theta (radians)around the Z-axis. 
    """     
    T = np.matrix([ [ math.cos(theta), -math.sin(theta),   0.0, 0.0], 
                    [ math.sin(theta),  math.cos(theta),   0.0, 0.0],
                    [             0.0,              0.0,   1.0, 0.0], 
                    [             0.0,              0.0,   0.0, 1.0] ]) 
    return T
#========================================================================
# d) Shape Size Amplification or Shrinking.
# Usage example:  Scaled_vector = [x y z 1] * T_scaling(150.0 , 200.0, 0.0) 

def T_scaling(sx, sy, sz): 
    """ Expand points by sx in the X-direction, 
                      sy in the Y-direction and 
                      sz in the Z direction. 
    """ 
    T  = np.matrix([ [ sx,     0.0,      0.0,      0.0],
                     [0.0,      sy,      0.0,      0.0], 
                     [0.0,     0.0,       sz,      0.0], 
                     [0.0,     0.0,      0.0,     1.0] ]) 
    return T
#========================================================================
# e) Shape Translation (Shifting).
# Usage example:  Scaled_vector = [x y z 1] * T_translate( 300.0, 300.0, 0.0) 

def T_translate(tx, ty, tz): 
    """ Shift points tx in the X-direction, 
                     ty in the Y-direction and 
                     tz in the Z direction. 
    The apparent direction of Z increasing seems to be negative!!!. 
    """ 
    T = np.matrix([[1.0,   0.0,   0.0,   0.0], 
                   [0.0,   1.0,   0.0,   0.0], 
                   [0.0,   0.0,   1.0,   0.0], 
                   [ tx,    ty,    tz,   1.0] ]) 
    return T
#========================================================================
