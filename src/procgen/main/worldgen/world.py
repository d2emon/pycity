import noise
from ..sprites import tiles
from .vor_map import VoronoiMap


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

        self.points = None
        self.inners = None
        self.roads = None

    def get_tile(self, x, y):
        if y < 0 or y >= self.height or x < 0 or x >= self.width:
            return None

        return self.__items[y][x]

    def set_tile(self, x, y, tile):
        self.__items[y][x] = tile

    def generate_road_mask(self, scale=20.0):
        road_mask = [[0 for _ in range(self.width)] for _ in range(self.height)]
        for y in range(self.height):
            for x in range(self.width):
                value = noise.pnoise2(x/scale, y/scale, octaves=3)
                if abs(value) < 0.05:  # Узкий диапазон для дорог
                    road_mask[y][x] = 1
        return road_mask

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

        world_map = VoronoiMap(width, height)

        for tile_data in world_map.fill_tiles():
            pos, value, rect = tile_data
            tile = cls.create_tile(value, tile_size)
            tile.rect = rect
            world.set_tile(pos[0], pos[1], tile)

        world_map.fill()

        world.points = world_map.points
        world.inners = world_map.inners
        world.roads = world_map.roads

        return world

