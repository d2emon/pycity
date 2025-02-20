import pygame
from game import events
from game.state_game import StateGame
from . import states
from .main import MainScreenGroup
from .menu import MenuScreenGroup


class Breakout(StateGame):
    screens = {
        states.MENU: MenuScreenGroup,
        states.PLAYING: MainScreenGroup,
    }

    def game_menu(self):
        self.state = states.MENU

    def game_play(self):
        self.state = states.PLAYING

    def start(self):
        super().start()
        self.game_menu()

    # Events

    def on_game_event(self, event):
        super().on_game_event(event)

        if event.type == events.EVENT_PLAY:
            self.game_play()
            return

        if event.type == events.EVENT_STOP:
            self.stop()
            return

        if event.type == MainScreenGroup.EVENT_WIN:
            self.game_win()
            return

        if event.type == MainScreenGroup.EVENT_LOOSE:
            self.game_loose()
            return


if __name__ == "__main__":
    game = Breakout()
    game()
