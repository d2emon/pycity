import pygame
from game.state_game import StateGame
from sprites.image import Image
from sprites.menu_items import MenuItems
from sprites.screen import ScreenGroup
from .item import MainMenuItem


class MenuScreenGroup(ScreenGroup):
    # EVENT_MENU_BUTTON = 50200

    background_image = "res/global/map.jpg"
    start_rect = pygame.Rect(8, 8, 240, 40)

    def __init__(self, window, *spites):
        super().__init__(window, *spites)

        self.background = Image(self.rect, self.background_image)
        self.add(self.background)

        self.menu_items = MenuItems(
            MainMenuItem("Play", event_type="BREAKOUT"),
            MainMenuItem("Walk Map", event_type="MAP_WALK"),
            MainMenuItem("City", event_type="CITY"),
            MainMenuItem("Quit", event_type="QUIT"),
        )
        for menu_item in self.menu_items:
            self.add(menu_item, layer=10)
