import sys
#Exits Game when player quits
import pygame

from settings import Settings
from ship import Ship
import game_functions as gf
#Importing Setting




def run_game():

    pygame.init()

    ai_settings = Settings()
    #Instance Of setting



    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    #Builds background to make game work properly

    #defines size of the screen

    pygame.display.set_caption("Galaga")

    ship = Ship(screen)


    #Backround color (This is very interesting. The different numbers combine to form a singular color)

    while True:
        #Keeps Game functioning
        gf.check_events(ship)
        gf.update_screen(ai_settings, screen, ship)
        screen.fill(ai_settings.bg_color)
        # Backround color (This is very interesting. The different numbers combine to form a singular color)
        #Gives Screen Color
        ship.blitme()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                #Exits Game

        pygame.display.flip()

run_game()