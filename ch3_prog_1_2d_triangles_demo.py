"""  ch3 No.1 
Program name: 2d_triangles_demo_1.py 
Objective: Demonstrate the display of 2D objects.. 

Keywords: 2d objects, display. 
============================================================================79 
From the book "Python Graphics for Games: Working in 3 Dimensions"

Comments: Three triangles are drawn. No use is made of loops. 
                                                                                      
Tested on: Python 2.6, Python 2.7, Python 3.2, 
Author: Mike Ohlson de Fine    
================================ 
""" 
from Tkinter import * 
# from tkinter import *   # Use this instead of the above for python version 3.x

root = Tk() 
root.title('Trianagles') 
cw = 200                                      # canvas width. 
ch = 200                                      # canvas height. 
canvas_1 = Canvas(root, width=cw, height=ch, background="white") 
canvas_1.grid(row=0, column=1) 
#==================================================================== 
triangle_1 = [ 21.0, 40.0   ,4.1, 7.0   ,23.0, 18.3, 21.0, 40.0  ] 

triangle_2 = [ 5.3 , 4.8   ,42.4, 7.5   ,23.6 , 17.4  ,5.3 , 4.8  ] 

triangle_3 = [ 42.6, 10.0   ,23.7, 40.6  ,23.8, 18.2 , 42.6, 10.0   ] 
#==================================================================== 
canvas_1.create_line(triangle_1) 
canvas_1.create_line(triangle_2) 
canvas_1.create_line(triangle_3) 

root.mainloop()
