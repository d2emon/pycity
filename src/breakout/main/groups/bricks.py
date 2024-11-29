import logging
import pygame
# from config.games import breakout as config
# from games.breakout.intersect import intersect
from ..sprites.brick import Brick


class Bricks(pygame.sprite.Group):
    width = 7 # 12
    height = 6 # 8

    def __init__(self, *groups):
        super().__init__()

        for y in range(self.height):
            for x in range(self.width):
                Brick((x, y), self, *groups)
