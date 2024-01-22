import pygame 
from pygame.sprite import Sprite 

class Ship(Sprite):
    """ Manage the ship """
    def __init__(self, game):
        """ Initialize the ship and setting its position """
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings
        self.screen_rect = game.screen.get_rect()

        # Load gambar image
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Setting posisi pesawat ketika game dimulai
        self.rect.midbottom = self.screen_rect.midbottom

        # Simpan posisi horizontal pesawat di x
        self.x = float(self.rect.x)

        # Setting movement dgn flag; dimulai dengan posisi diam: False
        self.move_right = False
        self.move_left = False
    
    def center_ship(self):
        """ Centering ship in the middle of the screen """
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
        
    def update(self):
        """ Update posisi kapal berdasarkan movement flag """
        # Cek apakah kapal masih berada di dalam jendela
        if self.move_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.move_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # Update nilai self.rect.x
        self.rect.x = self.x
    

    def blitme(self):
        """ Draw the ship at the current position """
        self.screen.blit(self.image, self.rect)