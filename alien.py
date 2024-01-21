import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """ Represents Aliens On the game """

    def __init__(self, game):
        """ Attributes awal dari alien """
        super().__init__()

        # Setup Windows settings
        self.settings = game.settings
        self.screen = game.screen # -> Surface
        self.screen_rect = self.screen.get_rect() # -> Rect

        # Load alien image
        self.image = pygame.image.load('images/alien.bmp') # -> Surface
        self.rect = self.image.get_rect() # -> Rect

        # Cari tau posisi rect Alien di pojok kiri atas
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Posisi X
        self.x = float(self.rect.x)








