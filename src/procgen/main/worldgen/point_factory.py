import random


class PointFactory:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def generate(self, count=10):
        for _ in range(count):
            x = random.randrange(0, self.width)
            y = random.randrange(0, self.height)
            yield x, y
