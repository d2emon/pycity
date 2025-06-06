from procgen.world_map.world import World
from .point_factory import PointFactory
from .road_factory import RoadFactory
from .tile_factory import TileFactory
from .voronoi_factory import VoronoiFactory


def generate_world(width, height, tile_size):
    world = World(
        width,
        height,
        tile_size,
        # Metadata
        map_name="Voronoi Map",
        generator="VoronoiMapGenerator",
    )

    tile_factory = TileFactory()
    world.heightmap = tile_factory.generate(width, height)

    point_factory = PointFactory(width, height)
    centers = point_factory.generate(10)

    voronoi_factory = VoronoiFactory(width, height)
    graph = voronoi_factory.generate(centers)

    for pos in graph.points:
        world.add_point(None, pos)

    road_factory = RoadFactory(world.heightmap)

    for ridge in graph.ridges:
        road = road_factory.from_nodes(*ridge)
        world.add_road(None, road)

    for center in graph.centers:
        for road in road_factory.generate_from_center(
            center,
            step_max_length=3,
            branch_prob=0.1,
        ):
            world.add_road(None, road)

    for center in graph.points:
        for road in road_factory.generate_from_center(
            center,
            step_min_length=2,
            step_max_length=5,
            branch_prob=0.4,
        ):
            world.add_road(None, road)

    return world
