"""Walk on map.

Typical usage example:

  game = MapWalk()
  game()
"""

import logging
import pygame
from game.state_game import StateGame
from .main import MainScreenGroup


class MyGame(StateGame):
    STATE_GAME = 'STATE_GAME'

    screens = {
        STATE_GAME: MainScreenGroup,
    }


if __name__ == "__main__":
    MyGame.run()
