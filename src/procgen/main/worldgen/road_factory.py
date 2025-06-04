class RoadData:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    @property
    def width(self):
        return self.end[0] - self.start[0]

    @property
    def height(self):
        return self.end[1] - self.start[1]

    @property
    def line(self):
        # np.array([road[0], road[1]])
        return [self.start, self.end]

    @property
    def points(self):
        samples = 10

        dx = self.width / samples
        dy = self.height / samples
        for i in range(samples + 1):
            x = int(self.start[0] + dx * i)
            y = int(self.start[1] + dy * i)
            yield x, y


class RoadFactory:
    max_road_height = 0.8

    def __init__(self, heightmap):
        self.heightmap = heightmap

    # Validators

    def is_valid_road(self, road):
        for pos in road.points:
            if self.heightmap.get_value(pos) > self.max_road_height or self.heightmap.is_water(pos):
                return False

        return True

    # Road helpers

    def smooth_road(self, road):
        simplified = list(road.line)  # rdp(line, epsilon=2.0)  # Параметр "epsilon" контролирует уровень упрощения
        if len(simplified) > 1:
            return simplified

    @classmethod
    def road_weight(self, city1, city2):
        # city1 = np.argmin([np.linalg.norm(road[0] - p) for p in points])
        # city2 = np.argmin([np.linalg.norm(road[1] - p) for p in points])
        return city1.size + city2.size
