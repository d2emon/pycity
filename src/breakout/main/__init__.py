import logging
import pygame
from sprites.image import Image
from sprites.screen import Screen
from .groups.bricks import Bricks
from .sprites.paddle import Paddle


class MainScreen(Screen):
    BACKGROUND_IMAGE = "res/global/map.jpg"

    def __init__(self, game, *groups):
        super().__init__(game, *groups)

        background = Image(self.rect, self.BACKGROUND_IMAGE)

        player_pos = (self.rect.centerx, 400)
        base_speed = 10
        player = Paddle(player_pos, base_speed, self.sprites)

        self.__background_group = pygame.sprite.GroupSingle(background)
        self.__player_group = pygame.sprite.GroupSingle(player)

        level_rect = pygame.Rect(0, 0, 570, 400)
        self.level = Bricks(level_rect)

        self.start()

    @property
    def player(self):
        return self.__player_group.sprite

    @property
    def ball(self):
        return self.player.ball

    def start(self):
        self.player.start(self.level)

    def update(self, *args, **kwargs):
        if not self.player.has_started:
            self.start()

        # if len(self.level) <= 0:
        #     return self.events.emit(events.EVENT_WIN)

        # if self.player.game_over:
        #     return self.events.emit(events.EVENT_LOOSE)

        self.level.update(*args, **kwargs)
        self.player.ball_group.update(*args, **kwargs)

        self.__background_group.draw(self.image)

        super().update(*args, **kwargs)

        self.player.ball_group.draw(self.image)
        self.level.draw(self.image)

