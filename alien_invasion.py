import sys 
import pygame 
from settings import Settings
from ship import Ship

class AlienInvasion:
    """ Merepresentasikan secara keseluruhan game """
    def __init__(self):
        """ Basic Settings ketika game berjalan """
        #* Setting screen windows
        pygame.init()
        self.settings = Settings()
        self.clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode(
            (self.settings.width, self.settings.heigt))
        pygame.display.set_caption("Alien Invasion Game")

        self.ship = Ship(self)

    def run_game(self):
        """ Start the main loop of the game """
        while True:
            # Events of the game
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Fill the screen with color
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()

            # Display  screen terlihat
            pygame.display.flip()
            self.clock.tick(60) # 60 seconds frame rate

if __name__ == '__main__':
    # Run the game
    alien_invasion = AlienInvasion()
    alien_invasion.run_game()        