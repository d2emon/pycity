import logging
import random
import pygame
from sprites.moving import Moving
from breakout.intersect import get_bounds, intersect, COLLIDE_BOTTOM, COLLIDE_HORIZONTAL, COLLIDE_VERTICAL
from .images.ball import draw_ball


class Ball(Moving):
    def __init__(
        self,
        pos,
        bounds,
        *groups,
    ):
        image = draw_ball()

        rect = pygame.Rect(0, 0, 10, 10)
        if pos:
            rect.center = pos

        speed = random.randint(-2, 2), 1

        super().__init__(
            image,
            rect,
            speed,
            *groups,
        )

        self.bounds = bounds
        self.fallen = False

    def update_speed(self, speed=(0, 0)):
        x = self.speed[0] + speed[0]
        y = self.speed[1] + speed[1]
        return x, y

    def reverse_x(self, speed=(0, 0)):
        x, y = self.update_speed(speed)
        self.speed = -x, y

    def reverse_y(self, speed=(0, 0)):
        x, y = self.update_speed(speed)
        self.speed = x, -y

    def hit_object(self, edge, speed=(0, 0)):
        logging.debug(f"HIT OBJECT {edge}")
        if edge in COLLIDE_HORIZONTAL:
            # self.sound_effects['paddle_hit'].play()
            self.reverse_x(speed)
        elif edge in COLLIDE_VERTICAL:
            # self.sound_effects['paddle_hit'].play()
            self.reverse_y(speed)

    def hit_edge(self, edge):
        logging.debug(f"HIT EDGE {edge}")
        if edge == COLLIDE_BOTTOM:
            self.fallen = True
        else:
            self.hit_object(edge)

    def check_bounds(self):
        for edge in get_bounds(self.rect, self.bounds):
            self.hit_edge(edge)

    def check_bricks(self, bricks):
        for brick in bricks:
            edge = intersect(self.rect, brick.rect)

            if edge is None:
                continue

            self.hit_object(edge)
            bricks.remove(brick)

            yield brick
