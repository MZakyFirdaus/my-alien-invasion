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
            self._check_events()
            self.ship.update()
            self._update_screen()
            self.clock.tick(60) # 60 seconds frame rate
    
    def _check_events(self):
        #! Events of the game !#
        
        #* Dibawah ini merupakan cek untuk beberapa event di game
        for event in pygame.event.get():
            #? Cek tipe event kalau user klik exit button
            if event.type == pygame.QUIT:
                sys.exit()
            #? Cek type event kalau user klik arrow keyboard
            elif event.type == pygame.KEYDOWN:
                self._check_keydown(event)

            #? Cek type event kalao user tidak klik arrow keyboard
            elif event.type == pygame.KEYUP:
                self._check_keyup(event)
            
    def _update_screen(self):
        # Fill the screen with color
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        # Display  screen terlihat
        pygame.display.flip()
    
    def _check_keydown(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.move_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.move_left = True

    def _check_keyup(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.move_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.move_left = False
if __name__ == '__main__':
    # Run the game
    alien_invasion = AlienInvasion()
    alien_invasion.run_game()        