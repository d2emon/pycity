import random
from .map_objects.road import Road
from .map_objects.tree import Oak
from .rpg import RPGMap
from .terrain import Grass, Rock, Water, TerrainData


class WorldMap:
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
        self.terrain = TerrainData(
            Grass,
            Rock,
            Water,
        )
        self.objects = []
        self.zoning = []
        self.roads = []
        self.rpg = RPGMap()

        self.heightmap = None

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
    def map_points(self):
        for map_object in self.objects:
            pos = self.get_valid_pos(map_object.pos)
            if pos:
                map_object.pos = pos
                yield map_object

    @property
    def road_nodes(self):
        return [road.nodes for road in self.roads]

    def add_point(self, object_id, pos):
        point = Oak(object_id, pos)
        self.objects.append(point)
        return point

    def add_road(self, object_id, nodes):
        point = Road(object_id, nodes)
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
