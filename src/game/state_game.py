import logging
import pygame
from . import Game, states


class StateGame(Game):
    STATE_EXIT = states.EXIT
    # STATE_GAME_OVER = states.GAME_OVER
    STATE_INITIALIZATION = states.INITIALIZATION
    STATE_PLAYING = states.PLAYING
    STATE_WIN = states.WIN

    def __init__(
        self,
        title="Game",
        window_size=(640, 480),
        # fps=60,

        background_color=(0, 0, 0),
        delay=16,

        **config,
    ):
        super().__init__(
            title=title,
            window_size=window_size,
            background_color=background_color,
            delay=delay,
            # fps=fps
            **config,
        )
        logging.debug(f"Create game ({config})")

        self.events.update({
            # self.events.UPDATE: self.on_update,
            # self.events.DRAW: self.on_draw,
            # self.events.KEY_UP: self.on_key_up,
            # self.events.KEY_DOWN: self.on_key_down,
        })

        # self.game_is_over = False
        self.screen_group = pygame.sprite.GroupSingle()
        self.state = self.STATE_INITIALIZATION
        logging.debug(f"Initialize game")
        # self.objects = []

    @property
    def is_running(self):
        return self.state != self.STATE_EXIT

    @is_running.setter
    def is_running(self, value):
        if value:
            self.state = self.STATE_PLAYING
        else:
            self.state = self.STATE_EXIT

    def start(self):
        logging.debug("Event: STATE_GAME.INIT")
        self.state = self.STATE_PLAYING

    def stop(self):
        logging.debug("Event: STATE_GAME.QUIT")
        self.state = self.STATE_EXIT

    def game_win(self):
        logging.debug("Event: STATE_GAME.WIN")
        self.state = self.STATE_WIN

    # New methods

    def set_screen(self, screen, state=None, events=None):
        if state is not None:
            self.state = state

        self.screen_group.sprite = screen
        # self.events.update(self.screen_group.events.handlers)
        # if events:
        #     self.events.update(events)
        # # screen_group.events.listeners.append(self.events)
        # self.events.listeners.append(screen_group.events)

        # self.events.update(screen_group.events.handlers)

    def update(self):
        super().update()

        logging.debug("Event: STATE_GAME.UPDATE")
        self.screen_group.update()

    def draw(self):
        super().draw()

        logging.debug("Event: STATE_GAME.DRAW")
        self.screen_group.draw(self.screen)

    # Events

"""


class StateGame(Game):
    # Events

    def on_close(self, *args, **kwargs):
        self.stop()

    def on_key_down(self, *args, keys=None, **kwargs):
        if keys is None:
            return

        if pygame.K_ESCAPE in keys:
            self.stop()

    def on_key_up(self, *args, **kwargs):
        pass

    #

    def update_events(self, events):
        pass
"""
