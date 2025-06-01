import random
import noise
from .sprites import tiles
from .sprites.map_points import MapPoint


class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.__items = []
        for _ in range(height):
            row = []
            for _ in range(width):
                row.append(None)
            self.__items.append(row)

        self.points = []

    def get_tile(self, x, y):
        if y < 0 or y >= self.height or x < 0 or x >= self.width:
            return None

        return self.__items[y][x]

    def set_tile(self, x, y, tile):
        self.__items[y][x] = tile

    @classmethod
    def create_tile(cls, value, size):
        water_level = -0.2
        grass_level = 0
        rock_level = 0.2

        if value < water_level:
            return tiles.Water(size)
        elif value < grass_level:
            return tiles.Sand(size)
        elif value < rock_level:
            return tiles.Grass(size)
        else:
            return tiles.Rock(size)

    # Генерация карты с помощью шума Перлина
    @classmethod
    def generate_map(cls, width, height, tile_size):
        scale = 20.0
        octaves = 6
        persistence = 0.5
        lacunarity = 2.0

        world = cls(width, height)
        for y in range(height):
            for x in range(width):
                value = noise.pnoise2(
                    x / scale,
                    y / scale,
                    octaves=octaves,
                    persistence=persistence,
                    lacunarity=lacunarity,
                )

                tile = cls.create_tile(value, tile_size)
                world.set_tile(x, y, tile)


        for _ in range(10):
            x = random.randrange(0, width)
            y = random.randrange(0, height)

            point = MapPoint((x, y), tile_size)
            world.points.append(point)

        return world

