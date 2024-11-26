import logging
import pygame
from game.state_game import StateGame
# from windows.controls import TextObject
from . import states
# from . import events, states
from .menu import MenuScreen
# from .menu_screen import MenuScreen
# from .game_screen import GameScreen


class Breakout(StateGame):
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
        self.screen_group.sprite = MenuScreen(self.screen.get_rect())
        # self.set_screen(
        #     events={
        #         events.MENU_PLAY: self.on_select_play,
        #         events.MENU_QUIT: self.on_select_quit,
        #     },
        # )

    def start(self):
        super().start()
        self.game_menu()

    # Events


"""


class Breakout(StateGame):
    def game_play(self):
        self.set_screen(
            GameScreen(self.size),
            states.PLAYING,
            events={
                events.EVENT_WIN: self.on_win,
                events.EVENT_LOOSE: self.on_loose,
            },
        )

    # Events

    def on_select_play(self, *args, **kwargs):
        self.game_play()

    def on_select_quit(self, *args, **kwargs):
        self.stop()

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
