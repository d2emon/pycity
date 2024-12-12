import pygame


class ScreenGroup(pygame.sprite.LayeredUpdates):
    def __init__(self, game, *spites):
        super().__init__(*spites)

        self.game = game


class Screen(pygame.sprite.Sprite):
    def __init__(self, game, *groups):
        super().__init__(*groups)

        self.game = game
        self.sprites = self.create_group()

        self.load_image()

    def create_group(self):
        return ScreenGroup(self.game)

    def load_image(self):
        rect = self.game.window.get_rect()
        self.image = pygame.Surface(rect.size)
        self.rect = rect

    def update(self, *args, **kwargs):
        super().update(*args, **kwargs)

        self.sprites.update(*args, **kwargs)
        self.sprites.draw(self.image)
