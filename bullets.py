import pygame 
from pygame.sprite import Sprite

class Bullets(Sprite):
    """ Konfigurasi Bullets ada dalam kelas ini """

    def __init__(self, game):
        """ 
        Create a bullet object at ships current position

        Parameter:
        game: Objek game dari Alien Invasion
        """
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings
        self.bullet_color = self.settings.bullet_color

        # Menentukan posisi awal peluru 
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width
                                , self.settings.bullet_height)
        self.rect.midtop = game.ship.rect.midtop

        # posisi awal bullets
        self.y = float(self.rect.y)

    def update(self):
        """ Menggerakan posisi bullets ke atas """
        # Secara terus-menerus menembakkan peluru ke atas
        self.y -= self.settings.bullet_speed

        # Update posisi
        self.rect.y = self.y

    def draw_bullets(self):
        """ Finishing untuk menggambarkan bullets """
        pygame.draw.rect(self.screen, self.bullet_color, self.rect)

    