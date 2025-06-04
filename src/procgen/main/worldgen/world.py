from procgen.world_map.heightmap import Heightmap
from ..sprites import tiles
from .vor_map import VoronoiMap


class World(Heightmap):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.__tiles = [
            [None for _ in range(width)]
            for _ in range(height)
        ]

        self.points = None
        self.inners = None
        self.roads = None

    def get_tile(self, pos):
        x, y = pos

        if y < 0 or y >= self.height or x < 0 or x >= self.width:
            return None

        return self.__tiles[y][x]

    def set_tile(self, pos, value):
        x, y = pos

        if y < 0 or y >= self.height or x < 0 or x >= self.width:
            return

        self.__tiles[y][x] = value

    def load_world(self, world_map):
        self.load(world_map.tiles)

        for pos, value in self.values:
            tile = self.tile_by_value(value)
            tile.rect = world_map.get_tile_rect(pos)
            self.set_tile(pos, tile)

        self.points = world_map.points
        self.inners = world_map.inners
        self.roads = world_map.roads

    def generate_voronoi(self):
        world_map = VoronoiMap.generate(self.width, self.height)
        self.load_world(world_map)

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
