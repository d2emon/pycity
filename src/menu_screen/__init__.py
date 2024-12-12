import pygame
from game import states
from game.state_game import StateGame
from breakout.main import MainScreen as BreakoutScreen
from map_walk.main import MainScreen as MapWalkScreen
from .menu import MenuScreen


class MenuScreen(StateGame):
    MENU = 'BREAKOUT.MENU'
    PLAYING = states.PLAYING
    MAP_WALK = 'MAP_WALK'

    screens = {
        MENU: MenuScreen,
        PLAYING: BreakoutScreen,
        MAP_WALK: MapWalkScreen,
    }

    def game_menu(self):
        self.state = self.MENU

    def game_play(self):
        self.state = self.PLAYING

    def game_map_walk(self):
        self.state = self.MAP_WALK

    def start(self):
        super().start()
        self.game_menu()


if __name__ == "__main__":
    game = MenuScreen()
    game()
