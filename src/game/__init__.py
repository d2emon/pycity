import logging
import sys
import pygame
import events.keys
import events.mouse




class Game:
    def __init__(
        self,
        title="Game",
        window_size=(800, 600),
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

        # Set game fields

        self.background_color = background_color # ???
        self.delay = delay # ???
        # self.fps = fps
        self.title = title # caption
        self.window_size = window_size # size
        self.config = config # ???
        self.__is_running = False

        # Initialize pygame

        pygame.init()

        # Initialize window

        self.window = self.create_window(window_size, title)

        # ?

        self.player_group = pygame.sprite.GroupSingle()
        self.sprites = pygame.sprite.Group()

        # Initalize font system

        pygame.font.init()
        self.fonts = {}

        # TODO: Initialize sound system

        # pygame.mixer.pre_init(44100, 16, 2, 4096)

        # TODO: Initialize clock

        # self.clock = pygame.time.Clock()

        # Set INIT error on init
        # Set QUIT error on quit

    # Creating window

    @classmethod
    def create_window(cls, size, title):
        """Create game window.

        Args:
            size (tuple): Window width and height.
            title (string): Window title.

        Returns:
            pygame.Surface: Window surface.
        """
        pygame.display.set_caption(title)
        window = pygame.display.set_mode(size)
        return window

    # Getters and setters

    @property
    def is_running(self):
        """Get if game is running (playing).

        Returns:
            bool: Game is running.
        """
        return self.__is_running

    @is_running.setter
    def is_running(self, value):
        """Set game is running (playing).

        Args:
            value (bool): Game is running.
        """
        self.__is_running = value

    # ?

    @property
    def player(self):
        return self.player_group.sprite

    @player.setter
    def player(self, value):
        self.player_group.sprite = value

    # @property
    # def camera(self):
    #     return self.camera.sprite

    # @camera.setter
    # def camera(self, value):
    #     self.camera.sprite = value

    # Game loop setters

    def start(self):
        """Start game."""
        logging.debug("Starting game")
        self.is_running = True

    def stop(self):
        """Stop game."""
        logging.debug("Stopping game")
        self.is_running = False

    # Game loop methods

    def load(self):
        """Load game data before start."""
        logging.debug("Event: INIT")
        self.on_init()

    def update(self):
        """Update game on next tick."""
        # pygame.display.update() - may be usefull
        pass

    def set_delay(self):
        """Wait for next tick."""
        pygame.time.delay(self.delay)
        # self.clock.tick(self.fps)

    def draw(self):
        """Draw game screen."""
        self.window.fill(self.background_color)
        self.sprites.draw(self.window)
        # pygame.display.flip()

    def quit(self):
        """Close game window."""
        logging.debug("Event: QUIT")
        self.on_quit()

        logging.debug("Quiting game")
        pygame.quit()
        sys.exit()

    # ?

    def get_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.stop()

            elif event.type == pygame.KEYDOWN:
                events.keys.set_pressed(event.key)
            elif event.type == pygame.KEYUP:
                events.keys.unset_pressed(event.key)

            # elif event.type == pygame.MOUSEMOTION:
            #     logging.debug(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                events.mouse.set_pressed(event.button)
            elif event.type == pygame.MOUSEBUTTONUP:
                events.mouse.unset_pressed(event.button)


            if events.keys.is_key_pressed(pygame.K_ESCAPE):
                self.stop()

    def play(self):
        self.get_events()

        self.update()
        self.set_delay()
        self.draw()

        pygame.display.flip()

    # Events

    def on_init(self):
        logging.debug("Event: GAME.INIT")

    def on_quit(self):
        logging.debug("Event: GAME.QUIT")

    # Main game

    def __call__(self, *args, **kwargs):
        """Game loop controller."""
        self.load()
        self.start()

        while self.is_running:
            self.play()

        self.quit()
