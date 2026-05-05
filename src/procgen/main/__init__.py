"""Main game screen.

Typical usage example:

  self.screen = MainScreen(self.window.get_rect())
  self.events.update(self.screen.events)
"""
import pygame
import config
from procgen.world_map.world import World
from sprites.background import Background
from sprites.screen import ScreenGroup
from .sprites.level import Level
from .sprites.player import Player
from procgen.worldgen import generate_universe


class MainScreenGroup(ScreenGroup):
    """Sprites for main screen."""

    # ScreenGroup loaders

    def create_background(self):
        return Background(self.rect, (128, 128, 128))

    def create_level(self):
        world = World(
            10, # config.MAP_WIDTH,
            10, # config.MAP_HEIGHT,
            config.TILE_SIZE,
            # Metadata
            map_name="Universe Map",
            generator="UniverseMapGenerator",
        )
        generate_universe(world)
        return Level.from_world(world)

    def create_player(self):
        player = Player(
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
