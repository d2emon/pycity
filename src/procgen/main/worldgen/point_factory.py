import random


class PointFactory:
    def __init__(self, width, height, seed=1):
        self.width = width
        self.height = height
        self.seed = seed

    def generate(self, count=10):
        random.seed(self.seed)
        for _ in range(count):
            x = random.randrange(0, self.width)
            y = random.randrange(0, self.height)
            yield x, y
