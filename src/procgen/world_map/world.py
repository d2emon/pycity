import random
from .map_objects.road import Road
from .map_objects.tree import Oak
from .roads import Road as RoadData, Roads
from .rpg import RPGMap
from .terrain import TerrainData
from .tiles import Tiles


class World:
    def __init__(
        self,
        width=255,
        height=255,
        tile_size=8,
        **metadata,
    ):
        # Metadata
        self.width = width
        self.height = height
        self.tile_size = tile_size
        self.__metadata = metadata

        # Layers
        self.terrain = TerrainData()
        self.objects = []
        self.zoning = []
        self.roads = []
        self.rpg = RPGMap()

        self.__heightmap = None
        self.tiles = None

    @property
    def metadata(self):
        return {
            **self.__metadata,
            "tile_size": self.tile_size,
            "width": self.width,
            "height": self.height,
        }

    @property
    def external_links(self):
        return {
            "building_prefabs": "assets/buildings/",
            "rpg_npc_db": "npcs.json"
        }

    @property
    def heightmap(self):
        return self.__heightmap

    @heightmap.setter
    def heightmap(self, value):
        self.__heightmap = value
        self.tiles = Tiles.load(value, self.tile_size)

    @property
    def map_points(self):
        for map_object in self.objects:
            pos = self.get_valid_pos(map_object.pos)
            if pos:
                map_object.pos = pos
                yield map_object

    @property
    def road_nodes(self):
        return [road.nodes for road in self.roads]

    @property
    def road_data(self):
        roads = [RoadData.from_road_data(road) for road in self.roads]
        return Roads(*roads)

    def add_point(self, object_id, pos):
        point = Oak(object_id, pos)
        self.objects.append(point)
        return point

    def add_road(self, object_id, road_data):
        point = Road(object_id, [self.tiles.get_tile_center(point) for point in road_data.nodes], is_correct=road_data.is_correct)
        self.roads.append(point)
        return point

    # Helpers

    @classmethod
    def int_pos(cls, pos):
        return int(pos[0]), int(pos[1])

    # Validators

    def is_valid_pos(self, pos):
        x, y = pos
        return 0 <= x < self.width and 0 <= y < self.height

    # Getters

    def get_valid_pos(self, pos):
        x, y = self.int_pos(pos)

        if not self.is_valid_pos((x, y)):
            return None

        return x, y
