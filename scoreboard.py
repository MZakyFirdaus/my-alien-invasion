import pygame.font
from pygame.sprite import Group 

from ship import Ship

class ScoreBoard:
    """ Class yang merepresentasikan score dalam game """
    def __init__(self, game):
        """ Initialize class atributes """
        self.game = game
        self.settings = game.settings
        self.stats = game.stats
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()

        #* Atributes boarder
        self.text_color = (50,50,50)
        self.font = pygame.font.SysFont(None, 48)

        #* Draw Text Score
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ship()

    def prep_ship(self):
        """ Shows how many ships left on the game """
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.game)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)

    def prep_level(self):
        """ Rendering Current Level to image """
        level_text = str(self.stats.level)
        self.level_image = self.font.render(level_text, True,
                                            self.text_color,
                                            self.settings.bg_color)
        self.level_image_rect = self.level_image.get_rect()
        self.level_image_rect.right = self.score_rect.right
        self.level_image_rect.top = self.score_rect.bottom + 10

    def prep_high_score(self):
        """ Rendering high score to image """
        high_score = round(self.stats.high_score, -1)
        high_score_text = f"{high_score:,}"
        self.high_score_image = self.font.render(high_score_text, True,
                                                 self.text_color, 
                                                 self.settings.bg_color)
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.screen_rect.top

    def prep_score(self):
        """ Rendering score to image """
        rounded_score = round(self.stats.score, -1)
        score_text = f"{rounded_score:,}"
        self.score_image = self.font.render(score_text, True, 
                                             self.text_color, 
                                             self.settings.bg_color)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def check_high_score(self):
        """ Cek current score against high score """
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()

    def draw_score(self):
        """ Draw the score at right-top of the screen """
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_image_rect)
        self.ships.draw(self.screen)

