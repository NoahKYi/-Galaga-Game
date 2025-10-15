import pygame

class Ship():
#Pygame treats things like rectangles
#x,y coordinates & Origin are the top left of the rectangle
    def __init__(self, screen):
        self.screen = screen

        self.image = pygame.image.load("PythonGalagaShip.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        #Gets Rect of ship

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        #Defines where the ship is at

    def blitme(self):
        #Draws ship at its location
        self.screen.blit(self.image, self.rect)

