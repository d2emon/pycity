import config
from .point_factory import PointFactory
from .tile_factory import TileFactory
from .tile_map import TileMap
from .voronoi_factory import VoronoiFactory
from .world_map import WorldMap


def generate_world(width, height, tile_size):
    tile_map = TileMap(tile_size)

    world_map = WorldMap(
        width,
        height,
        tile_size,
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
            [tile_map.get_center(point) for point in ridge],
        )

    return world_map
