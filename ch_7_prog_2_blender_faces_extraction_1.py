"""  ch7 No.2   
Program name: blender_faces_extraction_1.py 
Objective: Extract faces from a .obj file and convert them to Python face lists. 

Keywords: blender, geometry, vertices, faces 
============================================================================79 
From the book "Python Graphics for Games: Working in 3 Dimensions"

Comments:  Data used in this program: 
1. Wavefront.obj files exported form Blender. 
   Blender 3D objects are the source objects. 

Tested on: Python 2.6, Python 2.7.3, Python 3.2.3 
Author:          Mike Ohlson de Fine 
""" 
# File containing 3D objects exported from Blender. 
obj_file_name = "/home/mikeodf/constr/triangle_pyramid.obj"     # Data source. 

def extract_integers(line): 
    """  Objective: identify 3D object faces in a line of Wavefront .obj file. 
         Each .obj line of the form "f a1  b1 c1 d1" is converted to a Python list like 
         "[ a1,  b1, c1, d1 ]" where a1,  b1, c1 and d1 are integers. 
         These integers are indexes of the array of vertices. 
         Each face of the object (triangular or four sided) is defined as a list 
         "faces[n][ vertex_list[a1],  vertex_list[b1], vertex_list[c1], vertex_list[d1] ]" 

         Assumption: An appropriate line of characters for parsing has been found. 
         Now we work through it character by character looking for minus signs, decimal points 
         and digits. These are added to a string xx which will be converted to an integer. 
         A non-digit will signal the completion of the line. 
    """ 
    slice_loc = 0                         # Slice position counter. 
    line_length = len(line)               # Total length of line. 
    sign = ''                             # The sign (negative or positive) of the number. 
    jadigit = 0                           # Digit 'present' toggle flag. 
    xx = ''                               # xx will become the CURRENT floating point number. 
    float_seq = 0                         # The number of floats obtained. 
    digit_list = [] 

    # Pad the line with a space. Necessary to avoid loop index errors. 
    line = line + ' ' 
    for chr in line: 
    
        # Overriding condition. Only proceed if we are working inside the line length. 
        if slice_loc <= line_length-1: 
        
            # Is character non-digit? 
            if line[slice_loc].isdigit() == False: 
         
                # Is character a minus sign? 
                if line[slice_loc] == '-': 
                    sign = '-' 
                    xx = sign 
                slice_loc = slice_loc + 1       

            # Is character a digit? 
            if  line[slice_loc].isdigit(): 
                jadigit = 1   
                xx = xx + line[slice_loc]     # Add the new digit to xx 
                slice_loc = slice_loc + 1 

            # Is character a decimal point? 
            if  line[slice_loc] == '.': 
                jadigit = 1   
                xx = xx + line[slice_loc]       # Add this digit to xx 
                slice_loc = slice_loc + 1 

            # The previous character was a digit but the current one is not 
            # Therefore the current integer number is now complete. 
            if  line[slice_loc].isdigit() == False and jadigit == 1:   # Terminate float. 
                jadigit = 0   # Clear 'working up float' flag. 
                float_seq = float_seq + 1 
                sign = ''    # Clear the sign flag. 
                vertex_index = int(xx)-1 
                digit_list.append(vertex_index)      # Add the latest integer to the list. 
                slice_loc = slice_loc + 1 
                xx = '' 

    return digit_list 

faces_integers = [] 
# 2. Find Wavefront faces and form into lists. 
with open(obj_file_name) as ff: 
    counter = 0                          # Slice position counter. 
    for line in ff:                      # For each line in ff: 
        line_length = len(line)          # Total length of line. 
        if line.find('f') != -1:         # Is there a 'f' anywhere in the line? This denotes a face. 
            slice_loc = line.find('f')   # If yes, return lowest index in string where 'v' occurs. 
            if slice_loc == 0:         # If the first character is 'v' then: 
               integers_list =  extract_integers(line) 
 
               faces_integers.append(integers_list) 

print 'faces_list: ', faces_integers 
