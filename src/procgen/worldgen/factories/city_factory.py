from procgen.world_map.map_objects.tree import Oak
from .factory import Factory


class CityFactory(Factory):
    def __init__(self, heightmap):
        self.heightmap = heightmap

    def __call__(self, pos, *args, **kwargs):
        if world.heightmap.is_valid(pos):
            point = Oak(None, pos)
            yield point
