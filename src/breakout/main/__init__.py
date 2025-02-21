import logging
import pygame
from game import states
from game.state_game import StateGame
from sprites.image import Image
from sprites.message import Message
from sprites.screen import ScreenGroup
from .groups.bricks import Bricks
from .resources import MainResources
from .sprites.paddle import Paddle


class MainScreenGroup(ScreenGroup):
    EVENT_WIN = 50103
    EVENT_LOOSE = 50104

    STATE_GAME_OVER = states.GAME_OVER
    STATE_PLAYING = states.PLAYING
    STATE_WIN = states.WIN

    def __init__(self, window, *spites):
        super().__init__(window, *spites)

        rect = self.window.get_rect()
        self.background = Image(rect, MainResources.get('background'))

        player_pos = (rect.centerx, 400)
        base_speed = 10
        self.player = Paddle(player_pos, base_speed)

        level_rect = pygame.Rect(0, 0, 570, 400)
        self.level = Bricks(level_rect)

        self.__messages = pygame.sprite.Group()

        self.__state = None

        pygame.event.set_allowed([
            self.EVENT_WIN,
            self.EVENT_LOOSE,
            StateGame.EVENT_STOP,
        ])

        self.start()

    @property
    def ball(self):
        return self.player.ball

    def start(self):
        if self.player.lives > 0:
            self.player.start(self.level)

    def win(self, *args, **kwargs):
        rect = self.window.get_rect()
        message = Message(
            rect,
            "YOU WIN!!!",
            font=pygame.font.SysFont('Arial', 24),
            color=(0, 255, 0),
        )
        self.__messages.add(message)
        pygame.event.post(self.EVENT_WIN)

    def loose(self, *args, **kwargs):
        rect = self.window.get_rect()
        message = Message(
            rect,
            "YOU LOOSE!!!",
            font=pygame.font.SysFont('Arial', 24),
            color=(255, 0, 0),
        )
        self.__messages.add(message)
        pygame.event.post(self.EVENT_LOOSE)

    def update(self, *args, **kwargs):
        if self.__state == self.STATE_WIN:
            pygame.event.post(pygame.event.Event(StateGame.EVENT_STOP))
        elif self.__state == self.STATE_GAME_OVER:
            pygame.event.post(pygame.event.Event(StateGame.EVENT_STOP))
        elif self.__state == self.STATE_PLAYING:
            if self.player.game_over:
                self.loose()
            elif self.level.is_finished:
                self.win()
            elif not self.player.has_started:
                self.start()

        self.empty()
        self.add(self.background)
        self.add(self.player, layer=10)
        if self.ball is not None:
            self.add(self.ball, layer=8)
        self.add(*self.level, layer=5)
        self.add(*self.__messages)

        super().update(*args, **kwargs)
