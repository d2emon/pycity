from procgen.world_map.tiles import Tiles
from ..sprites import tiles
from ..sprites.map_points import MapPoint
from .roads import Road, Roads


class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.points = []
        self.inners = []
        self.roads = Roads()

        self.tiles = Tiles(width, height)

    @classmethod
    def load(cls, world_map):
        world = cls(
            world_map.heightmap.width,
            world_map.heightmap.height,
        )

        world.tiles = Tiles.load(world_map.heightmap, world_map.tile_map)

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

        return world

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
