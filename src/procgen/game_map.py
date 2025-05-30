import pygame
from tiles import get_tile


class GameMap:
    def __init__(self, world, screen_size, tile_size):
        self.screen_width, self.screen_height = screen_size

        self.tile_size = tile_size

        self.player_pos = [self.screen_width // 2, self.screen_height // 2]
        self.camera_pos = [0, 0]
        self.world = world

    def set_camera(self, screen, pos):
        player_x, player_y = pos

        # Камера следует за игроком
        self.camera_pos[0] = player_x * self.tile_size - screen.get_width() // 2
        self.camera_pos[1] = player_y * self.tile_size - screen.get_height() // 2

    def get_map_rect(self, pos):
        tile_x, tile_y = pos
        camera_x, camera_y = self.camera_pos

        x = tile_x * self.tile_size - camera_x
        y = tile_y * self.tile_size - camera_y

        return x, y

    def __draw_sprite(self, screen, sprite, pos):
        x, y = self.get_map_rect(pos)

        sprite.rect.x = x
        sprite.rect.y = y

        if 0 <= x < self.screen_width and 0 <= y < self.screen_height:
            sprite.draw(screen)

    def fill(self, screen, player):
        for y in range(self.world.height):
            for x in range(self.world.width):
                tile = self.world.get_tile(x, y)
                self.__draw_sprite(screen, tile, (x, y))

        # Игрок
        self.__draw_sprite(screen, player, self.player_pos)
