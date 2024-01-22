import pygame.font

class ScoreBoard:
    """ Class yang merepresentasikan score dalam game """
    def __init__(self, game):
        """ Initialize class atributes """
        self.settings = game.settings
        self.stats = game.stats
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()

        #* Atributes boarder
        self.text_color = (50,50,50)
        self.font = pygame.font.SysFont(None, 48)

        #* Draw Text Score
        self.prep_score()

    def prep_score(self):
        """ Rendering text to image """
        rounded_score = round(self.stats.score, -1)
        score_text = f"{rounded_score:,}"
        self.score_image = self.font.render(score_text, True, 
                                             self.text_color, 
                                             self.settings.bg_color)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def draw_score(self):
        """ Draw the score at right-top of the screen """
        self.screen.blit(self.score_image, self.score_rect)

