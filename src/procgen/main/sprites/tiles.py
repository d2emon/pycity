import pygame


class Tile(pygame.sprite.Sprite):
    color_name = "white"
    is_solid = False

    def __init__(self, size, *groups):
        super().__init__(*groups)

        self.image  = pygame.Surface((size, size))
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

tiles = {
    'water': Water,
    'sand': Sand,
    'grass': Grass,
}


def get_tile(tile_id, size):
    tile = tiles[tile_id]
    if tile is None:
        return None

    return tile(size)
