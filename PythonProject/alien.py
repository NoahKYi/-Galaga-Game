import pygame
from pygame.sprite import Sprite

class Alien(Sprite):

    def __init__(self, ai_settings, screen):
        super(Alien, self).__init__()
        self.image = pygame.image.load("MillF.bmp")
        self.screen = screen
        self.ai_settings = ai_settings

        #Load the alien

        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def blitme(self):
        self.screen.blit(self.image, self.rect)

