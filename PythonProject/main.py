import sys
#Exits Game when player quits
import pygame

from settings import Settings
from ship import Ship
import game_functions as gf
#Importing Settings

def run_game():
    pygame.init()

    ai_settings = Settings()
    #Instance Of setting

    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    #Builds background to make game work properly

    pygame.display.set_caption("Galaga")

    ship = Ship(ai_settings, screen)

    while True:
        #Keeps Game functioning
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_settings, screen, ship)
        screen.fill(ai_settings.bg_color)
        # Backround color (This is very interesting. The different numbers combine to form a singular color)
        #Gives Screen Color
        ship.blitme()
        pygame.display.flip()

run_game()