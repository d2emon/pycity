import pygame


class Screen(pygame.sprite.Sprite):
    # BACKGROUND_IMAGE = "../res/global/map.jpg"
    # BACKGROUND_POS = 0, 0

    def __init__(self, game, *groups):
        super().__init__(*groups)

        self.game = game
 
        self.sprites = pygame.sprite.Group()

        self.load_image()

    @classmethod
    def load_image(self):
        # return pygame.image.load(self.BACKGROUND_IMAGE)
        rect = self.game.window.get_rect()
        self.image = pygame.Surface(rect.size)
        self.rect = rect

    def update(self, *args, **kwargs):
        super().update(*args, **kwargs)

        self.sprites.update(*args, **kwargs)
        self.sprites.draw(self.image)
