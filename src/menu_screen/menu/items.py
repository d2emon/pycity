import pygame
from sprites.button import Button
from sprites.menu_items import MenuItems
from .item import MainMenuItem


class MainMenuItems(MenuItems):
    margins = 5, 5

    def __init__(self, *items):
        super().__init__(*items)

        self.horizontal = False

        self.align_items()

    def align_items(self):
        top = 0
        left = 0

        for item in self:
            item.rect.left = left + self.margins[0]
            item.rect.top = top + self.margins[1]

            if self.horizontal:
                left = item.rect.right + self.margins[0]
            else:
                top = item.rect.bottom + self.margins[1]
