import pygame


class Screen(pygame.sprite.Sprite):
    def __init__(self, game, *groups):
        super().__init__(*groups)

        rect = game.window.get_rect()

        self.image = pygame.Surface(rect.size)
        self.rect = rect
        self.game = game
        self.sprites = pygame.sprite.Group()

    def update(self, *args, **kwargs):
        super().update(*args, **kwargs)

        self.sprites.update(*args, **kwargs)
        self.sprites.draw(self.image)
