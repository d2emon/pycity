"""Walking in procedure generated world.

Typical usage example:

  game = ProcGen()
  game()
"""

from game.state_game import StateGame
from .main import MainScreenGroup


class ProcGen(StateGame):
    state_screens = {
        StateGame.STATE_PLAYING: MainScreenGroup,
    }

    # State selectors

    def game_play(self):
        self.state = StateGame.STATE_PLAYING


if __name__ == "__main__":
    game = ProcGen()
    game()
