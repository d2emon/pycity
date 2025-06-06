import pygame
from game import events
from sprites.image import Image
from sprites.menu_items import MenuItems
from sprites.screen import ScreenGroup
from .item import MainMenuItem
from .resources import MenuResources


class MenuScreenGroup(ScreenGroup):
    background_image = "res/global/map.jpg"

    def __init__(self, window, *spites):
        super().__init__(window, *spites)

        self.background = Image(self.rect, MenuResources.get('background'))
        self.add(self.background)

        self.menu_items = MenuItems(
            MainMenuItem("PLAY", event_type="BUTTON_PLAY"),
            MainMenuItem("QUIT", event_type="BUTTON_QUIT"),
        )
        for menu_item in self.menu_items:
            self.add(menu_item, layer=10)
