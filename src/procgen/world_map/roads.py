import random
from scipy.spatial import Voronoi


class Road:
    dx = 50
    dy = 50

    def __init__(self, *points, width=3, color=(100, 100, 100)):
        self.width = width
        self.color = color
        self.points = [*points]

    def draw(self, road_map):
        road_map.create_image(self.points, self.color, self.width)

    @classmethod
    def generate_crow(cls, start, end, width=3, color=(100, 100, 100)):
        min_points = 1
        max_points = 3

        points = []
        points.append(start)
        for _ in range(random.randint(min_points, max_points)):
            x = (start[0] + end[0]) // 2 + random.randint(-cls.dx, cls.dx)
            y = (start[1] + end[1]) // 2 + random.randint(-cls.dy, cls.dy)
            points.append((x, y))
        points.append(end)

        return cls(
            *points,
            width=width,
            color=color,
        )

    @classmethod
    def from_road_data(cls, road):
        is_correct = road.metadata.get('is_correct')
        color = (100, 100, 100) if is_correct else (255, 0, 0)
        return cls(*road.nodes, color=color)


class Roads:
    def __init__(self, *items):
        self.items = [*items]

    def draw(self, road_map):
        for item in self.items:
            item.draw(road_map)

    @classmethod
    def generate_crow(cls, points):
        items = []
        for start_id, start in enumerate(points):
            for end in points[start_id + 1:]:
                items.append(Road.generate_crow(start, end, color=(0, 0, 128)))

        return cls(*items)
