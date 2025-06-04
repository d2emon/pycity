import config
from ..sprites import tiles
from ..sprites.map_points import MapPoint
from .roads import Road, Roads
from .tile_map import TileMap


class World:
    tile_map = TileMap(config.TILE_SIZE)

    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.__tiles = [
            [None for _ in range(width)]
            for _ in range(height)
        ]

        self.points = []
        self.inners = []
        self.roads = Roads()

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

    def load(self, world_map):
        self.width = world_map.heightmap.width
        self.height = world_map.heightmap.height

        for pos, value in world_map.heightmap.values:
            tile = self.tile_by_value(value)
            tile.rect = self.tile_map.get_tile(pos)
            self.set_tile(pos, tile)

        self.points = []
        for map_object in world_map.map_points:
            pos = map_object.pos
            point = MapPoint(pos, self.tile_map.tile_size)
            point.rect = self.tile_map.get_tile(pos)
            self.points.append(point)

        self.roads = Roads()
        for nodes in world_map.road_nodes:
            road = Road(*nodes)
            self.roads.items.append(road)

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
