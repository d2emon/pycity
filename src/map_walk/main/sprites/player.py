"""Player sprite.

Typical usage example:

  player = Player((0, 0))
"""
import pygame
import directions
import events.keys
from sprites.solid import Solid
from .images.player import draw_player
from .. import data


class Player(Solid):
    def __init__(
        self,
        pos,
        base_speed=10,
        *groups,
    ):
        super().__init__(*groups)
        
        self.image = draw_player(data.SCALE)

        self.rect = self.image.get_rect()
        if pos:
            self.rect.center = pos

        self.keys = {
            directions.RIGHT: pygame.K_RIGHT,
            directions.LEFT: pygame.K_LEFT,
            directions.UP: pygame.K_UP,
            directions.DOWN: pygame.K_DOWN,
        }

        self.level = None

        self.speed = 0, 0
        self.__base_speed = base_speed

    # Getters

    @property
    def has_started(self):
        return self.level is not None

    # Actions

    def move_left(self):
        self.speed = -self.__base_speed, 0

    def move_right(self):
        self.speed = self.__base_speed, 0

    def move_up(self):
        self.speed = 0, -self.__base_speed

    def move_down(self):
        self.speed = 0, self.__base_speed

    def stop(self):
        self.speed = 0, 0

    def start(self, level):
        self.level = level

    def update(self, *args, **kwargs):
        self.stop()
        if self.has_started:
            if events.keys.is_key_pressed(self.keys[directions.LEFT]):
                self.move_left()
            if events.keys.is_key_pressed(self.keys[directions.RIGHT]):
                self.move_right()
            if events.keys.is_key_pressed(self.keys[directions.UP]):
                self.move_up()
            if events.keys.is_key_pressed(self.keys[directions.DOWN]):
                self.move_down()

            # if self.rect.left <= self.level.left:
            #     self.rect.left = self.level.left
            # if self.rect.right >= self.level.right:
            #     self.rect.right = self.level.right

            self.level.move(*self.speed)

            #     items = self, *self.level

            #     for item in self.ball.get_collides(items):
            #         self.ball.hit_object(item)
            #         if isinstance(item, Brick):
            #             self.score += item.points
            #             self.level.remove(item)

        super().update(*args, **kwargs)
