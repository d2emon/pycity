import logging
import pygame
import directions
import events.keys
from sprites.moving import Moving
# from games.breakout.intersect import intersect
from .images.paddle import draw_paddle
from .ball import Ball


class Paddle(Moving):
    def __init__(
        self,
        pos,
        base_speed=10,
        *groups,
    ):
        image = draw_paddle()

        rect = pygame.Rect(300, 400, 80, 20)
        if pos:
            rect.center = pos

        super().__init__(
            image,
            rect,
            (0, 0),
            *groups,
        )
        
        self.keys = {
            directions.RIGHT: pygame.K_RIGHT,
            directions.LEFT: pygame.K_LEFT,
        }

        self.ball = None
        self.__base_speed = base_speed
        self.speed = 0, 0

        # self.lives = 5
        # self.score = 0

    def move_left(self):
        self.speed = -self.__base_speed, 0

    def move_right(self):
        self.speed = self.__base_speed, 0

    def stop(self):
        self.speed = 0, 0

    def start(self, pos, speed, *groups):
        self.ball = Ball(pos, speed, *groups)

    def update(self, *args, **kwargs):
        self.speed = 0, 0
        if events.keys.is_key_pressed(self.keys[directions.LEFT]):
            self.move_left()
        if events.keys.is_key_pressed(self.keys[directions.RIGHT]):
            self.move_right()

        super().update(*args, **kwargs)

        # if self.ball is None:
        #     return

        # if self.ball.fallen:
        #     return self.loose()

        # edge = intersect(self.ball.rect, self.rect)
        # if edge is not None:
        #     # self.sound_effects['paddle_hit'].play()
        #     self.ball.hit_paddle(edge, self.speed)


"""
class Paddle(Moving):
    @property
    def has_started(self):
        return self.ball is not None

    @property
    def game_over(self):
        return self.lives <= 0

    def loose(self):
        # self.sound_effects['paddle_hit'].play()
        self.lives -= 1
        self.ball = None
"""
