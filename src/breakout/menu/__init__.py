import pygame
from game import events
from sprites.image import Image
from sprites.screen import ScreenGroup
from .items import MainMenuItems


class MenuScreenGroup(ScreenGroup):
    background_image = "res/global/map.jpg"

    def __init__(self, window, *spites):
        super().__init__(window, *spites)

        rect = self.window.get_rect()
        self.background = Image(rect, self.background_image)
        self.add(self.background)

        self.menu_items = MainMenuItems({
            MainMenuItems.BUTTON_PLAY: "PLAY",
            MainMenuItems.BUTTON_QUIT: "QUIT",
        })
        for menu_item in self.menu_items:
            self.add(menu_item, layer=10)
