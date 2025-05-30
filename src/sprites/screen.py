import pygame
from .menu_items import MenuItems


class ScreenGroup(pygame.sprite.LayeredUpdates):
    def __init__(self, window, *spites):
        super().__init__(*spites)

        self.window = window
        self.rect = window.get_rect()

        self.background = self.create_background()
        self.player = self.create_player()
        self.level = self.create_level()

    def create_background(self):
        return None

    def create_player(self):
        return None

    def create_level(self):
        return None


class MenuScreenGroup(ScreenGroup):
    def __init__(self, window, *spites):
        super().__init__(window, *spites)

        self.menu_items = MenuItems()
        for menu_item in self.create_menu_items():
            self.menu_items.add(menu_item)
            self.add(menu_item, layer=10)
        self.menu_items.align_items()

    def create_menu_items(self):
        return []

