class GameStats:
    """ Mencatat semua statistik dalam game """

    def __init__(self, game):
        """ Setup awal """
        self.settings = game.settings

        # High Score gaboleh di reset
        self.high_score = 0
        self.reset_stats()

    def reset_stats(self):
        """ Status yang kemungkinan dapat berubah di dalam game """
        self.ships_left = self.settings.ship_limits
        self.score = 0
        self.level = 1