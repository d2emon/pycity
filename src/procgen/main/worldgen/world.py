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

    def get_tile(self, pos):
        x, y = pos

        if y < 0 or y >= self.height or x < 0 or x >= self.width:
            return None

        return self.__items[y][x]

    def set_tile(self, pos, tile):
        x, y = pos
        self.__items[y][x] = tile

    def create_tile(self, pos, value):
        tile = self.tile_by_value(value)
        self.set_tile(pos, tile)
        return tile

    def load(self, world_map):
        for y, row in enumerate(world_map.tiles):
            for x, value in enumerate(row):
                tile = self.create_tile((x, y), value)
                tile.rect = world_map.get_tile_rect((x, y))

        self.points = world_map.points
        self.inners = world_map.inners
        self.roads = world_map.roads

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

    # Генерация карты с помощью шума Перлина
    @classmethod
    def generate_map(cls, width, height):
        world = cls(width, height)

        world_map = VoronoiMap.generate(width, height)
        world.load(world_map)

        return world

