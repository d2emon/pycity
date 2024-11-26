import pygame
# from events import Events



class Screen(pygame.sprite.Sprite):
    def __init__(self, rect, *groups):
        super().__init__(*groups)

        self.image = pygame.Surface(rect.size)
        self.rect = rect
        self.sprites = pygame.sprite.Group()

        # self.events = Events()

    def update(self, *args, **kwargs):
        super().update(*args, **kwargs)

        self.sprites.update(*args, **kwargs)
        self.sprites.draw(self.image)
