from procgen.world_map.tiles import Tiles


class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.tiles = None
        self.map_points = []
        self.road_data = None

    @classmethod
    def load(cls, world_map):
        world = cls(
            world_map.heightmap.width,
            world_map.heightmap.height,
        )

        world.tiles = world_map.tiles
        world.map_points = world_map.map_points
        world.road_data = world_map.road_data

        return world
