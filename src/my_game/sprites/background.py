import pygame
from loaders import resources
from .map_sprite import MapSprite


# class Background(Surface):
class Background(MapSprite):
    def __init__(self, size, *groups):
        surface = pygame.Surface(size)
        image = pygame.image.load(resources.BGFILE)

        super().__init__(image, (0, 0), *groups)

        self.surface = surface
        self.image = image

        # surface.blit(image, self.rect)
        # screen.blit(self, self.rect)
