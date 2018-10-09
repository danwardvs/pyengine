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
from state import State
from world import World
from mouselistener import MouseListener

class Game(State):
    
    game_world = None
    
    def create_game_world(self):
        print(type(self.game_display))
        
        self.game_world = World(self.game_display)
    
    
    
    
    def draw(self):
        self.game_world.draw()
        
    def update(self):
        
        if MouseListener.button_pressed[MouseListener.Buttons.MOUSE_LEFT_CLICK.value]:
            self.game_world.create_box(MouseListener.mouse_x/20, -(MouseListener.mouse_y/20), 1.6, 1.6)
            
        if MouseListener.button_pressed[MouseListener.Buttons.MOUSE_RIGHT_CLICK.value]:
            self.game_world.create_box(MouseListener.mouse_x/20, -(MouseListener.mouse_y/20), 1, 1)
            
        self.game_world.update()

        
