import logging
from procgen.world_map.world import World
from .point_factory import PointFactory
from .road_factory import RoadFactory
from .tile_factory import TileFactory
from .tile_road_factory import generate_roads
from .voronoi_factory import VoronoiFactory

from .nested.universe import UniverseFactory
from .nested.factory import SizeFactory


def log_model(model):
    logging.debug("Model: %s (%s)", model, model.factory)
    logging.debug("Size: (%s, %s) in %s", model.width, model.height, model.pos)
    logging.debug("Name: %s", model.name)


def generate_world(width, height, tile_size):
    world = World(
        width,
        height,
        tile_size,
        # Metadata
        map_name="Voronoi Map",
        generator="VoronoiMapGenerator",
    )

    universe_size_factory = SizeFactory()
    universe_size_factory.min_width = universe_size_factory.max_width = width
    universe_size_factory.min_height = universe_size_factory.max_height = height

    universe_factory = UniverseFactory()
    universe_factory.size_factory = universe_size_factory
    universe = universe_factory()
    log_model(universe)
    for supercluster in universe.children:
        log_model(supercluster)

    tile_factory = TileFactory()
    world.heightmap = tile_factory.generate(width, height)

    point_factory = PointFactory(width, height)
    centers = point_factory.generate_equally()

    voronoi_factory = VoronoiFactory(width, height)
    graph = voronoi_factory.generate(centers)

    road_factory = RoadFactory(world.heightmap)

    for ridge in graph.ridges:
        main_road = road_factory.from_nodes(*ridge)
        for path in generate_roads(main_road, world.heightmap):
            road = road_factory.from_nodes(*path)
            road.weight = 4
            world.add_road(None, road)

    for pos in graph.centers:
        world.add_point(None, pos)
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
            world.add_point(None, pos)
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
