class Settings:
    """ Menyimpan semua settings di sini """
    def __init__(self):
        self.width = 800
        self.heigt = 600
        self.bg_color = (230, 230, 230)

        # Ship Settings
        self.ship_speed = 1.5

        # Bullets settings
        self.bullet_speed = 2.0
        self.bullet_width = 3 # pixels
        self.bullet_height = 15 # pixels
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3