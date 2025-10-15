import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    "Manages bullets from a ship"

    def __init__(self, ai_settings, screen, ship):
        super(Bullet, self).__init__()
        self.screen = screen

        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        #Creates bullet

        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor
        #stores bullet color and speed factor
    def update(self):
        #Moves the bullet around the screen
        self.y -= self.speed_factor
        #Decreases Y value to move up the screen

        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self. color, self.rect)