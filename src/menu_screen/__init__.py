import pygame
import config
from game import states
from game.state_game import StateGame
from breakout.main import MainScreenGroup as BreakoutScreen
from map_walk.main import MainScreenGroup as MapWalkScreen
from my_game.main import MainScreenGroup as CityScreen
from .menu import MenuScreenGroup


class MenuScreen(StateGame):
    MENU = 'BREAKOUT.MENU'
    PLAYING = states.PLAYING
    MAP_WALK = 'MAP_WALK'
    PLAY_CITY = 'PLAY_CITY'

    screens = {
        MENU: MenuScreenGroup,
        PLAYING: BreakoutScreen,
        MAP_WALK: MapWalkScreen,
        PLAY_CITY: CityScreen,
    }

    def __init__(self, **game_config):
        super().__init__(
            title=config.CAPTION,
            window_size=config.WINDOW_SIZE,
            background_color=config.BACKGROUND_COLOR,
            delay=config.DELAY,
            # fps=60,
            **game_config,
        )

    def game_menu(self):
        self.state = self.MENU

    def game_play(self):
        self.state = self.PLAYING

    def game_map_walk(self):
        self.state = self.MAP_WALK

    def game_city(self):
        self.state = self.PLAY_CITY

    def start(self):
        super().start()
        self.game_menu()


if __name__ == "__main__":
    game = MenuScreen()
    game()
