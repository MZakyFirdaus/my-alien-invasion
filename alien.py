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

        # Load alien image
        self.image = pygame.image.load('images/alien.bmp') # -> Surface
        self.rect = self.image.get_rect() # -> Rect

        # Posisikan setiap alien di pojok kiri atas
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Posisi X
        self.x = float(self.rect.x)

    def check_edges(self):
        """ Cek apabila alien sudah menyentuh sisi kanan """
        screen_rect = self.screen.get_rect()
        return (self.rect.right >= screen_rect.right) or (self.rect.left <= 0)
    
    def update(self):
        """ Membuat alien bergerak ke kanan atau kiri """
        self.x += self.settings.alien_moving_speed * self.settings.direction
        self.rect.x = self.x

    









