"""Main game screen.

Typical usage example:

  self.screen = MainScreen(self.window.get_rect())
  self.events.update(self.screen.events)
"""
import pygame
import config
from sprites.background import Background
from sprites.screen import ScreenGroup
from .sprites.level import Level
from .sprites.player import Player
from .worldgen import generate_world


class MainScreenGroup(ScreenGroup):
    """Sprites for main screen."""

    # ScreenGroup loaders

    def create_background(self):
        return Background(self.rect, (128, 128, 128))

    def create_level(self):
        world = generate_world(config.MAP_WIDTH, config.MAP_HEIGHT, config.TILE_SIZE)
        return Level.from_world(
            world,
            tile_size=config.TILE_SIZE,
        )

    def create_player(self):
        player = Player(
            tile_size=config.TILE_SIZE,
            level=self.level,
        )
        self.add(player, layer=10)

        player.rect.center = self.window.get_rect().center

        return player

    def update(self, *args, **kwargs):
        keys = pygame.key.get_pressed()
        self.player.check_keys(keys)

        self.level.set_camera(self.window, self.player.pos)

        super().update(*args, **kwargs)
