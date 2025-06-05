from procgen.world_map.world import World
from .point_factory import PointFactory
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

    for ridge in graph.ridges:
        world.add_road(None, ridge)

    return world
