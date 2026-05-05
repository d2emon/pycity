import pygame
from . import colors


class Tile(pygame.sprite.Sprite):
    color = colors.WHITE
    is_solid = False

    def __init__(self, size, value=1.0, *groups):
        super().__init__(*groups)

        self.image  = pygame.Surface(size)
        self.rect = self.image.get_rect()

        self.height = value

        self.create_image()

    def create_image(self):
        pygame.draw.rect(self.image, self.color, self.image.get_rect())


class SolidTile(Tile):
    is_solid = True


class Space(Tile):
    color = colors.BLACK


class Water(SolidTile):
    color = colors.BLUE


class Sand(Tile):
    color = colors.KHAKI


class Grass(Tile):
    color = colors.GREEN


class Rock(SolidTile):
    color = colors.BROWN
