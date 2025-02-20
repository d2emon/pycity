import pygame


class ScreenGroup(pygame.sprite.LayeredUpdates):
    def __init__(self, window, *spites):
        super().__init__(*spites)

        self.window = window
        self.rect = window.get_rect()
