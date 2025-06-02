"""Main game screen.

Typical usage example:

  self.screen = MainScreen(self.window.get_rect())
  self.events.update(self.screen.events)
"""
import logging
import pygame
from sprites.image import Image
from sprites.screen import ScreenGroup
from . import data
from .resources import MainResources
from .sprites.map import MapSprite
from .sprites.player import Player


class MainScreenGroup(ScreenGroup):
    """Sprites for main screen.
    
    Attributes:
      map_sprite (MapSprite): Map sprite.
      player (Player): Player sprite.
    """

    def __init__(self, window, **sprites):
        super().__init__(window, **sprites)
        self.start()

    # ScreenGroup loaders

    def create_background(self):
        return Image(self.rect, MainResources.get('background'))

    def create_player(self):
        player_pos = self.rect.center
        base_speed = data.PLAYER_SPEED
        player = Player(player_pos, base_speed)
        self.add(player, layer=10)
        return player

    def create_level(self):
        level = MapSprite(self.rect, data.VIEWPOINT)
        self.add(level, layer=5)
        return level

    def start(self):
        if not self.player.has_started:
            self.player.start(self.level)
