import pygame
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


if __name__ == "__main__":
    game = Breakout()
    game()
