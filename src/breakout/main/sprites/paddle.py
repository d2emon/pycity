import pygame
import directions
import events.keys
from sprites.moving import Moving
from sprites.solid import Solid
from .images.paddle import draw_paddle
from .ball import Ball
from .brick import Brick


class Paddle(Moving, Solid):
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

        self.ball_group = pygame.sprite.GroupSingle()
        self.level = None

        self.__base_speed = base_speed

        self.lives = 5
        self.score = 0

    # Getters

    @property
    def ball(self):
        return self.ball_group.sprite

    @property
    def has_started(self):
        return self.ball is not None

    @property
    def game_over(self):
        return self.lives <= 0

    # Actions

    def move_left(self):
        self.speed = -self.__base_speed, 0

    def move_right(self):
        self.speed = self.__base_speed, 0

    def stop(self):
        self.speed = 0, 0

    def start(self, level):
        self.level = level
        self.ball_group.sprite = Ball(level)

    def loose(self):
        # self.sound_effects['paddle_hit'].play()
        self.lives -= 1
        self.ball_group.empty()

    def update(self, *args, **kwargs):
        self.stop()
        if events.keys.is_key_pressed(self.keys[directions.LEFT]):
            self.move_left()
        if events.keys.is_key_pressed(self.keys[directions.RIGHT]):
            self.move_right()

        super().update(*args, **kwargs)

        if not self.has_started:
            return

        if self.rect.left <= self.level.left:
            self.rect.left = self.level.left
        if self.rect.right >= self.level.right:
            self.rect.right = self.level.right

        if self.ball.fallen:
            return self.loose()

        if self.level:
            items = self, *self.level

            for item in self.ball.get_collides(items):
                self.ball.hit_object(item)
                if isinstance(item, Brick):
                    self.score += item.points
                    self.level.remove(item)
