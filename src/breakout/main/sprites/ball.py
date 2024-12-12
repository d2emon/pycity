import random
import pygame
from sprites.moving import Moving
from sprites.solid import Solid
from breakout.intersect import intersect, COLLIDE_BOTTOM, COLLIDE_HORIZONTAL, COLLIDE_VERTICAL
from .images.ball import draw_ball


class Ball(Moving, Solid):
    def __init__(
        self,
        level,
        *groups,
    ):
        image = draw_ball()
        rect = image.get_rect()
        rect.center = level.start_pos

        speed = random.randint(-2, 2), 1

        super().__init__(
            image,
            rect,
            speed,
            *groups,
        )

        self.level = level
        self.fallen = False

    def update_speed(self, speed=(0, 0)):
        x = self.speed[0] + speed[0]
        y = self.speed[1] + speed[1]
        return x, y

    def reverse_x(self, speed=(0, 0)):
        # self.sound_effects['paddle_hit'].play()
        x, y = self.update_speed(speed)
        self.speed = -x, y

    def reverse_y(self, speed=(0, 0)):
        # self.sound_effects['paddle_hit'].play()
        x, y = self.update_speed(speed)
        self.speed = x, -y

    def hit_object(self, item):
        edge = intersect(self.rect, item.rect)
        speed = item.speed if isinstance(item, Moving) else (0, 0)

        if edge is None:
            return

        if edge in COLLIDE_HORIZONTAL:
            self.reverse_x(speed)
        elif edge in COLLIDE_VERTICAL:
            self.reverse_y(speed)

    def update(self, *args, **kwargs):
        super().update(*args, **kwargs)

        if self.rect.left <= self.level.left:
            self.reverse_x()
        if self.rect.top <= self.level.top:
            self.reverse_y()
        if self.rect.right >= self.level.right:
            self.reverse_x()
        if self.rect.bottom >= self.level.bottom:
            self.fallen = True
