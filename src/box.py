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

import pygame

class Box(object):
    
    
    body = None
    game_display = None
    box = None
    
    def __init__(self,new_world,new_display,new_x,new_y,new_width,new_height):
        self.game_display = new_display
        self.body = new_world.b2_game_world.CreateDynamicBody(position=(new_x, new_y))

    # And add a box fixture onto it (with a nonzero density, so it will move)
        self.box = self.body.CreatePolygonFixture(box=(new_width, new_height), density=1, friction=0.3)
        
    def draw(self):
        pygame.draw.rect(self.game_display,(0,0,255),[0,0,10,10],1000)
        pygame.draw.rect(self.game_display,(0,0,255),[self.body.position.x*16,-(self.body.position.y*16)+500,10,10],2)
        print(self.body.position)

        