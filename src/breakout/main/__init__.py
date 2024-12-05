import logging
import pygame
from sprites.image import Image
from sprites.message import Message
from sprites.screen import Screen
from .groups.bricks import Bricks
from .sprites.paddle import Paddle


class MainScreenGroup(pygame.sprite.LayeredUpdates):
    backgroundImage = "res/global/map.jpg"

    def __init__(self, game, *spites):
        super().__init__(*spites)

        self.game = game
 
        rect = game.window.get_rect()
        self.background = Image(rect, self.backgroundImage)

        player_pos = (rect.centerx, 400)
        base_speed = 10
        self.player = Paddle(player_pos, base_speed)

        level_rect = pygame.Rect(0, 0, 570, 400)
        self.level = Bricks(level_rect)

        self.__messages = pygame.sprite.Group()

        self.start()

    @property
    def ball(self):
        return self.player.ball

    def start(self):
        if self.player.lives > 0:
            self.player.start(self.level)

    def win(self, *args, **kwargs):
        rect = self.game.window.get_rect()
        message = Message(
            rect,
            "YOU WIN!!!",
            font=pygame.font.SysFont('Arial', 24),
            color=(0, 255, 0),
        )
        self.__messages.add(message)
        self.game.game_win()

    def loose(self, *args, **kwargs):
        rect = self.game.window.get_rect()
        message = Message(
            rect,
            "YOU LOOSE!!!",
            font=pygame.font.SysFont('Arial', 24),
            color=(255, 0, 0),
        )
        self.__messages.add(message)
        self.game.game_loose()

    def update(self, *args, **kwargs):
        if self.game.state == self.game.STATE_WIN:
            self.game.stop()
        elif self.game.state == self.game.STATE_GAME_OVER:
            self.game.stop()
        elif self.game.state == self.game.STATE_PLAYING:
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

class MainScreen(Screen):
    BACKGROUND_IMAGE = "res/global/map.jpg"

    def __init__(self, game, *groups):
        super().__init__(game, *groups)

        self.sprites = MainScreenGroup(game)
