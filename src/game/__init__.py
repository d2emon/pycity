import logging
import sys
import pygame
import key_input


def create_screen(size, title):
    pygame.display.set_caption(title)
    screen = pygame.display.set_mode(size)
    return screen


class Game:
    def __init__(
        self,
        title="Game",
        window_size=(800, 600),
        # size=(800, 600),
        background_color=(0, 0, 0),
        delay=16,
        # fps=60
        **config,
    ):
        pygame.init()

        self.config = config

        self.title = title
        self.window_size = window_size
        self.screen = create_screen(window_size, title)
        self.background_color = background_color
        self.delay = delay

        self.player_group = pygame.sprite.GroupSingle()
        self.sprites = pygame.sprite.Group()

        pygame.font.init()
        self.fonts = {}

        # pygame.mixer.pre_init(44100, 16, 2, 4096)

        # self.clock = pygame.time.Clock()
        # self.fps = fps

        self.events = {
            "INIT": self.on_init,
            # GameEvents.DRAW: self.draw,
            "QUIT": self.on_quit,
            # GameEvents.UPDATE: self.update,
        }

        self.__is_running = False

    @property
    def is_running(self):
        return self.__is_running

    @is_running.setter
    def is_running(self, value):
        self.__is_running = value

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

    def load(self):
        self.on_init()

    def start(self):
        self.is_running = True

    def get_events(self):
        for event in pygame.event.get():
            # self.events.process_event(event)
            if event.type == pygame.QUIT:
                self.stop()

            elif event.type == pygame.KEYDOWN:
                key_input.keys_down.add(event.key)
            elif event.type == pygame.KEYUP:
                key_input.keys_down.remove(event.key)

            elif event.type == pygame.MOUSEMOTION:
                logging.debug(event)

            if pygame.K_ESCAPE in key_input.keys_down:
                self.stop()

    def update(self):
        logging.debug("Event: GAME.UPDATE")

        # # [self.events.process_event(event) for event in self.game_events]

        # pygame.display.update()

    def set_delay(self):
        pygame.time.delay(self.delay)
        # self.clock.tick(self.fps)

    def draw(self):
        logging.debug("Event: GAME.DRAW")

        self.screen.fill(self.background_color)
        self.sprites.draw(self.screen)

    def play(self):
        self.get_events()

        self.update()
        self.set_delay()
        self.draw()

        pygame.display.flip()

    def stop(self):
        logging.debug(f"Event: STOP")
        self.is_running = False

    def quit(self):
        self.on_quit()

        logging.debug("Quiting game")
        pygame.quit()
        sys.exit()

    def __call__(self, *args, **kwargs):
        logging.debug("Starting game")
        self.load()
        self.start()

        while self.is_running:
            self.play()

        self.quit()

    # Events

    def on_init(self):
        logging.debug("Event: GAME.INIT")

    def on_quit(self):
        logging.debug("Event: GAME.QUIT")
