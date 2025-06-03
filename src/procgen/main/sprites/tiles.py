import pygame
import config


class Tile(pygame.sprite.Sprite):
    color_name = "white"
    is_solid = False
    size = config.TILE_SIZE

    def __init__(self, *groups):
        super().__init__(*groups)

        self.image  = pygame.Surface((self.size, self.size))
        self.rect = self.image.get_rect()

        self.create_image()

    @property
    def color(self):
        return pygame.Color(self.color_name)

    def create_image(self):
        pygame.draw.rect(self.image, self.color, self.image.get_rect())


class Water(Tile):
    color_name = 'blue'
    is_solid = True


class Sand(Tile):
    color_name = 'khaki'


class Grass(Tile):
    color_name = 'green'


class Rock(Tile):
    color_name = 'brown'
    is_solid = True
