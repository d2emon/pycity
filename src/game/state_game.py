import logging
import pygame
import events.keys
from . import Game, states


game_logger = logging.getLogger('state-game')


class StateGame(Game):
    EVENT_PLAY = 50101
    EVENT_STOP = 50102

    STATE_EXIT = states.EXIT
    STATE_GAME_OVER = states.GAME_OVER
    STATE_INITIALIZATION = states.INITIALIZATION
    STATE_PLAYING = states.PLAYING
    STATE_WIN = states.WIN

    state_screens = {}

    def __init__(self, window, **config):
        """Initialize game"""
        super().__init__(window, **config)

        self.logger.debug("Initializing game with states")

        # Set game fields
        # self.game_is_over = False
        self.__state = self.STATE_INITIALIZATION
        # self.objects = []

        # Create sprites
        self.__group = None

    # Getters and setters

    @property
    def state_screen(self):
        """Get current screen.

        Returns:
            pygame.sprite.Sprite: Current screen sprite.
        """
        return self.__group

    @state_screen.setter
    def state_screen(self, value):
        """Set current screen.

        Args:
            value (pygame.sprite.Sprite): New screen sprite.
        """
        self.__group = value

        # Add screen events to handlers
        # Add custom events to handlers
        # Add screen to event listeners

    @property
    def state(self):
        """Get current state.

        Returns:
            string: Current game state.
        """
        return self.__state

    @state.setter
    def state(self, value):
        """Set new state and change screen.

        Args:
            value (string): New game state.
        """
        self.logger.debug(f"[State: {value}]")

        if self.__state == value and self.__group is not None:
            return

        self.__state = value

        screen = self.state_screens.get(value)
        if screen is None:
            return

        self.state_screen = screen(self.window)

    @property
    def is_running(self):
        """Get if game is running (playing).

        Returns:
            bool: Game is running.
        """
        return self.state != self.STATE_EXIT

    @is_running.setter
    def is_running(self, value):
        """Set game is running (playing).

        Args:
            value (bool): Game is running.
        """
        if value:
            self.__state = self.STATE_PLAYING
        else:
            self.__state = self.STATE_EXIT

    # Game loop setters

    def start(self):
        """Start game."""
        self.logger.debug("Starting game with states")

        self.state = self.STATE_PLAYING

    def stop(self):
        """Stop game."""
        self.logger.debug("Stopping game with states")

        self.state = self.STATE_EXIT

    def game_win(self):
        """Win game."""
        self.logger.debug("Winning game with states")

        self.state = self.STATE_WIN

    def game_loose(self):
        """Loose game."""
        self.logger.debug("Loosing game with states")

        self.state = self.STATE_GAME_OVER

    # Game loop methods

    def load(self, window):
        # # Load resources
        # GameResources.load()

        super().load(window)

    def update(self):
        super().update()

        if self.__group is not None:
            self.__group.update()

    def draw(self, screen):
        if self.__group is not None:
            self.__group.draw(screen)

        super().draw(screen)
