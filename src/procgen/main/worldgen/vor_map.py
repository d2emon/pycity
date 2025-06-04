import pygame
import config
from procgen.world_map.heightmap import Heightmap
from .point_factory import PointFactory
from .roads import Road, Roads
from .tile_factory import TileFactory
from .tile_map import TileMap
from .voronoi_factory import VoronoiFactory
from .world_map import WorldMap


class VoronoiMap:
    tile_map = TileMap(config.TILE_SIZE)

    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.points = []
        self.roads = Roads()

        self.heightmap = Heightmap(width, height)

    # Subitem constructors

    def create_road(self, nodes):
        road = Road(*nodes)
        self.roads.items.append(road)
        return road

    # Getters

    def get_tile_rect(self, pos):
        return self.tile_map.get_tile(pos)

    # Generator

    @classmethod
    def generate(cls, width, height):
        world_map = WorldMap(
            width,
            height,
            config.TILE_SIZE,
            # Metadata
            map_name="Voronoi Map",
            generator="VoronoiMapGenerator",
        )

        tile_factory = TileFactory()
        world_map.heightmap = tile_factory.generate(width, height)

        point_factory = PointFactory(width, height)
        centers = point_factory.generate(10)

        voronoi_factory = VoronoiFactory(width, height)
        graph = voronoi_factory.generate(centers)

        for pos in graph.points:
            world_map.add_point(None, pos)

        for ridge in graph.ridges:
            world_map.add_road(
                None,
                [cls.tile_map.get_center(point) for point in ridge],
            )

        voronoi_map = cls(width, height)
        voronoi_map.heightmap = world_map.heightmap
        voronoi_map.points = world_map.map_points
        for road in world_map.road_nodes:
            voronoi_map.create_road(road)

        return voronoi_map
