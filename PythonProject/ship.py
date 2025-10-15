import pygame

class Ship():
#This file is for controlling movement/interaction
#Pygame treats things like rectangles
#x,y coordinates & Origin are the top left of the rectangle
    def __init__(self, ai_settings, screen):
        self.screen = screen
        self.ai_settings = ai_settings
        self.image = pygame.image.load("PythonGalagaShip.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        #Gets Rect of ship

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        #Defines where the ship is at

        self.center = float(self.rect.centerx)
        #Decimal for the ship's center

        self.moving_right = False
        self.moving_left = False
        #Movement Flags

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        self.rect.centerx = self.center
        #Update rect object from the ship's center

    def blitme(self):
        #Draws ship at its location/screen
        self.screen.blit(self.image, self.rect)


