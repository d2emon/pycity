"""Main game screen.

Typical usage example:

  self.screen = MainScreen(self.window.get_rect())
  self.events.update(self.screen.events)
"""
import logging
import pygame
from sprites.image import Image
from sprites.screen import Screen, ScreenGroup
from . import data
from .sprites.map import MapSprite
from .sprites.player import Player


class MainScreenGroup(ScreenGroup):
    """Sprites for main screen.
    
    Attributes:
      map_sprite (MapSprite): Map sprite.
      player (Player): Player sprite.
    """

    backgroundImage = "res/global/map.jpg"

    def __init__(self, game, *spites):
        """Intialize main sprites

        Args:
            rect (pygame.Rect): Screen rect
        """
        super().__init__(game, *spites)

        rect = game.window.get_rect()
        self.background = Image(rect, self.backgroundImage)

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


class MainScreen(Screen):
    """Main screen for game

    Attributes:
        events (Events): Game events.
        sprites (Sprites): Screen sprites.
    """

    def __init__(self, game, *groups):
        """Initialize main screen.

        Args:
            rect (pygame.Rect): Main screen rect
        """
        super().__init__(game, *groups)

        self.sprites = MainScreenGroup(game)

    @property
    def map_sprite(self):
        """Getter for map sprite.

        Returns:
            MapSprite: Map sprite
        """
        return self.sprites.map_sprite

    @property
    def player(self):
        """Getter for player sprite.

        Returns:
            Player: Player sprite.
        """
        return self.sprites.player