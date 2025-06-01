import random
import pygame
import config
from ..sprites.map_points import MapPoint


class Points(pygame.sprite.Group):
    size = config.TILE_SIZE

    def add_point(self, pos):
        point = MapPoint(pos, self.size)
        self.add(point)

    def generate(self, width, height, count=5):
        for _ in range(count):
            x = random.randrange(0, width)
            y = random.randrange(0, height)
            self.add_point((x, y))
