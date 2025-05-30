import pygame
from sprites.image import Image
from sprites.screen import MenuScreenGroup
from .item import MainMenuItem
from .resources import MenuResources


class MenuScreenGroup(MenuScreenGroup):
    def create_background(self):
        background = Image(self.rect, MenuResources.get('background'))
        self.add(background)
        return background

    def create_menu_items(self):
        yield MainMenuItem("Play", event_type="BREAKOUT"),
        yield MainMenuItem("Walk Map", event_type="MAP_WALK"),
        yield MainMenuItem("City", event_type="CITY"),
        yield MainMenuItem("Quit", event_type="QUIT"),
