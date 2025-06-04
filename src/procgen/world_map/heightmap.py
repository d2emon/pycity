class Heightmap:
    water_level = -0.2

    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.__items = [
            [0.0 for _ in range(width)]
            for _ in range(height)
        ]

    def get_value(self, pos):
        x, y = pos

        if y < 0 or y >= self.height or x < 0 or x >= self.width:
            return 0.0

        return self.__items[y][x]

    def set_value(self, pos, value):
        x, y = pos

        if y < 0 or y >= self.height or x < 0 or x >= self.width:
            return

        self.__items[y][x] = value

    def is_water(self, pos):
        return self.get_value(pos) > self.water_level

    def load(self, data):
        for y, row in enumerate(data):
            for x, value in enumerate(row):
                self.set_value((x, y), value)

    @property
    def values(self):
        for y in range(self.height):
            for x in range(self.width):
                yield (x, y), self.get_value((x, y))
