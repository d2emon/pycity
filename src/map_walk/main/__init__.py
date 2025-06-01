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

    def __init__(self, window, *spites):
        """Intialize main sprites

        Args:
            rect (pygame.Rect): Screen rect
        """
        super().__init__(window, *spites)

        rect = self.window.get_rect()
        self.background = Image(rect, MainResources.get('background'))

        self.map_sprite = MapSprite(rect, data.VIEWPOINT)

        player_pos = rect.center
        base_speed = data.PLAYER_SPEED
        self.player = Player(player_pos, base_speed)

        self.start()

    def start(self):
        if not self.player.has_started:
            self.player.start(self.map_sprite)

    def update(self, *args, **kwargs):
        self.empty()
        self.add(self.background)
        self.add(self.map_sprite, layer=5)
        self.add(self.player, layer=10)

        super().update(*args, **kwargs)
