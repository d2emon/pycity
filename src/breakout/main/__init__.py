import logging
import random
import pygame
from sprites.screen import Screen
# from .groups.bricks import Bricks
from .sprites.paddle import Paddle


class MainScreen(Screen):
    BACKGROUND_IMAGE = "res/global/map.jpg"

    def __init__(self, game, *groups):
        super().__init__(game, *groups)

        background = pygame.sprite.Sprite()
        background.image = pygame.image.load(self.BACKGROUND_IMAGE)
        background.rect = self.rect
        self.background = pygame.sprite.GroupSingle(background)

        player_pos = (self.rect.centerx, 400)
        base_speed = 10
        player = Paddle(player_pos, base_speed, self.sprites)

        self.__player_group = pygame.sprite.GroupSingle(player)

        # self.bricks = Bricks()

        start()

    @property
    def player(self):
        self.__player_group.sprite

    def start(self):
        ball_speed = random.randint(-2, 2), 1
        self.player.start(self.rect.center, ball_speed, self.sprites)

    def update(self, *args, **kwargs):
        self.background.draw(self.image)

        # self.bricks.update(self.player)

        super().update(*args, **kwargs)

        # if not self.bricks:
        #     return self.events.emit(events.EVENT_WIN)

        # if self.player.game_over:
        #     return self.events.emit(events.EVENT_LOOSE)

        # self.bricks.draw(self)
