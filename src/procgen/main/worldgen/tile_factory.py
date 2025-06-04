import noise
from procgen.world_map.heightmap import Heightmap


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


    def generate_roads(self, width, height):
        roads = [
            [0 for _ in range(width)]
            for _ in range(height)
        ]

        for y in range(height):
            for x in range(width):
                value = noise.pnoise2(
                    x / self.scale,
                    y / self.scale,
                    octaves=3
                )
                if 0.04 < abs(value) < 0.05:  # Узкий диапазон для дорог
                    roads[y][x] = 1

        return roads

    def generate(self, width, height):
        heightmap = Heightmap(width, height)
        heightmap.load([
            [self.generate_tile(x, y) for x in range(width)]
            for y in range(height)
        ])
        return heightmap
