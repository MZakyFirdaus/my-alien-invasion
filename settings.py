class Settings:
    """ Menyimpan semua settings di sini """
    def __init__(self):
        """ Settings untuk hal yang tetap sepanjang game """
        self.width = 800
        self.heigt = 600
        self.bg_color = (230, 230, 230)

        # Ship Settings
        self.ship_limits = 3

        # Bullets settings
        self.bullet_width = 3 # pixels
        self.bullet_height = 15 # pixels
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # Aliens setinggs
        self.drop_moving_speed = 10

        # Setiap level naik 10%
        self.speed_scale = 1.1

        # Initialize dynamic settings
        self.set_dynamic_settings()

    def set_dynamic_settings(self):
        """ Setting untuk hal yang mungkin berubah sepanjang game """
        self.ship_speed = 1.5
        self.bullet_speed = 2.5
        self.alien_moving_speed = 1.0

        # Bergerak right = 1 ; left = -1
        self.direction = 1

    def increase_speed(self):
        """ Setiap naik level ubah settings dinamisnya """
        self.ship_speed *= self.speed_scale
        self.bullet_speed *= self.speed_scale
        self.alien_moving_speed *= self.speed_scale 