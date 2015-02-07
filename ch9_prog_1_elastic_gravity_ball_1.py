"""   ch9 No.1  
Program name: elastic_gravity_ball_1.py 
Objective: A ball bouncing subject to gravity and energy loss with each impact. 

Keywords: ball, bounce, gravity, time, movement, mutual impact 
============================================================================79 
From the book "Python Graphics for Games: Working in 3 Dimensions"

Comments: The "canvas_1.delete("ball_1")" method delets the drawn ball_1. 
This tag (label) in the "canvas_1.create_oval( ball_1['posn_x'], ... tags="ball_1") 
instruction says that any drawn object with the identified with the tag "ball_1" 
must be deleted. 
The use of different tags for different objects allows selective deletion. 
Here we delete the ball but leave the trajectory line untouched. 
 
Tested on: Python 2.6, Python 2.7.3, Python 3.2.3 
Author: Mike Ohlson de Fine. 
""" 
from Tkinter import * 
#from tkinter import * 
import time 
import math 
root = Tk() 
root.title("Bouncing Ball with trajectory trace.") 

cw = 800                                     # canvas width 
ch = 400                                     # canvas height 

GRAVITY = 2.5                             
canvas_1 = Canvas(root, width=cw, height=ch, background="white") 
canvas_1.grid(row=0, column=0) 

cycle_period = 20                        # time between new positions of the ball (milliseconds). 
time_scaling = 0.05                      # This governs the size of the differential steps. 
                                         # when calculating changes in position. 

# The parameters determining the dimensions of the ball and it's position. 
# Separate but similarly behaved objects can be made. 
ball_1 = {'posn_x':25.0,              # x position of box containing the ball (bottom). 
           'posn_y':25.0,             # x position of box containing the ball (left edge). 
           'velocity_x':45.0,         # amount of x-movement each cycle of the 'for' loop. 
           'velocity_y':50.0,         # amount of y-movement each cycle of the 'for' loop. 
           'ball_width':20.0,         # size of ball - width (x-dimension). 
           'ball_height':20.0,        # size of ball - height (y-dimension). 
           'color':"blue",            # color of the ball .
           'coef_restitution':0.8     # proportion of elastic enrgy recovered each bounce .

def detectWallCollision(ball_1): 
    """ Detect ball-to-wall collision. This that detects collisions with the walls of the container 
        and then reverses the direction of movement if a collision is detected. 
    """ 
    if ball_1['posn_x'] > cw -  ball_1['ball_width']:           # Collision with right-hand container wall. 
	 ball_1['velocity_x'] = -ball_1['velocity_x'] *  ball_1['coef_restitution']   # Reverse direction. 
         ball_1['posn_x'] = cw -  ball_1['ball_width'] 
    if  ball_1['posn_x'] <  1:                                               # Collision with left-hand  wall. 
	 ball_1['velocity_x'] = -ball_1['velocity_x'] *  ball_1['coef_restitution'] 
         ball_1['posn_x'] = 1     
    if  ball_1['posn_y'] <   ball_1['ball_height']             # Collision with ceiling. 
	 ball_1['velocity_y'] = -ball_1['velocity_y'] *  ball_1['coef_restitution'] 
         ball_1['posn_y'] = ball_1['ball_height'] 
    if  ball_1['posn_y'] > ch - ball_1['ball_height'] :        # Floor collision.  
	 ball_1['velocity_y'] = - ball_1['velocity_y'] *  ball_1['coef_restitution'] 
         ball_1['posn_y'] = ch -  ball_1['ball_height'] 


def diffEquation(ball_1): 
     """ Difference Equation for approximate ball physics. 
     """ 
     x_old =  ball_1['posn_x'] 
     y_old =  ball_1['posn_y'] 
     ball_1['posn_x'] +=   ball_1['velocity_x'] * time_scaling 
     ball_1['velocity_y'] =  ball_1['velocity_y'] + GRAVITY  # A crude equation incorporating gravity. 
     ball_1['posn_y'] +=  ball_1['velocity_y'] * time_scaling 
     canvas_1.create_oval( ball_1['posn_x'],  ball_1['posn_y'],  ball_1['posn_x'] +  ball_1['ball_width'] \ 
     ,ball_1 ['posn_y'] +  ball_1['ball_height'], fill= ball_1['color'], tags="ball_1") 
     canvas_1.create_line( x_old,  y_old,  ball_1['posn_x'], ball_1 ['posn_y'], width = 3, fill= ball_1['color']) 
     detectWallCollision(ball_1)       # Has the ball collided with any container wall? 


for i in range(1, 1000):               # End the program after 1000 position shifts. 
    diffEquation(ball_1)               # Apply physics to the motion of the ball. 
    canvas_1.update()                  # Refreshes the drawing on the canvas. 
    canvas_1.after(cycle_period)       # Makes execution pause for 20 milliseconds.          
    canvas_1.delete("ball_1")           # Erases everything on the canvas .
root.mainloop()
