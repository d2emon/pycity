import logging
import pygame
from .images.brick import draw_brick


class Brick(pygame.sprite.Sprite):
    width = 80
    height = 20

    margin_h = 1
    margin_v = 1

    offset_x = 10
    offset_y = 10

    cell_width = width + margin_h
    cell_height = height + margin_v

    def __init__(self, pos, *groups):
        super().__init__(*groups)

        self.image = draw_brick()

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        if pos:
            x, y = pos
            self.rect.x = self.offset_x + x * self.cell_width
            self.rect.y = self.offset_y + y * self.cell_height

        # self.effect = effect
        self.points = 10
