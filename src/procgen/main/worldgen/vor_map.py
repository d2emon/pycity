import pygame
import config
from scipy.spatial import Voronoi
from .points import Points
from .roads import Road, Roads
from .world_map import WorldMap
from ..sprites.map_points import MapPoint


class VoronoiMap:
    tile_size = config.TILE_SIZE

    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.inners = pygame.sprite.Group()
        self.points = pygame.sprite.Group()
        self.roads = Roads()

        self.world_map = WorldMap(
            width,
            height,
            self.tile_size,
            # Metadata
            map_name="Voronoi Map",
            generator="VoronoiMapGenerator",
        )

    def add_inner(self, pos):
        x = int(pos[0])
        y = int(pos[1])
        if 0 <= x < self.width and 0 <= y < self.height:
            point = MapPoint((x, y), self.tile_size)
            self.inners.add(point)

    def add_point(self, pos):
        x = int(pos[0])
        y = int(pos[1])
        if 0 <= x < self.width and 0 <= y < self.height:
            point = MapPoint((x, y), self.tile_size)
            self.points.add(point)

    def add_road(self, nodes):
        road = Road(*nodes)
        self.roads.items.append(road)

    def load_world_map(self, world_map):
        for point in world_map.map_points:
            self.add_point(point)

        for road in world_map.road_nodes:
            self.add_road(road)

    def fill_world(self):
        world_map = WorldMap(
            self.width,
            self.height,
            self.tile_size,
            # Metadata
            map_name="Voronoi Map",
            generator="VoronoiMapGenerator",
        )
        world_map.generate_points(10)

        vor = Voronoi(world_map.map_points)
        for point_id, point in enumerate(vor.vertices):
            world_map.add_point(point_id, point)

        for road_id, simplex in enumerate(vor.ridge_vertices):
            if -1 not in simplex:  # Игнорируем рёбра, уходящие в бесконечность
                start = vor.vertices[simplex[0]]
                start_rect = self.get_tile_rect(*start)

                end = vor.vertices[simplex[1]]
                end_rect = self.get_tile_rect(*end)

                world_map.add_road(road_id, [start_rect.center, end_rect.center])

        return world_map

    def fill(self):
        world_map = self.fill_world()
        self.load_world_map(world_map)
        self.world_map = world_map

    @classmethod
    def get_tile_rect(cls, x, y):
        return pygame.Rect(
            int(x) * cls.tile_size,
            int(y) * cls.tile_size,
            cls.tile_size,
            cls.tile_size,
        )
