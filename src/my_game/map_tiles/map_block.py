import pygame
from loaders.load_map import load_map_block


min_x = 16 * 32
max_x = 16 * 32 * 2
min_y = 16 * 32
max_y = 16 * 32 * 2


class MapBlock:
    def __init__(self, block_file, tileset):
        self.tile_size = tileset.size

        data = load_map_block(block_file)
        self.tiles = list(tileset.fill(data))

    def update(self, x_offset, y_offset, *groups):
        for y, row in enumerate(self.tiles):
            for x, tile in enumerate(row):
                image = tile.image
                pos = (
                    x_offset + x * self.tile_size,
                    y_offset + y * self.tile_size,
                )
                sprite = pygame.sprite.Sprite(*groups)
                sprite.image = image
                sprite.rect = image.get_rect()
                sprite.rect.topleft = pos
                sprite.is_solid = tile.is_solid
