import logging
import sys
import pygame
import events.keys
import events.mouse
from sprites.modals import Modals


game_logger = logging.getLogger('game')


class Game:
    EVENT_INIT = 50001
    EVENT_QUIT = 50002

    def __init__(
        self,
        title="Game",
        window_size=(800, 600),
        background_color=(0, 0, 0),
        delay=16,
        # fps=60,
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

        # Initialize pygame
        pygame.init()

        # Initialize events
        pygame.event.set_allowed([
            self.EVENT_INIT,
            self.EVENT_QUIT,
        ])

        # Set window params
        self.background_color = background_color
        self.delay = delay
        # self.fps = fps
        self.title = title
        self.window_size = window_size

        self.config = config

        self.__is_running = False

        # Initialize window
        self.window = pygame.display.set_mode(window_size)
        pygame.display.set_caption(self.title)

        # Create sprite lists
        # TODO: Use layered groups
        self.background_image = None
        self.sprites = pygame.sprite.Group()
        self.modals = Modals()

        # Initalize font system
        pygame.font.init()
        self.fonts = {}

        # TODO: Initialize sound system
        # pygame.mixer.pre_init(44100, 16, 2, 4096)

        # TODO: Initialize clock
        # self.clock = pygame.time.Clock()

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

    # Game loop setters

    def start(self):
        """Start game."""
        game_logger.debug("Starting game")

        self.is_running = True

    def stop(self):
        """Stop game."""
        game_logger.debug("Stopping game")

        self.is_running = False

    # Game loop methods

    def load(self):
        """Load game data before start."""
        game_logger.debug("Loading game")

        # Load sprites
        self.background_image = self.create_back()

        self.on_init()

    def update(self):
        """Update game on next tick."""

        if pygame.key.get_pressed()[pygame.K_ESCAPE]:
            self.stop()

        if events.keys.is_key_pressed(pygame.K_ESCAPE):
            self.stop()

        # pygame.display.update() - may be usefull

        self.modals.update()

    def set_delay(self):
        """Wait for next tick."""
        pygame.time.delay(self.delay)
        # self.clock.tick(self.fps)

    def draw_back(self):
        # Fill screen
        self.window.blit(self.background_image, (0, 0))

    def draw(self):
        """Draw game screen."""
        self.sprites.draw(self.window)
        self.modals.draw(self.window)

        # pygame.display.flip()

    def quit(self):
        """Close game window."""
        game_logger.debug("Quiting game")

        self.on_quit()
        pygame.quit()

    def get_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.stop()

            if self.modals.has_modals:
                self.modals.on_game_event(event)
            else:
                self.on_game_event(event)

    def play(self):
        self.get_events()

        self.update()
        self.set_delay()  # ???
        # TODO: Fix it with layers
        self.draw_back()
        self.draw()

        # Update screen
        pygame.display.flip()

    # Events

    def on_init(self):
        pygame.event.post(pygame.event.Event(self.EVENT_INIT))
        # GameEvent.send('START')

    def on_quit(self):
        pygame.event.post(pygame.event.Event(self.EVENT_QUIT))

    def on_game_event(self, event):
        game_logger.debug(f"Event: {event}")

        if event.type == pygame.KEYDOWN:
            events.keys.set_pressed(event.key)

        if event.type == pygame.KEYUP:
            events.keys.unset_pressed(event.key)

        if event.type == pygame.MOUSEBUTTONDOWN:
            events.mouse.set_pressed(event.button)

        if event.type == pygame.MOUSEBUTTONUP:
            events.mouse.unset_pressed(event.button)

    # Main game

    def __call__(self, *args, **kwargs):
        """Game loop controller."""
        self.load()
        self.start()

        # Main game loop
        while self.is_running:
            self.play()

        self.quit()

    # Sprite creators

    def create_back(self):
        """Load game data before start."""
        # if config.NO_BACKGROUND:
        #     image = pygame.Surface(self.window_size)
        #     image.fill(self.background_color)
        # else:
        #     image = GameResources.get('main-screen')

        image = pygame.Surface(self.window_size)
        image.fill(self.background_color)

        return image
