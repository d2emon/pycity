import logging
import random
import pygame
from sprites.moving import Moving
from breakout.intersect import intersect, COLLIDE_BOTTOM, COLLIDE_HORIZONTAL, COLLIDE_VERTICAL
from .images.ball import draw_ball


class Ball(Moving):
    def __init__(
        self,
        level,
        *groups,
    ):
        image = draw_ball()
        rect = image.get_rect()
        # rect = pygame.Rect(0, 0, 10, 10)
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

    def hit_object(self, edge, speed=(0, 0)):
        logging.debug(f"HIT OBJECT {edge}")
        if edge in COLLIDE_HORIZONTAL:
            self.reverse_x(speed)
        elif edge in COLLIDE_VERTICAL:
            self.reverse_y(speed)

    def check_bricks(self):
        for brick in self.level:
            edge = intersect(self.rect, brick.rect)

            if edge is None:
                continue

            self.hit_object(edge)
            self.level.remove(brick)

            yield brick

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
