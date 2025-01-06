from blocks import block_files
from .map_block import MapBlock


class BlockTileset:
    def __init__(self, tilemap):
        self.tiles = [
            MapBlock(filename, tilemap)
            for filename in block_files
        ]

    def fill_row(self, data):
        for block_code in data:
            yield self.tiles[block_code]

    def fill(self, data):
        for row in data:
            print(row)
            yield list(self.fill_row(row))
