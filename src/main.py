
import pygame

game_display = pygame.display.set_mode((800,600))
pygame.display.set_caption('Nice Window')
pygame.display.flip()

from state import State
from menu import Menu
from init import Init
from game import Game

current_state = Init()

clock = pygame.time.Clock()
    
running = True

def change_state(new_state):
    global current_state

    if new_state != State.program_states.STATE_NULL:
        if new_state == State.program_states.STATE_MENU.value:
            current_state = Menu()

        if new_state == State.program_states.STATE_GAME.value:
            print(' we just frickin changed to a game, does that not mean anything to you?')
            current_state = Game()
            current_state.set_display(game_display)
            print(type(game_display))
            current_state.create_game_world()


while running:
    
        
    clock.tick(60)
    
    change_state(current_state.get_next_state())
    
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            running = False
    
    print(type(current_state))
    current_state.update()
     

    
    game_display.fill((255,255,255))

    current_state.draw()
    
    pygame.display.update()

    

    