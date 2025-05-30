import logging
import pygame
import events.keys
import events.mouse


class Window:
    logger = logging.getLogger('window')

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
        self.logger.debug("Initializing game")

        # Initialize pygame
        pygame.init()

        # Initialize events
        pygame.event.set_allowed([
            self.EVENT_INIT,
            self.EVENT_QUIT,
        ])

        # Set window params
        self.screen = None

        self.background_color = background_color
        self.delay = delay
        # self.fps = fps
        self.title = title
        self.size = window_size

        self.config = config

        # Initialize window
        self.init_window()

        # Initalize font system
        pygame.font.init()
        # self.fonts = {}

        # TODO: Initialize sound system
        # pygame.mixer.pre_init(44100, 16, 2, 4096)

        # TODO: Initialize clock
        # self.clock = pygame.time.Clock()

        pygame.event.post(pygame.event.Event(self.EVENT_INIT))

        self.logger.debug("Starting game")

    # Events

    def on_game_event(self, event):
        self.logger.debug(f"Event: {event}")

        if event.type == pygame.KEYDOWN:
            events.keys.set_pressed(event.key)

        if event.type == pygame.KEYUP:
            events.keys.unset_pressed(event.key)

        if event.type == pygame.MOUSEBUTTONDOWN:
            events.mouse.set_pressed(event.button)

        if event.type == pygame.MOUSEBUTTONUP:
            events.mouse.unset_pressed(event.button)


    # Game loop methods

    def init_window(self):
        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption(self.title)

    def get_events(self):
        for event in pygame.event.get():
            self.on_game_event(event)
            yield event

    def update(self):
        """Update game on next tick."""
        # may be usefull
        pygame.display.update()

    def draw(self):
        # Update screen
        pygame.display.flip()

    def next_tick(self):
        """Wait for next tick."""
        pygame.time.delay(self.delay)
        # self.clock.tick(self.fps)

    def quit(self):
        """Close game window."""
        self.logger.debug("Quiting game")
        pygame.event.post(pygame.event.Event(self.EVENT_QUIT))

        pygame.quit()
