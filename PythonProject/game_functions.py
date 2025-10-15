import sys
import pygame

def check_events(ship):
    for event in pygame.event.get():
        if event.type == pygame.event.get():
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                #The event key listens for the key to push it right
                ship.rect.centerx += 21

def update_screen(ai_settings, screen, ship):
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    pygame.display.flip()




