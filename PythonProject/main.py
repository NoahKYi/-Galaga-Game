import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
#Importing Settings

"Most important file, connects everything together"



def run_game():
    x = True
    pygame.init()
    ai_settings = Settings()
    #Instance Of setting

    screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
    #screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    #Builds background to make game work properly

    pygame.display.set_caption("Galaga")

    ship = Ship(ai_settings, screen)
    bullets = Group()


    while (True):
        #Keeps Game functioning
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        bullets.update()

        #Getting rid of old bullets
        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)
        print(len(bullets))

        gf.update_screen(ai_settings, screen, ship, bullets)
        screen.fill(ai_settings.bg_color)
        # Backround color (This is very interesting. The different numbers combine to form a singular color)
        #Gives Screen Color

        ship.blitme()
        pygame.display.flip()

run_game()