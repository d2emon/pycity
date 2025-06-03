import noise


class TileFactory:
    def __init__(self):
        self.scale = 20.0
        self.octaves = 6
        self.persistence = 0.5
        self.lacunarity = 2.0

    def generate_tile(self, x, y):
        return noise.pnoise2(
            x / self.scale,
            y / self.scale,
            octaves=self.octaves,
            persistence=self.persistence,
            lacunarity=self.lacunarity,
        )

    def generate(self, width, height):
        return [
            [self.generate_tile(x, y) for x in range(width)]
            for y in range(height)
        ]
