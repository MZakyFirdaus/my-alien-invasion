import pygame 

class Ship:
    """ Manage the ship """
    def __init__(self, game):
        """ Initialize the ship and setting its position """
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()

        # Load gambar image
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Setting posisi pesawat ketika game dimulai
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """ Draw the ship at the current position """
        self.screen.blit(self.image, self.rect)