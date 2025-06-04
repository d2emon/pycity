from procgen.world_map.tiles import Tiles
from ..sprites import tiles
from ..sprites.map_points import MapPoint
from .roads import Road, Roads


class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.roads = Roads()

        self.tiles = None
        self.map_points = []

    @classmethod
    def load(cls, world_map):
        world = cls(
            world_map.heightmap.width,
            world_map.heightmap.height,
        )

        world.tiles = Tiles.load(world_map.heightmap, world_map.tile_map)
        world.map_points = world_map.map_points

        world.roads = Roads()
        for nodes in world_map.road_nodes:
            road = Road(*nodes)
            world.roads.items.append(road)

        return world
