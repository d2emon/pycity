import noise
import tiles


class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.items = []
        for y in range(height):
            row = []
            for x in range(width):
                row.append(None)
            self.items.append(row)

    # Генерация карты с помощью шума Перлина
    @classmethod
    def generate_map(cls, width, height, tile_size):
        scale = 20.0
        world = cls(width, height)
        for y in range(height):
            for x in range(width):
                value = noise.pnoise2(x / scale, y / scale, octaves=6)
                if value < -0.05:
                    tile = tiles.Water(tile_size)
                elif value < 0.1:
                    tile = tiles.Sand(tile_size)
                else:
                    tile = tiles.Grass(tile_size)
                world.items[x][y] = tile
        return world


