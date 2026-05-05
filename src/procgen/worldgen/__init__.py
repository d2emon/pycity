import logging
from procgen.world_map.world import World
from procgen.world_map.map_objects.universe import Supercluster
from procgen.world_map.map_objects.tree import Oak

from .factories.point_factory import PointFactory
from .factories.road_factory import RoadFactory
from .factories.tile_factory import TileFactory
from .factories.tile_road_factory import generate_roads
from .factories.voronoi_factory import VoronoiFactory

from .nested.universe import UniverseFactory
from .nested.factory import SizeFactory



logger = logging.getLogger('worldgen')


def log_model(model):
    logger.debug("Name:\t%s <%s>", model.name, model.object_id)
    logger.debug("Model:\t%s (%s)", model, model.factory)
    logger.debug("Size:\t(%s, %s) in %s", model.width, model.height, model.pos)


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

    # tile_factory = TileFactory()
    # world.heightmap = tile_factory.generate(world.heightmap)

    return world


def generate_world(world):
    tile_factory = TileFactory()
    world.heightmap = tile_factory.generate(world.width, world.height)

    point_factory = PointFactory(world.width, world.height)
    centers = point_factory.generate_equally()

    voronoi_factory = VoronoiFactory(world.width, world.height)
    graph = voronoi_factory.generate(centers)

    road_factory = RoadFactory(world.heightmap)

    for ridge in graph.ridges:
        main_road = road_factory.from_nodes(*ridge)
        for path in generate_roads(main_road, world.heightmap):
            road = road_factory.from_nodes(*path)
            road.weight = 4
            world.add_road(None, road)

    for pos in graph.centers:
        point = Oak(None, pos)
        world.add_point(point)
        if world.heightmap.is_valid(pos):
            for road in road_factory.generate_from_center(
                pos,
                step_max_length=3,
                branch_prob=0.1,
            ):
                for path in generate_roads(road, world.heightmap):
                    subroad = road_factory.from_nodes(*path)
                    world.add_road(None, subroad)

    for pos in graph.points:
        if world.heightmap.is_valid(pos):
            point = Oak(None, pos)
            world.add_point(point)
            for road in road_factory.generate_from_center(
                pos,
                step_min_length=2,
                step_max_length=5,
                branch_prob=0.4,
            ):
                for path in generate_roads(road, world.heightmap):
                    subroad = road_factory.from_nodes(*path)
                    world.add_road(None, subroad)

    return world
