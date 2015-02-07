""" ch6 No.2 
Program name: inkscape2python_2.py 
Objective: Produce a layered complex drawing based on a photograph. 

Keywords: inkscape, conversion, drawing, vertices, lines, 
============================================================================79 
From the book "Python Graphics for Games: Working in 3 Dimensions"

Comments: Input data used is a series of SVG files exported from Inkscape. 

Tested on: Python 2.6, Python 2.7.3, Python 3.2.3 
Author:          Mike Ohlson de Fine 
""" 
obj_file_name_1 = "/home/mikeodf/constr/master_face_lightshade1.svg" # Inkscape output file. 
obj_file_name_2 = "/home/mikeodf/constr/master_face_dark_fills1.svg" # Inkscape output file. 
obj_file_name_3 = "/home/mikeodf/constr/master_face_highlights1.svg" # Inkscape output file. 
obj_file_name_4 = "/home/mikeodf/constr/master_face_lines.svg"            # Inkscape output file. 

def extract_floats(line): 
    """  Objective: Extract a complete floating point number, including sign.        
    """ 
    slice_loc = 0                                                                         # Slice position counter. 
    line_length = len(line)                                                          # Total length of line. 
    sign = ''                                                                                  # The sign (negative or positive) of the number. 
    jadigit = 0                                                                              # Digit 'present' toggle flag. 
    xx = ''                                                                    # xx will become the CURRENT floating point number. 
    float_seq = 0                                              # The number of floats obtained. When == 3 add 1.0 for augmentation. 
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
                jadigit = 1   
                xx = xx + line[slice_loc]     # Add the new digit to xx .
                slice_loc = slice_loc + 1 

            # Is character a decimal point? 
            if  line[slice_loc] == '.': 
                jadigit = 1   
                xx = xx + line[slice_loc]       # Add this digit to xx .
                slice_loc = slice_loc + 1 

            # The previous character was a digit but the current one is not , 
            # therefore the current floating point number is now complete. 
            if  line[slice_loc].isdigit() == False and jadigit == 1:                            # Terminate float. 
                jadigit = 0                                                                                           # Clear 'working up float' flag. 
                float_seq = float_seq + 1 
                sign = ''                                                                                               # Clear the sign flag. 
                float_list.append(float(xx))                                                                # Add the latest float to the list .
                slice_loc = slice_loc + 1 
                xx = '' 

    return float_list    


def get_xy_strings(obj_file_name): 
    """  Identify lines containing x-y coordinates and extract the floating point pairs.
           The argument is the name and directory locations of the SVG file to be parsed.
    """ 
    id_start = ' d="M '             # Id signature for a valid vertex list in the inkscape.svg Data source. 
    line_set = [] 
    file_lines = 0 
 
    with open(obj_file_name) as ff: 
        counter = 0                          # Slice position counter. 
        for line in ff:                        # For each line ( line is the string contents of the line) .
            line_length = len(line)     # Total length of line. Needed for number of slices. 
            file_lines += 1                  # Keep a count of the number of lines. 

            if line.find(id_start) != -1:                    # id_start string discovered. This denotes an SVG line of vertices. 
                slice_loc = line.find(id_start)           # The next character will be what we have been seeking -  a float. 
                line_string = line 
                floats_list = extract_floats(line) 
                line_set.append(floats_list) 
    return line_set 

# Extract from each of four files.
line_set_1 = get_xy_strings(obj_file_name_1) 
line_set_2 = get_xy_strings(obj_file_name_2) 
line_set_3 = get_xy_strings(obj_file_name_3) 
line_set_4 = get_xy_strings(obj_file_name_4) 

# ========================== 
#  CONVERTED SHAPE  TESTING 
# ========================== 
from Tkinter import * 
#from tkinter import *   # Use this instead of the above for python version 3.x
root = Tk() 
root.title('Inkscape shapes converted to Python list.') 
cw = 800                                       # canvas width. 
ch = 1200                                      # canvas height. 
canvas_1 = Canvas(root, width=cw, height=ch, background="#eeeeee") 
canvas_1.grid(row=0, column=1) 

for i in range(len(line_set_1)):                                # Light shadows. 
    canvas_1.create_polygon( line_set_1[i], width = 1,  fill= '#cccccc' ) 

for i in range(len(line_set_2)):                                # Dark shadows. 
    canvas_1.create_polygon( line_set_2[i], width = 1,  fill= '#444444' ) 

for i in range(len(line_set_3)):                                  # Highlights. 
    canvas_1.create_polygon( line_set_3[i], width = 1,  fill= '#ffffff' ) 

for i in range(len(line_set_4)):                                 # Lines 
    canvas_1.create_line( line_set_4[i], width = 1,  fill= '#444444' ) 

root.mainloop()
