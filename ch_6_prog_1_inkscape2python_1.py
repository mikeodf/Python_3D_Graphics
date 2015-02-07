""" ch6 No.1 
Program name: inkscape2python_1.py 
Objective: Transform an inkscape.svg drawing file into a usable Python vertex lists. 
Specifically: Identify 2D vertices in all lines saved in a SVG file from an 
Inkscape drawing. 
Each .svg line like:  d="M 82.833,90.697 L 97.985,78.575 L 118.19,99.788" 
is converted to a Python list like: 
[ 82.833,90.697 , 97.985,78.575 , 118.19,99.788  ] 

Keywords: inkscape, conversion, drawing, vertices, lines, 
============================================================================79 
From the book "Python Graphics for Games: Working in 3 Dimensions"

Comments: Method:Identify 2D vertices in all lines saved in a SVG file from an 
Inkscape drawing. 
Each .svg line like:  d="M 82.833,90.697 L 97.985,78.575 L 118.19,99.788" 
is converted to a Python list like: 
[ 82.833,90.697 , 97.985,78.575 , 118.19,99.788  ] 

Input data used is an SVG file exported from Inkscape. 

Tested on: Python 2.6, Python 2.7.3, Python 3.2.3 
Author:          Mike Ohlson de Fine 
""" 
obj_file_name = "/home/mikeodf/constr/face_0.svg" # Inkscape output file. 

def extract_floats(line): 
    """  Objective: Extract a complete floating point number, including sign.        
         Assumption: An appropriate line of characters ( the "line" argument) 
         for parsing has been found. 
         Now we work through it character by character looking for minus signs, decimal points 
         and digits. These are added to a string xx which will be converted to a float. 
         A non-digit will signal the completion of the float. 
    """ 
    slice_loc = 0                 #  Slice position counter. 
    line_length = len(line)       # Total length of line. 
    sign = ''                     # The sign (negative or positive) of the number. 
    jadigit = 0                   # Digit 'present' toggle flag. 
    xx = ''                       # xx will become the CURRENT floating point number. 
    float_seq = 0                 # The number of floats obtained. When == 3 add 1.0 for augmentation. 
    float_list = [] 

    # Pad the line with a space. Necessary to avoid loop index errors. 
    line = line + ' ' 
    for chr in line: 
    
        # Overriding condition. Only proceed if we are working inside the line length. 
        if slice_loc <= line_length-1: 
        
            # Is the character a non-digit? 
            if line[slice_loc].isdigit() == False: 
         
                # Is the character a minus sign? 
                if line[slice_loc] == '-': 
                    sign = '-' 
                    xx = sign 
                slice_loc = slice_loc + 1       

            # Is the character a digit? 
            if  line[slice_loc].isdigit(): 
                jadigit = 1   
                xx = xx + line[slice_loc]     # Add the new digit to xx 
                slice_loc = slice_loc + 1 

            # Is the character a decimal point? 
            if  line[slice_loc] == '.': 
                jadigit = 1   
                xx = xx + line[slice_loc]       # Add this digit to xx 
                slice_loc = slice_loc + 1 

            # The previous character was a digit but the current one is not, 
            # therefore the current floating point number is now complete. 
            if  line[slice_loc].isdigit() == False and jadigit == 1:   # Terminate float. 
                jadigit = 0                            # Clear 'working up float' flag. 
                float_seq = float_seq + 1        
                sign =''                               # Clear the sign flag. 
                float_list.append(float(xx))           # Add the latest float to the list .
                slice_loc = slice_loc + 1 
                xx = '' 

    return float_list    

id_start = ' d="M '             # Id signature for a valid vertex list in the inkscape.svg  - Data source. 

line_set = [] 
file_lines = 0 
''' note to open a file and process its contents, and make sure to close it,
    you can simply do: 
    with open("x.txt") as f: 
''' 
with open(obj_file_name) as ff: 
    counter = 0                    # Slice position counter. 
    for line in ff:                # For each line ( line is the string contents of the line) 
        line_length = len(line)    # Total length of line. Needed for number of slices. 
        file_lines += 1            # Keep a count of the number of lines. 
        #Whenever id_start is discovered line.find(id_start) will be true. 
        # This method returns index (string slice location) if found and -1 otherwise. 
       
        if line.find(id_start) != -1:         # id_start string discovered. This denotes an SVG line of vertices. 
            slice_loc = line.find(id_start)     # The nxt character will be what we have been seeking -  a float. 
            line_string = line 
            floats_list = extract_floats(line) 
            line_set.append(floats_list) 
 
# ========================== 
#  CONVERTED SHAPE  TESTING 
# ========================== 
from Tkinter import * 
#from tkinter import *   # Use this instead of the above for python version 3.x
root = Tk() 
root.title('Inkscape shapes converted to Python list.') 
cw = 350                                      # canvas width. 
ch = 300                                      # canvas height. 
canvas_1 = Canvas(root, width=cw, height=ch, background="#eeeeee") 
canvas_1.grid(row=0, column=1) 

for i in range(len(line_set)): 
    canvas_1.create_line( line_set[i], width = 3,  fill= 'blue' ) 

root.mainloop()
