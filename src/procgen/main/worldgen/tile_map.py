import pygame


class TileMap:
    def __init__(self, tile_size):
        self.tile_size = tile_size

    def get_tile(self, pos):
        tile_x, tile_y = pos
        return pygame.Rect(
            tile_x * self.tile_size,
            tile_y * self.tile_size,
            self.tile_size,
            self.tile_size,
        )

    def get_pos(self, pos):
        x, y = pos
        tile_x = x // self.tile_size
        tile_y = y // self.tile_size
        return tile_x, tile_y
