
import pygame

game_display = pygame.display.set_mode((800,600))
pygame.display.set_caption('Nice Window')
pygame.display.flip()

from state import State
from menu import Menu
from init import Init

current_state = Init()

clock = pygame.time.Clock()
    
running = True

def change_state(new_state):
    global current_state

    if new_state != State.program_states.STATE_NULL:
        print("buttz galore")
        if new_state == State.program_states.STATE_MENU.value:
            current_state = Menu()
            print("buttz mkgee")



while running:
    
        
    clock.tick(60)
    
    change_state(current_state.get_next_state())
    print(current_state.get_next_state())
    
    for event in pygame.event.get():
        
        

        if event.type == pygame.QUIT:
            running = False
    
    current_state.update()

    
    game_display.fill((255,255,255))

    current_state.draw()
    
    pygame.display.update()

    

    