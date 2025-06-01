import random


class Road:
    dx = 50
    dy = 50

    def __init__(self, width=3, color=(100, 100, 100)):
        self.width = width
        self.color = color
        self.points = []

    def generate(self, start, end):
        min_points = 1
        max_points = 3

        self.points = [start]

        for _ in range(random.randint(min_points, max_points)):
            x = (start[0] + end[0]) // 2 + random.randint(-self.dx, self.dx)
            y = (start[1] + end[1]) // 2 + random.randint(-self.dy, self.dy)
            self.points.append((x, y))

        self.points.append(end)

    def draw(self, road_map):
        road_map.create_image(self.points, self.color, self.width)


class Roads:
    def __init__(self, *items):
        self.items = [*items]

    @classmethod
    def generate(cls, points):
        items = []

        for start_id, start in enumerate(points):
            for end in points[start_id + 1:]:
                road = Road()
                road.generate(start, end)
                items.append(road)

        return cls(*items)

    def draw(self, road_map):
        for item in self.items:
            item.draw(road_map)

