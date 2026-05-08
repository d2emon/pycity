import logging
from procgen.world_map.world import World
from procgen.world_map.map_objects.universe import Supercluster
from procgen.world_map.map_objects.tree import Oak

from .factories.city_factory import CityFactory
from .factories.point_factory import PointFactory
from .factories.road_factory import RoadFactory
from .factories.tile_factory import TileFactory
from .factories.tile_road_factory import TileRoadFactory
from .factories.voronoi_factory import VoronoiFactory

from .nested.universe import UniverseFactory
from .nested.factory import SizeFactory


logger = logging.getLogger('worldgen')


def log_model(model):
    logger.debug("Name:\t\"%s\" (%s) - %s", model.name, model.object_id, model)
    logger.debug("    Factory:\t%s", model.factory)
    logger.debug("    Position:\t%s", model.pos)

    width = f"{model.width}*10^{model.scale}" if model.scale else model.width
    height = f"{model.height}*10^{model.scale}" if model.scale else model.height
    logger.debug("    Size:\t%s, %s", width, height)


def generate_universe(world):
    universe_size_factory = SizeFactory.exact(world.width, world.height)

    universe_factory = UniverseFactory()
    universe_factory.size_factory = universe_size_factory
    universe = universe_factory()
    log_model(universe)

    for supercluster in universe.children:
        log_model(supercluster)
        point = Supercluster(supercluster.object_id, supercluster.pos)
        world.add_point(point)

    return world


def generate_world(world):
    tile_factory = TileFactory()
    world.heightmap = tile_factory.generate(world.width, world.height)

    point_factory = PointFactory(world.width, world.height)
    centers = point_factory.fill(12, 12)

    voronoi_factory = VoronoiFactory(world.width, world.height)
    graph = voronoi_factory(centers)

    road_factory = RoadFactory(world.heightmap)
    tile_road_factory = TileRoadFactory(world.heightmap)
    city_factory = CityFactory(world.heightmap)

    for ridge in graph.ridges:
        for road in tile_road_factory.generate_main_road(ridge):
            world.add_road(None, road)

    for pos in graph.centers:
        for point in city_factory(pos):
            world.add_point(point)

        for road in tile_road_factory.generate_central_road(
            pos,
            # step_min_length=2,
            step_max_length=3,
            branch_prob=0.1,
        ):
            world.add_road(None, road)

    for pos in graph.points:
        for point in city_factory(pos):
            world.add_point(point)

        for road in tile_road_factory.generate_central_road(
            pos,
            step_min_length=2,
            step_max_length=5,
            branch_prob=0.4,
        ):
            world.add_road(None, road)

    return world
