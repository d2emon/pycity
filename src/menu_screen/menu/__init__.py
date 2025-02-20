import pygame
from game.state_game import StateGame
from sprites.image import Image
from sprites.screen import ScreenGroup
from .item import MainMenuItem
from .items import MainMenuItems


class MenuScreenGroup(ScreenGroup):
    EVENT_GAME_BREAKOUT = 50201
    EVENT_GAME_CITY = 50202
    EVENT_GAME_MAP_WALK = 50203

    background_image = "res/global/map.jpg"
    start_rect = pygame.Rect(8, 8, 240, 40)

    def __init__(self, window, *spites):
        super().__init__(window, *spites)

        rect = self.window.get_rect()
        self.background = Image(rect, self.background_image)
        self.add(self.background)

        self.menu_items = MainMenuItems(
            MainMenuItem("Play", self.on_play_click),
            MainMenuItem("Walk Map", self.on_map_walk_click),
            MainMenuItem("City", self.on_city_click),
            MainMenuItem("Quit", self.on_quit_click),
        )

        for menu_item in self.menu_items:
            self.add(menu_item, layer=10)

        pygame.event.set_allowed([
            self.EVENT_GAME_BREAKOUT,
            self.EVENT_GAME_MAP_WALK,
            self.EVENT_GAME_CITY,
            StateGame.EVENT_STOP,
        ])

    def on_play_click(self, *args, **kwargs):
        pygame.event.post(pygame.event.Event(self.EVENT_GAME_BREAKOUT))

    def on_map_walk_click(self, *args, **kwargs):
        pygame.event.post(pygame.event.Event(self.EVENT_GAME_MAP_WALK))

    def on_city_click(self, *args, **kwargs):
        pygame.event.post(pygame.event.Event(self.EVENT_GAME_CITY))

    def on_quit_click(self, *args, **kwargs):
        pygame.event.post(pygame.event.Event(StateGame.EVENT_STOP))
