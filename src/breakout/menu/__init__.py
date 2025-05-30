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
        yield MainMenuItem("PLAY", event_type="BUTTON_PLAY")
        yield MainMenuItem("QUIT", event_type="BUTTON_QUIT"),
