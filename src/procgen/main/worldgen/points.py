import random
import pygame
import config
from ..sprites.map_points import MapPoint


class Points(pygame.sprite.Group):
    size = config.TILE_SIZE

    def generate(self, width, height, count=10):
        for _ in range(count):
            x = random.randrange(0, width)
            y = random.randrange(0, height)

            point = MapPoint((x, y), self.size)
            self.add(point)
