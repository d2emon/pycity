import logging
import pygame

from map import TileKindTileset


class TilesetImage:
    def __init__(self, filename):
        logging.debug(f"Loading tileset {filename}")
        self.image = pygame.image.load(filename)
        logging.debug(f"Loaded tileset {filename}")

    def create_tile(self, name, is_solid, area):
        return TileKindTileset(name, is_solid, self.image, area)
