"""   ch7 No.1  
Program name: blender_vertices_extraction_1.py 
Objective: Transfer a blender.obj 3D object file into single Python vertex list. 

Keywords: blender, geometry, vertices, list 
============================================================================79 
From the book "Python Graphics for Games: Working in 3 Dimensions"

Comments: Wavefront.obj files exported from Blender. 
          Blender 3D objects are the source objects. 
 
Tested on: Python 2.6, Python 2.7.3, Python 3.2.3 
Author:          Mike Ohlson de Fine 
""" 
# File containing 3D objects exported from Blender. 
obj_file_name = "/home/mikeodf/constr/blender_objects/triangle.obj"  # Data source. 
 
def extract_floats(line): 
    """  Objective: identify 3D vertices in a line of Wavefront .obj file. 
         Each .obj line on the form "v x1  y1 z1 " is converted to a Python list like 
         "[ xa, y1, z1 ]" where x1, y1 and z1 are floating point numbers. 
         Assumption: An appropriate line of characters for parsing has been found. 
         Then we work through it character by character looking for minus signs, decimal points 
         and digits. These are added to a string xx which will be converted to a float. 
         A non-digit will signal the completion of the floating point number. 
    """ 
    slice_loc = 0                       # Slice position counter. 
    line_length = len(line)             # Total length of line. 
    sign = ''                           # The sign (negative or positive) of the number. 
    yesdigit = 0                        # 'Digit present' toggle flag. 
    xx = ''                             # xx will become the CURRENT floating point number. 
    float_seq = 0                       # The number of floats obtained. 
    float_list = [] 

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
                yesdigit = 1   
                xx = xx + line[slice_loc]     # Add the new digit to xx. 
                slice_loc = slice_loc + 1 

            # Is character a decimal point? 
            if  line[slice_loc] == '.': 
                yesdigit = 1   
                xx = xx + line[slice_loc]       # Add this decimal point to xx. 
                slice_loc = slice_loc + 1 

            # The previous character was a digit but the current one is not 
            # Therefore the current floating point number is now complete. 
            if  line[slice_loc].isdigit() == False and yesdigit == 1:    # Terminate float. 
                yesdigit = 0                                                                   # Clear 'working up float' flag. 
                float_seq = float_seq + 1 
                sign =''                            # Clear the sign flag. 
                float_list.append(float(xx))        # Add the latest float to the list. 
                slice_loc = slice_loc + 1 
                xx = '' 

    return float_list 

def augment_vertices(vertex_list): 
    """  Just augment the vertex position vector by inserting 1.0 at the end. 
    """ 
    for i in range(len(vertex_list)): 
        vertex_list[i].append(1.0) 
    return vertex_list 

# Find vertices and transform into augmented vertex vectors. 
vertex_list = [] 
with open(obj_file_name) as ff: 
    counter = 0                                   # Slice position counter. 
    for line in ff:                               # For each line in ff: 
        line_length = len(line)                   # Total length of line. 
        if line.find('v') != -1:    # Is there a 'v' anywhere in the line? 
                                    # This denotes a vertex. 
            slice_loc = line.find('v')  # If yes, return lowest index in string where 'v' occurs. 
            if slice_loc == 0:          # If the first character is 'v' then: 
               digit_list =  extract_floats(line)              
               vertex_list.append(digit_list) 

    augmented_vertex_list = augment_vertices(vertex_list) 

print 'vertex_list: ', vertex_list
