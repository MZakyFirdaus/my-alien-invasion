import sys 
import pygame 
from time import sleep

from settings import Settings
from ship import Ship
from bullets import Bullets
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import ScoreBoard

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

        # Menyimpan statistik game di self.stats
        self.stats = GameStats(self)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

        # Ketika file dijalan, game otomotasi jalan; "True"
        self.game_active = False

        # Buat play button
        self.play_button = Button(self, 'Play')
        
        # Buat score board
        self.sb = ScoreBoard(self)

    def run_game(self):
        """ Mulai looping untuk game """
        while True:
            self._check_events()

            if self.game_active:
                self.ship.update()
                self._update_aliens()
                self._update_bullets()
            
            self._update_screen()
            self.clock.tick(60) # 60 seconds frame rate
    
    def _check_events(self):
        """  Events of the game  """
        
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
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_play_button(self, mouse_pos):
        """ Start a new game when player clik the plau button """
        click_button = self.play_button.rect.collidepoint(mouse_pos) 
        if click_button and not self.game_active:
            self.settings.set_dynamic_settings()
            self.stats.reset_stats()
            self.sb.prep_score()
            self.sb.prep_level()
            self.sb.prep_ship()
            self.game_active = True

            # Hapus semua remaining fleet and bullets
            self.bullets.empty()
            self.aliens.empty()

            # Creating aliens and center the ship
            self._create_fleet()
            self.ship.center_ship()

            # Hide the cursor when the game is active
            pygame.mouse.set_visible(False)

    def _check_keydown(self, event):
        """ Responsd ketika key press """
        if event.key == pygame.K_RIGHT:
            self.ship.move_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.move_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullets()

    def _check_keyup(self, event):
        """ Respond ketika key release """
        if event.key == pygame.K_RIGHT:
            self.ship.move_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.move_left = False

    def _fire_bullets(self):
        """ Create every new bullets """
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullets = Bullets(self)
            self.bullets.add(new_bullets)

    def _update_bullets(self):
        """ Update position of bullets """
        self.bullets.update()

        # Get rid of bullets
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        
        # Cek apakah bullets dan alien saling bertabrakan
        #   apa tidak. Jika iya, hapus aliens
        self._check_if_collisions()

    def _check_if_collisions(self):
        """ Cek apakah bullets dan alien saling bertabrakan"""
        # Logika bila bullets dan alien bertemu
        #   alien akan hilang
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True)
        
        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)    
            self.sb.prep_score()
            self.sb.check_high_score()
        
        # Transisi ke level selanjutnya
        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()

            # Increase level
            self.stats.level += 1
            self.sb.prep_level()

    def _update_aliens(self):
        """ Menggerakan alien dan cek posisi alien """
        self._check_alien_edges()
        self.aliens.update()

        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        self._check_alien_bottom()
    def _ship_hit(self):
        """ Respond to the ship being hit by an alien. """
        if self.stats.ships_left > 0:
            # Mengurangi sisa ships 
            self.stats.ships_left -= 1
            self.sb.prep_ship()

            # Kosongkan Bullets dan Aliens
            self.bullets.empty()
            self.aliens.empty()

            # Buat armada dan kapal baru
            self._create_fleet()
            self.ship.center_ship()

            # Pause
            sleep(0.5)
        else:
            self.game_active = False
            pygame.mouse.set_visible(True)    

    def _check_alien_bottom(self):
        """ Ngecek apakah alien mencapai bottom atau tidak """
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.settings.heigt:
                self._ship_hit()
                break

    def _create_fleet(self):
        """ Create fleet of aliens """
        # Bikin armada alien sepanjang screen
        # screen - 2 * ukuran alien
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size

        current_x, current_y = alien_width, alien_height
        while current_y < (self.settings.heigt - 3 * alien_height):
            while current_x < (self.settings.width - 2 * alien_width):
                self._create_alien(current_x, current_y)
                current_x += 2 * alien_width
            
            # Reset Posisi x dan menambahkan posisi y
            current_x = alien_width
            current_y += 1.75 * alien_width

    def _create_alien(self, position_x, position_y):
        """ Creating alien """
        new_alien = Alien(self)
        new_alien.x = position_x
        new_alien.rect.x = position_x
        new_alien.rect.y = position_y
        self.aliens.add(new_alien)

    def _check_alien_edges(self):
        """ Cek apakah alien sudah di tepi screen """
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Drop the entire fleet and change the fleet's direction."""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.drop_moving_speed
        self.settings.direction *= -1

    def _update_screen(self):
        """ Update images on the screen, and flip to the new screen """
        # Fill the screen with color
        self.screen.fill(self.settings.bg_color)

        # Draw the object of the game
        for bullet in self.bullets.sprites():
            bullet.draw_bullets()
        self.ship.blitme()
        self.aliens.draw(self.screen)
        self.sb.draw_score()

        # Draw play button
        if not self.game_active:
            self.play_button.draw_button()

        # Display  screen terlihat
        pygame.display.flip()

if __name__ == '__main__':
    # Run the game
    alien_invasion = AlienInvasion()
    alien_invasion.run_game()        