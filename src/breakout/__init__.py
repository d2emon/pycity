import logging
import pygame
from game.state_game import StateGame
# from windows.controls import TextObject
from . import states
from .main import MainScreen
from .menu import MenuScreen


class Breakout(StateGame):
    screens = {
        states.MENU: MenuScreen,
        states.PLAYING: MainScreen,
    }

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
            # fps=fps,

            background_color=background_color,
            delay=delay,

            **config,
        )

    def game_menu(self):
        logging.debug("Initialize main menu")
        self.state = states.MENU
        # self.screen_group.sprite = MainScreen(self)
        # events={
        #     events.EVENT_WIN: self.on_win,
        #     events.EVENT_LOOSE: self.on_loose,
        # },

    def game_play(self):
        logging.debug("Initialize main game")
        self.state = states.PLAYING
        # self.screen_group.sprite = MenuScreen(self)

    def start(self):
        super().start()
        self.game_menu()

    # Events


"""


class Breakout(StateGame):
    # Events

    def on_win(self, *args, **kwargs):
        TextObject.show_message(self, "YOU WIN!!!", center=True)
        return self.game_win()

    def on_loose(self, *args, **kwargs):
        TextObject.show_message(self, "YOU LOOSE!!!", center=True)
        return self.stop()
"""


if __name__ == "__main__":
    game = Breakout()
    game()
