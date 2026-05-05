from procgen.main.sprites import tiles
from procgen.main.sprites.map_points import MapPoint
from .tiles import by_value
from ..tile_map import TileMap
from ..tiles import Tiles


class SpaceTiles(Tiles):
    def set_tile_by_value(self, pos, value):
        tile = by_value(self.tile_size, value)
        self.set_tile(pos, tile)
