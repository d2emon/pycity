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
        self.bricks = Bricks()

        self.start()

    @property
    def player(self):
        return self.__player_group.sprite

    @property
    def ball(self):
        return self.player.ball

    def start(self):
        self.player.start(self.rect)

    def update(self, *args, **kwargs):
        if not self.player.has_started:
            self.start()
        else:
            for brick in self.ball.check_bricks(self.bricks):
                self.player.score += brick.points

        # if not self.bricks:
        #     return self.events.emit(events.EVENT_WIN)

        # if self.player.game_over:
        #     return self.events.emit(events.EVENT_LOOSE)

        self.bricks.update(*args, **kwargs)
        self.player.ball_group.update(*args, **kwargs)

        self.__background_group.draw(self.image)

        super().update(*args, **kwargs)

        self.player.ball_group.draw(self.image)
        self.bricks.draw(self.image)

