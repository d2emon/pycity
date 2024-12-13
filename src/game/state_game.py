import logging
import pygame
import events.keys
from . import Game, states


class StateGame(Game):
    STATE_EXIT = states.EXIT
    STATE_GAME_OVER = states.GAME_OVER
    STATE_INITIALIZATION = states.INITIALIZATION
    STATE_PLAYING = states.PLAYING
    STATE_WIN = states.WIN

    screens = {}

    def __init__(
        self,
        title="Game",
        window_size=(640, 480),
        background_color=(0, 0, 0),
        delay=16,
        **config,
    ):
        """Initialize game window.

        Old Args:
            fps (int, optional): _description_. Defaults to 60.

        Args:
            title (str, optional): Window title (caption). Defaults to "Game".
            window_size (tuple, optional): Window width and height (size). Defaults to (800, 600).
            background_color (tuple, optional): Background color for screen. Defaults to (0, 0, 0).
            delay (int, optional): Delay before next tick. Defaults to 16.
        """
        super().__init__(
            title=title,
            window_size=window_size,
            background_color=background_color,
            delay=delay,
            **config,
        )

        logging.debug(f"Initializing game with states")

        # Set game fields

        # self.game_is_over = False
        self.__state = self.STATE_INITIALIZATION
        # self.objects = []

        # ?

        self.__screen_group = pygame.sprite.Group()

        # Set INIT error on init
        # Set UPDATE error on update
        # Set DRAW error on draw
        # Set KEY_UP error on key up
        # Set KEY_DOWN error on key down

    # Getters and setters

    @property
    def screen(self):
        """Get current screen.

        Returns:
            pygame.sprite.Sprite: Current screen sprite.
        """
        return self.__screen_group

    @screen.setter
    def screen(self, value):
        """Set current screen.

        Args:
            value (pygame.sprite.Sprite): New screen sprite.
        """
        self.__screen_group = value

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
        self.__state = value

        screen = self.screens.get(value)
        if screen is None:
            return

        self.screen = screen(self)

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
        logging.debug("Starting game with states")
        self.__state = self.STATE_PLAYING

    def stop(self):
        """Stop game."""
        logging.debug("Stopping game with states")
        self.__state = self.STATE_EXIT

    def game_win(self):
        """Win game."""
        logging.debug("Winning game with states")
        self.__state = self.STATE_WIN

    def game_loose(self):
        """Loose game."""
        logging.debug("Loosing game with states")
        self.__state = self.STATE_GAME_OVER

    # Game loop methods

    def check_keys(self):
        if events.keys.is_key_pressed(pygame.K_ESCAPE):
            self.stop()

    def update(self):
        super().update()

        self.check_keys()

        self.__screen_group.update()

    def draw(self):
        super().draw()

        # logging.debug("Event: STATE_GAME.DRAW")
        self.__screen_group.draw(self.window)
        # pygame.display.flip()
