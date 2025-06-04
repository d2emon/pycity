import pygame
import config
from procgen.world_map.heightmap import Heightmap
from .map_objects.road import Road as MapRoad
from .map_objects.tree import Oak
from .point_factory import PointFactory
from .points import Points
from .roads import Road, Roads
from .tile_factory import TileFactory
from .tile_map import TileMap
from .voronoi_factory import VoronoiFactory
from .world_map import WorldMap
from ..sprites.map_points import MapPoint


class VoronoiMap:
    tile_map = TileMap(config.TILE_SIZE)
    max_road_height = 0.8

    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.inners = pygame.sprite.Group()
        self.points = pygame.sprite.Group()
        self.roads = Roads()

        self.heightmap = Heightmap(width, height)

    # Helpers

    @classmethod
    def int_pos(cls, pos):
        return int(pos[0]), int(pos[1])

    # Validators

    def is_valid_pos(self, pos):
        x, y = pos
        return 0 <= x < self.width and 0 <= y < self.height

    def is_valid_road(self, start, end):
        samples = 10

        for i in range(samples + 1):
            x = int(start[0] + (end[0] - start[0]) * i / samples)
            y = int(start[1] + (end[1] - start[1]) * i / samples)
            pos = x, y
            if self.height.get_value(pos) > self.max_road_height or self.heightmap.is_water(pos):
                return False

        return True

    # Subitem constructors

    def __create_map_point(self, pos):
        x, y = self.int_pos(pos)

        if not self.is_valid_pos((x, y)):
            return None

        point = MapPoint((x, y), self.tile_map.tile_size)
        point.rect = self.tile_map.get_tile(point.pos)

        return point

    def __create_road(self, *nodes):
        return Road(*nodes)

    def create_inner(self, pos):
        point = self.__create_map_point(pos)
        if point:
            self.inners.add(point)
        return point

    def create_point(self, pos):
        point = self.__create_map_point(pos)
        if point:
            self.points.add(point)
        return point

    def create_road(self, nodes):
        road = self.__create_road(*nodes)
        self.roads.items.append(road)
        return road

    # WorldMap constructors

    @classmethod
    def create_map_object(cls, pos):
        return Oak(None, pos)

    @classmethod
    def create_map_road(cls, start, end):
        start_rect = cls.tile_map.get_tile(start)
        end_rect = cls.tile_map.get_tile(end)

        return MapRoad(None, [start_rect.center, end_rect.center])

    # Loaders

    def load_world_map(self, world_map):
        # self.points.empty()
        for point in world_map.map_points:
            self.create_point(point)

        for road in world_map.road_nodes:
            self.create_road(road)

    # Getters

    def get_tile_rect(self, pos):
        return self.tile_map.get_tile(pos)

    # Road helpers

    def smooth_road(self, road):
        line = list(road) # np.array([road[0], road[1]])
        simplified = list(line)  # rdp(line, epsilon=2.0)  # Параметр "epsilon" контролирует уровень упрощения
        if len(simplified) > 1:
            return simplified

    # Generator

    @classmethod
    def generate(cls, width, height):
        voronoi_map = cls(width, height)

        tile_factory = TileFactory()
        voronoi_map.heightmap = tile_factory.generate(width, height)

        point_factory = PointFactory(width, height)
        centers = point_factory.generate(10)

        voronoi_factory = VoronoiFactory(width, height)
        graph = voronoi_factory.generate(centers)

        world_map = WorldMap(
            width,
            height,
            config.TILE_SIZE,
            # Metadata
            map_name="Voronoi Map",
            generator="VoronoiMapGenerator",
        )
        world_map.objects = [cls.create_map_object(pos) for pos in graph.points]
        world_map.roads = [cls.create_map_road(*ridge) for ridge in graph.ridges]

        voronoi_map.load_world_map(world_map)

        return voronoi_map

    ####

    def road_weight(self, road):
        # city1 = np.argmin([np.linalg.norm(road[0] - p) for p in points])
        # city2 = np.argmin([np.linalg.norm(road[1] - p) for p in points])
        weight = 1.0  # city1.size + city2.size
        return weight
