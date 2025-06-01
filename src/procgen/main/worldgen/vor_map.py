import pygame
import config
from scipy.spatial import Voronoi
from .points import Points
from .roads import Road, Roads


class WorldMap:
    tile_size = config.TILE_SIZE

    def __init__(self):
        self.inners = Points()
        self.points = Points()
        self.roads = Roads()

    @classmethod
    def get_tile_rect(cls, x, y):
        return pygame.Rect(
            int(x) * cls.tile_size,
            int(y) * cls.tile_size,
            cls.tile_size,
            cls.tile_size,
        )

    @classmethod
    def generate(cls, width, height):
        world = cls()
        world.inners.generate(width, height)

        points = [point.pos for point in world.inners]
        vor = Voronoi(points)

        for point in points:
            world.inners.add_point(point)

        for point in vor.vertices:
            x = int(point[0])
            y = int(point[1])
            if 0 <= x < width and 0 <= y < height:
                world.points.add_point((x, y))

        for simplex in vor.ridge_vertices:
            if -1 not in simplex:  # Игнорируем рёбра, уходящие в бесконечность
                start = vor.vertices[simplex[0]]
                start_rect = cls.get_tile_rect(*start)
                
                end = vor.vertices[simplex[1]]
                end_rect = cls.get_tile_rect(*end)

                world.roads.items.append(Road(start_rect.center, end_rect.center))

        return world
