import pygame
from game.state_game import StateGame
from sprites.image import Image
from sprites.menu_items import MenuItems
from sprites.screen import ScreenGroup
from .item import MainMenuItem
from .resources import MenuResources


class MenuScreenGroup(ScreenGroup):
    def __init__(self, window, *spites):
        super().__init__(window, *spites)

        self.menu_items = MenuItems(
            MainMenuItem("Play", event_type="BREAKOUT"),
            MainMenuItem("Walk Map", event_type="MAP_WALK"),
            MainMenuItem("City", event_type="CITY"),
            MainMenuItem("Quit", event_type="QUIT"),
        )
        for menu_item in self.menu_items:
            self.add(menu_item, layer=10)

    # ScreenGroup loaders

    def create_background(self):
        background = Image(self.rect, MenuResources.get('background'))
        self.add(background)
        return background
