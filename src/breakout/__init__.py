import logging
import pygame
from game.state_game import StateGame
from sprites.message import Message
from . import states
from .main import MainScreen
from .menu import MenuScreen



class Breakout(StateGame):
    # KEY_DOWN = GameEvents.KEY_DOWN
    # KEY_UP = GameEvents.KEY_UP

    # MOUSE_BUTTON_DOWN = GameEvents.MOUSE_BUTTON_DOWN
    # MOUSE_BUTTON_UP = GameEvents.MOUSE_BUTTON_UP
    # MOUSE_MOTION = GameEvents.MOUSE_MOTION

    # EVENT_START = 'GAME.START'
    # EVENT_WIN = 'GAME.WIN'
    # EVENT_LOOSE = 'GAME.LOOSE'

    screens = {
        states.MENU: MenuScreen,
        states.PLAYING: MainScreen,
    }

    def game_menu(self):
        logging.debug("Initialize breakout main menu")
        self.state = states.MENU
        # events.EVENT_WIN: self.on_win,
        # events.EVENT_LOOSE: self.on_loose,

    def game_play(self):
        logging.debug("Initialize breakout game")
        self.state = states.PLAYING

    def start(self):
        super().start()
        self.game_menu()

    # Events

    def on_win(self, *args, **kwargs):
        message = Message(
            self.window.get_rect(),
            "YOU WIN!!!",
            center=True,
        )
        self.sprites.add(message)
        return self.game_win()

    def on_loose(self, *args, **kwargs):
        message = Message(
            self.window.get_rect(),
            "YOU LOOSE!!!",
            center=True,
        )
        self.sprites.add(message)
        return self.stop()


if __name__ == "__main__":
    game = Breakout()
    game()
