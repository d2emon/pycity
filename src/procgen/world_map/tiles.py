from procgen.main.sprites import tiles
from procgen.main.sprites.map_points import MapPoint
from .tile_map import TileMap


class Tiles:
    def __init__(self, width, height, tile_size):
        self.width = width
        self.height = height
        self.tile_size = tile_size

        self.__tile_map = TileMap(tile_size)
        self.__tiles = [
            [None for _ in range(width)]
            for _ in range(height)
        ]

    # Helpers

    @classmethod
    def int_pos(cls, pos):
        return int(pos[0]), int(pos[1])

    # Validators

    def is_valid_pos(self, pos):
        x, y = pos
        return 0 <= x < self.width and 0 <= y < self.height

    # Getters

    def get_valid_pos(self, pos):
        x, y = self.int_pos(pos)

        if not self.is_valid_pos((x, y)):
            return None

        return x, y

    # Tile methods

    def get_tile(self, pos):
        valid_pos = self.get_valid_pos(pos)

        if valid_pos is None:
            return None

        x, y = valid_pos
        return self.__tiles[y][x]

    def set_tile(self, pos, value):
        valid_pos = self.get_valid_pos(pos)

        if valid_pos is None:
            return

        value.rect = self.__tile_map.get_tile(valid_pos)

        x, y = valid_pos
        self.__tiles[y][x] = value

    def get_tile_by_pos(self, pos):
        tile_pos = self.__tile_map.get_pos(pos)
        return self.get_tile(tile_pos)

    def get_tile_center(self, pos):
        return self.__tile_map.get_center(pos)

    ####

    @classmethod
    def load(cls, heightmap, tile_size):
        tiles = cls(
            heightmap.width,
            heightmap.height,
            tile_size,
        )

        for pos, value in heightmap.values:
            tile = tiles.tile_by_value(value)
            tiles.set_tile(pos, tile)

        return tiles

    @classmethod
    def tile_by_value(cls, value):
        water_level = -0.2
        grass_level = 0
        rock_level = 0.2

        if value < water_level:
            return tiles.Water(value)
        elif value < grass_level:
            return tiles.Sand(value)
        elif value < rock_level:
            return tiles.Grass(value)
        else:
            return tiles.Rock(value)
