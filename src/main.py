
import pygame

game_display = pygame.display.set_mode((800,600))
pygame.display.set_caption('Nice Window')
pygame.display.flip()

from state import state
from menu import menu

current_state = menu()

clock = pygame.time.Clock()
    
running = True

while running:
    
    clock.tick(60)
    
    for event in pygame.event.get():
        
        

        if event.type == pygame.QUIT:
            running = False
    
    current_state.update()

    
    game_display.fill((255,255,255))

    current_state.draw()
    
    pygame.display.update()

    

    