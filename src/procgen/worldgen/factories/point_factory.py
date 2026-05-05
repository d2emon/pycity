import random
from .factory import Factory


class PointFactory(Factory):
    def __init__(self, width, height, seed=1):
        self.width = width
        self.height = height
        self.seed = seed

        self.reset()

    def reset(self):
        random.seed(self.seed)

    def __call__(self, *args, **kwargs):
        x = random.randrange(0, self.width)
        y = random.randrange(0, self.height)
        yield x, y

    def fill(self, dx=12, dy=12):
        for x in range(0, self.width, dx):
            for y in range(0, self.height, dy):
                yield x, y
