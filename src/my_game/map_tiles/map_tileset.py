class MapTileset:
    def __init__(self, tiles, size=64):
        self.size = size
        self.tiles = tiles

    def get_tile(self, tile_id):
        tile = self.tiles.get(tile_id)

        if tile is None:
            return self.tiles['01']

        return tile

    def fill_row(self, data):
        for block_code in data:
            yield self.get_tile(block_code)

    def fill(self, data):
        for row in data:
            yield list(self.fill_row(row))
