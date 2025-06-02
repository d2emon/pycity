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

    def get_map_rect(self, tile_x, tile_y, camera_pos):
        camera_x, camera_y = camera_pos

        x = tile_x * self.tile_size - camera_x
        y = tile_y * self.tile_size - camera_y

        return x, y

    def fill(self, camera_pos):
        self.empty()

        self.road_map.rect.topleft = self.get_map_rect(0, 0, camera_pos)
        self.add(self.road_map)
