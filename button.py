import pygame.font
import pygame
class Button:
    """ Class untuk mengatur tombol-tombol dalam game Alien Invasion """

    def __init__(self, game, msg):
        """ Atributes awal button """
        self.settings = game.settings
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()

        #* Ngatur ukuran dan properti button
        self.width, self.height = 200, 50
        self.button_color = (0, 135, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # Ngatur rectangle button
        self.rect = pygame.Rect(0,0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # Pesan button yang harus disiapkan satu kali
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """ Ubah text menjadi rendered image """
        self.msg_render = self.font.render(msg, True, 
                                           self.text_color, self.button_color)
        self.msg_render_rect = self.msg_render.get_rect()
        self.msg_render_rect.center = self.rect.center

    def draw_button(self):
        """ Menampilkan button di screen """
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_render, self.msg_render_rect)


