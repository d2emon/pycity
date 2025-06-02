"""Main game screen.

Typical usage example:

  self.screen = MainScreen(self.window.get_rect())
  self.events.update(self.screen.events)
"""
import pygame
import config
from sprites.background import Background
from sprites.screen import ScreenGroup
from .game_map import GameMap
from .sprites.level import Level
from .sprites.player import Player
from .world import World


class MainScreenGroup(ScreenGroup):
    """Sprites for main screen."""

    def __init__(self, window, **sprites):
        super().__init__(window, **sprites)

        self.world = None

    # ScreenGroup loaders

    def create_background(self):
        return Background(self.rect, (128, 128, 128))

    def create_player(self):
        player = Player(tile_size=config.TILE_SIZE)
        player.rect.center = self.window.get_rect().center
        self.add(player, layer=10)

        if self.level:
            player.level = self.level

        return player

    def create_level(self):
        self.world = World.generate_map(config.MAP_WIDTH, config.MAP_HEIGHT, config.TILE_SIZE)
        level_map = GameMap(
            self.world,
            self.window.get_rect().size,
            config.TILE_SIZE,
        )
        return Level(level_map, self.window.get_rect())

    def update(self, *args, **kwargs):
        keys = pygame.key.get_pressed()
        self.player.check_keys(keys)

        self.level.set_camera(self.window, self.player.pos)
        self.level.fill()

        super().update(*args, **kwargs)
