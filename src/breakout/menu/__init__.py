import logging
import pygame
from sprites.screen import Screen
from .items import MainMenuItems


class MenuScreen(Screen):
    BACKGROUND_IMAGE = "res/global/map.jpg"

    def __init__(self, rect, *groups):
        super().__init__(rect, *groups)

        background = pygame.sprite.Sprite()
        background.image = pygame.image.load(self.BACKGROUND_IMAGE)
        background.rect = rect.copy()

        self.background = pygame.sprite.GroupSingle(background)
        self.menu_items = MainMenuItems(self.on_item_click)
        # self.events.listeners.append(self.menu_items)

    def update(self, *args, **kwargs):
        super().update(*args, **kwargs)

        self.menu_items.update(*args, **kwargs)

        self.background.draw(self.image)
        self.menu_items.draw(self.image)

    def on_item_click(self, *args, **kwargs):
        logging.debug(f"ITEM CLICK {args} {kwargs}")
