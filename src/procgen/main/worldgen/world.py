from ..sprites import tiles
from ..sprites.map_points import MapPoint
from .roads import Road, Roads


class World:
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

    @classmethod
    def load(cls, world_map):
        world = cls(
            world_map.heightmap.width,
            world_map.heightmap.height,
        )

        for pos, value in world_map.heightmap.values:
            tile = world.tile_by_value(value)
            tile.rect = world_map.tile_map.get_tile(pos)
            world.set_tile(pos, tile)

        world.points = []
        for map_object in world_map.map_points:
            pos = map_object.pos
            point = MapPoint(pos, world_map.tile_map.tile_size)
            point.rect = world_map.tile_map.get_tile(pos)
            world.points.append(point)

        world.roads = Roads()
        for nodes in world_map.road_nodes:
            road = Road(*nodes)
            world.roads.items.append(road)

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
