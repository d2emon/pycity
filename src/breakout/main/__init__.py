import pygame
from sprites.image import Image
from sprites.message import Message
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

        self.__messages = pygame.sprite.Group()

        self.start()

    @property
    def player(self):
        return self.__player_group.sprite

    @property
    def ball(self):
        return self.player.ball

    def start(self):
        if self.player.lives > 0:
            self.player.start(self.level)

    def win(self, *args, **kwargs):
        message = Message(
            self.rect,
            "YOU WIN!!!",
            font=pygame.font.SysFont('Arial', 24),
            color=(0, 255, 0),
        )
        self.__messages.add(message)
        self.game.game_win()

    def loose(self, *args, **kwargs):
        message = Message(
            self.rect,
            "YOU LOOSE!!!",
            font=pygame.font.SysFont('Arial', 24),
            color=(255, 0, 0),
        )
        self.__messages.add(message)
        self.game.game_loose()

    def update(self, *args, **kwargs):
        self.__messages.update(*args, **kwargs)

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

        self.level.update(*args, **kwargs)
        self.player.ball_group.update(*args, **kwargs)

        self.__background_group.draw(self.image)

        self.player.ball_group.draw(self.image)
        self.level.draw(self.image)
        self.__messages.draw(self.image)

        super().update(*args, **kwargs)
