"""Walk on map.

Typical usage example:

  game = MapWalk()
  game()
"""

import pygame
# import config
from game.state_game import StateGame
# from .main import MainScreen


class MapWalk(StateGame):
    STATE_GAME = 'STATE_GAME'

    screens = {
        # STATE_GAME: MainScreen,
    }

    # Game control event definition

    # self.events.INIT: self.on_init,
    # self.events.DRAW: self.on_draw,
    # self.events.QUIT: self.on_quit,
    # self.events.UPDATE: self.on_update,

    def game_main(self):
        # self.state = self.STATE_GAME

        # pygame.display.flip()
        pass

    def start(self):
        """Initialize game.

        * Initialize Resource
        * Load background
        * Load main field
        * Initialize labels
        """
        super().start()
        self.game_main()

    # Events

    def on_draw(self, *args, **kwargs):
        """Draw main window.

        Draw main field and update rect
        Draw labels and update rect
        Check loose game
        """
        # self.window.blit(self.screen, (0, 0))
        # pygame.display.flip()
        pass

    def on_quit(self, *args, **kwargs):
        """Quit game."""
        # self.quit()
        pass

    def on_update(self, *args, **kwargs):
        """Update game controls.

        Hadle key pressed
        Update background
        Update main field
        Update labels
        """
        pass


if __name__ == "__main__":
    game = MapWalk()
    game()
