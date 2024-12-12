import pygame
from sprites.button import Button
from sprites.menu_items import MenuItems
from .item import MainMenuItem


class MainMenuItems(MenuItems):
    BUTTON_MARGIN = 5, 5
    BUTTON_WIDTH = 250
    BUTTON_HEIGHT = 50

    BUTTON_PLAY = "BUTTON_PLAY"
    BUTTON_MAP_WALK = "BUTTON_MAP_WALK"
    BUTTON_CITY = "BUTTON_CITY"
    BUTTON_QUIT = "BUTTON_QUIT"

    buttons = [
        BUTTON_PLAY,
        BUTTON_MAP_WALK,
        BUTTON_CITY,
        BUTTON_QUIT,
    ]

    button_titles = {
        BUTTON_PLAY: 'PLAY',
        BUTTON_MAP_WALK: 'MAP_WALK',
        BUTTON_CITY: 'CITY',
        BUTTON_QUIT: 'QUIT',
    }

    def __init__(self, events):
        super().__init__()

        self.add_items(events)

    def add_items(self, events):
        rect = pygame.Rect(
            self.BUTTON_MARGIN[0],
            self.BUTTON_MARGIN[1],
            self.BUTTON_WIDTH,
            self.BUTTON_HEIGHT,
        )
        # width = rect.width + self.BUTTON_MARGIN[0] * 2
        height = rect.height + self.BUTTON_MARGIN[1] * 2

        for id, button in enumerate(self.buttons):
            self.add(MainMenuItem(
                rect.move(0, id * height),
                self.button_titles[button],
                events[button],
            ))
