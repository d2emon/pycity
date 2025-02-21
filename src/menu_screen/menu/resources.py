import pygame
from resources import GameResources


class MenuResources(GameResources):
    @classmethod
    def load_images(cls):
        cls.logger.debug("Loading images")
        # yield 'background', pygame.image.load("res/global/map.jpg").convert_alpha()
        yield 'background', pygame.image.load("res/global/map.jpg")
