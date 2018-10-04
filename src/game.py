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


class Game(State):
    
    game_world = None
    
    def create_game_world(self):
        print(type(self.game_display))
        
        self.game_world = World(self.game_display)
    
    
    
    
    def draw(self):
        self.game_world.draw()
        
    def update(self):
        self.game_world.update()
