import noise
from .sprites import tiles


class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.__items = []
        for y in range(height):
            row = []
            for x in range(width):
                row.append(None)
            self.__items.append(row)

    def get_tile(self, x, y):
        return self.__items[y][x]

    def set_tile(self, x, y, tile):
        self.__items[y][x] = tile

    # Генерация карты с помощью шума Перлина
    @classmethod
    def generate_map(cls, width, height, tile_size):
        water_level = -0.25  # -0.05
        grass_level = 0.05
        rock_level = 0.2
        scale = 20.0
        world = cls(width, height)
        for y in range(height):
            for x in range(width):
                value = noise.pnoise2(x / scale, y / scale, octaves=6)

                if value < water_level:
                    tile = tiles.Water(tile_size)
                elif value < grass_level:
                    tile = tiles.Sand(tile_size)
                elif value < rock_level:
                    tile = tiles.Grass(tile_size)
                else:
                    tile = tiles.Rock(tile_size)

                world.set_tile(x, y, tile)
        return world


