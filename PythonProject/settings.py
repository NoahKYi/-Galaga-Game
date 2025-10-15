class Settings():
    #Class for how the ship looks/behaves

    def __init__ (self):

        #Screen Settings
        self.screen_width = 1265
        self.screen_height = 665
        self.bg_color = (0,0,0)

        #Ship Settings
        self.ship_speed_factor = 1.5

        #Bullet Settings
        self.bullet_speed_factor = 1
        self.bullet_width = 15
        self.bullet_height = 15
        self.bullet_color = 255,255,255