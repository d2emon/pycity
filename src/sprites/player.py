import pygame
import directions
from key_input import is_key_pressed
from sprites.map_sprite import MapSprite


min_x = 16 * 32
max_x = 16 * 32 * 2
min_y = 16 * 32
max_y = 16 * 32 * 2


class Player(MapSprite):
    default_movement_speed = 2

    def __init__(self, image, pos, *groups):
        super().__init__(image, pos, *groups)

        self.movement_speed = self.default_movement_speed
        # self.block_map = block_map
        self.last_rect = self.rect.copy()
        
        self.keys = {
            directions.UP: pygame.K_w,
            directions.DOWN: pygame.K_s,
            directions.RIGHT: pygame.K_d,
            directions.LEFT: pygame.K_a,
        }

    def update(self, game_map=None):
        self.last_rect = self.rect.copy()

        if is_key_pressed(self.keys[directions.UP]):
            self.y -= self.movement_speed
        if is_key_pressed(self.keys[directions.LEFT]):
            self.x -= self.movement_speed
        if is_key_pressed(self.keys[directions.DOWN]):
            self.y += self.movement_speed
        if is_key_pressed(self.keys[directions.RIGHT]):
            self.x += self.movement_speed

        # for sprite in pygame.sprite.spritecollide(self, tile_map, False):
        #     if sprite.is_solid:
        #         self.rect = last_rect

        game_map.check_pos(self)

        # if self.rect.top < min_y:
        #     if self.block_map.move(directions.UP):
        #         self.rect.bottom = max_y
        #     else:
        #         self.rect = last_rect
        # if self.rect.bottom > max_y:
        #     if self.block_map.move(directions.DOWN):
        #         self.rect.top = min_y
        #     else:
        #         self.rect = last_rect
        # if self.rect.left < min_x:
        #     if self.block_map.move(directions.LEFT):
        #         self.rect.right = max_x
        #     else:
        #         self.rect = last_rect
        # if self.rect.right > max_x:
        #     if self.block_map.move(directions.RIGHT):
        #         self.rect.left = min_x
        #     else:
        #         self.rect = last_rect
