"""
------------------------------------------------------------------------
[program description]
------------------------------------------------------------------------
Author: Danny Van Stemp
ID:     181549810
Email:  whatsmyemail@idunno.ca
__updated__ = "2018-07-27"
------------------------------------------------------------------------
"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import Box2D

"""
This is a simple example of building and running a simulation using Box2D. Here
we create a large ground box and a small dynamic box.

** NOTE **
There is no graphical output for this simple example, only text.
"""

from Box2D import (b2PolygonShape, b2World)
from box import Box

game_display = None



class World():
    
    b2_game_world = None
    groundBody = None
    body = None
    box = None
    game_boxes = []

    
    def create_box(self,new_x,new_y,new_width,new_height):
        print(type(game_display))
        new_box = Box(self,self.game_display,new_x,new_y,new_width,new_height)
        self.game_boxes.append(new_box)
    
    def __init__(self,new_display):
        self.b2_game_world = b2World()  # default gravity is (0,-10) and doSleep is True
        self.groundBody = self.b2_game_world.CreateStaticBody(position=(0, -48),
                                    shapes=b2PolygonShape(box=(80, 10)),
                                    )
        # Create a dynamic body at (0, 4)
        self.body = self.b2_game_world.CreateDynamicBody(position=(0, 4))

# And add a box fixture onto it (with a nonzero density, so it will move)
        self.box = self.body.CreatePolygonFixture(box=(1, 1), density=1, friction=0.3)
        print(type(new_display))
        self.game_display = new_display
        
        self.create_box(10,10,5,5)
        self.create_box(15,10,5,5)
        self.create_box(20,10,5,5)
        self.create_box(25,10,5,5)
        self.create_box(30,10,5,5)
        self.create_box(35,10,5,5)
        

        


    
# Prepare for simulation. Typically we use a time step of 1/60 of a second
# (60Hz) and 6 velocity/2 position iterations. This provides a high quality
# simulation in most game scenarios.

    
    

    timeStep = 1.0 / 60
    vel_iters, pos_iters = 6, 2

    def update(self):
    # Instruct the world to perform a single step of simulation. It is
    # generally best to keep the time step and iterations fixed.
        self.b2_game_world.Step(self.timeStep, self.vel_iters, self.pos_iters)

    # Clear applied body forces. We didn't apply any forces, but you should
    # know about this function.
        self.b2_game_world.ClearForces()
        
    def draw(self):
        for box in self.game_boxes:
            box.draw()



