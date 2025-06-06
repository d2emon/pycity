import logging
import pygame
import config
import events.keys
import events.mouse
from sprites.modals import Modals
from .window import Window


class Game:
    logger = logging.getLogger('game')

    def __init__(self, window, **game_config):
        """Initialize game"""
        self.config = game_config

        self.__is_running = False

        # Create sprite lists
        # TODO: Use layered groups
        self.background_color = (0, 0, 0)
        self.background_image = None
        self.sprites = pygame.sprite.Group()
        self.modals = Modals()

        # Initalize font system
        self.fonts = {}

        # TODO: Remove it
        self.window = window

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
        self.logger.debug("Starting game")

        self.is_running = True

    def stop(self):
        """Stop game."""
        self.logger.debug("Stopping game")

        self.is_running = False

    # Game loop methods

    def load(self, window):
        """Load game data before start."""
        self.logger.debug("Loading game")

        # Create background
        self.background_image = self.create_back(window)

    def process_event(self, event):
        if event.type == pygame.QUIT:
           self.stop()
           return

        if self.modals.has_modals:
            self.modals.on_game_event(event)
        else:
            self.on_game_event(event)

    def update(self):
        """Update game on next tick."""

        if pygame.key.get_pressed()[pygame.K_ESCAPE]:
            self.stop()

        if events.keys.is_key_pressed(pygame.K_ESCAPE):
            self.stop()

        self.modals.update()

        # self.window.update() - may be usefull

    def draw_back(self, screen):
        # Fill screen
        screen.blit(self.background_image, (0, 0))

    def draw(self, screen):
        """Draw game screen."""
        self.sprites.draw(screen)
        self.modals.draw(screen)

    def play(self, window):
        for event in window.get_events():
            self.process_event(event)

        self.update()
        # window.next_tick()  # ???

        screen = window.screen
        # TODO: Fix it with layers
        self.draw_back(screen)
        self.draw(screen)
        window.draw()

    # Events

    def on_game_event(self, event):
        logger = logging.getLogger('game.event')
        logger.debug(f"Event: {event}")

        if event.type == pygame.KEYDOWN:
            events.keys.set_pressed(event.key)

        if event.type == pygame.KEYUP:
            events.keys.unset_pressed(event.key)

        if event.type == pygame.MOUSEBUTTONDOWN:
            events.mouse.set_pressed(event.button)

        if event.type == pygame.MOUSEBUTTONUP:
            events.mouse.unset_pressed(event.button)

    # Main game

    def __call__(self, window, *args, **kwargs):
        """Game loop controller."""
        self.load(window)
        self.start()

        # Main game loop
        while self.is_running:
            self.play(window)

    # Sprite creators

    def create_back(self, window):
        """Load game data before start."""
        # if config.NO_BACKGROUND:
        #     image = pygame.Surface(window.size)
        #     image.fill(self.background_color)
        # else:
        #     image = GameResources.get('main-screen')

        image = pygame.Surface(window.size)
        image.fill(self.background_color)

        return image

    @classmethod
    def run(
        cls,
        title=config.CAPTION or "Game",
        window_size=config.WINDOW_SIZE or (800, 600),
        background_color=config.BACKGROUND_COLOR or (0, 0, 0),
        delay=config.DELAY or 16,
        window_config=None,
        **game_config,
    ):
        if window_config is None:
            window_config = {}

        window = Window(
            title,
            window_size,
            background_color,
            delay,
            **window_config,
        )
        game = cls(window.screen, **game_config)
        game(window)
        window.quit()
