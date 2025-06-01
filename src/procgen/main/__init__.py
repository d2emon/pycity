"""Main game screen.

Typical usage example:

  self.screen = MainScreen(self.window.get_rect())
  self.events.update(self.screen.events)
"""
import pygame
import config
# from sprites.image import Image
from sprites.screen import ScreenGroup
from .game_map import GameMap
from .sprites.player import Player
# from .resources import MainResources
from .world import World


class MainScreenGroup(ScreenGroup):
    """Sprites for main screen."""

    def __init__(self, window, **sprites):
        super().__init__(window, **sprites)

        self.world = None

    # ScreenGroup loaders

    def create_background(self):
        # background = Image(self.rect, MainResources.get('background'))
        # self.add(background)
        return None

    def create_player(self):
        player = Player(tile_size=config.TILE_SIZE)
        self.add(player, layer=10)

        player.rect.center = self.window.get_rect().center

        return player

    def create_level(self):
        self.world = World.generate_map(config.MAP_WIDTH, config.MAP_HEIGHT, config.TILE_SIZE)
        level = GameMap(
            self.world,
            self.window.get_rect().size,
            config.TILE_SIZE,
        )

        if self.player:
            self.player.level = level

        # self.add(level, layer=5)
        return level

    def update(self, *args, **kwargs):
        keys = pygame.key.get_pressed()
        self.player.check_keys(keys)

        self.level.set_camera(self.window, self.player.pos)
        self.level.fill()

        super().update(*args, **kwargs)

    def draw(self, surface, *args, **kwargs):
        self.level.draw(surface)
        super().draw(surface, *args, **kwargs)
