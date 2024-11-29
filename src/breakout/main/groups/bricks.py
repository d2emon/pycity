import logging
import pygame
# from config.games import breakout as config
# from games.breakout.intersect import intersect
from ..sprites.brick import Brick


class Bricks(pygame.sprite.Group):
    width = 7 # 12
    height = 6 # 8

    def __init__(self, rect, *groups):
        super().__init__()

        self.top = rect.top
        self.bottom = rect.bottom
        self.left = rect.left
        self.right = rect.right

        self.start_pos = rect.center

        self.rect = rect

        for y in range(self.height):
            for x in range(self.width):
                Brick((x, y), self, *groups)
