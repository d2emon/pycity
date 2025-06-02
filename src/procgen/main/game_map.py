import pygame
from .sprites.road_map import RoadMap


class GameMap(pygame.sprite.Group):
    def __init__(self, world, screen_size, tile_size):
        super().__init__()

        self.screen_width, self.screen_height = screen_size

        self.tile_size = tile_size

        self.world = world
        self.road_map = RoadMap(world.width * tile_size, world.height * tile_size)

        world.roads.draw(self.road_map)
