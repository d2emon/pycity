import pygame


class ScreenGroup(pygame.sprite.LayeredUpdates):
    def __init__(self, window, *spites):
        super().__init__(*spites)

        self.window = window
        self.rect = window.get_rect()

        self.background = self.create_background()
        self.player = self.create_player()
        self.level = self.create_level()

    def create_background(self):
        return None

    def create_player(self):
        return None

    def create_level(self):
        return None
