import pygame


class Tile:
    color_name = "white"

    def __init__(self, size):
        self.rect = pygame.Rect(0, 0, size, size)

    @property
    def color(self):
        return pygame.Color(self.color_name)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)


class Water(Tile):
    color_name = 'blue'


class Sand(Tile):
    color_name = 'khaki'


class Grass(Tile):
    color_name = 'green'


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
