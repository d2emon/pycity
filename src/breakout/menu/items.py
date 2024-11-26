import logging
import pygame
from sprites.button import Button
from sprites.menu_items import MenuItems, MenuItem
# from config.games import breakout as config
# from events import Events
# from windows.controls import TextObject
# from ... import events


class MainMenuItem(Button):
    def __init__(self, rect, title, on_click=lambda *args, **kwargs: None):
        super().__init__(
            rect,
            title,
            on_click=on_click,
            # font=self.font,
            # padding=config.BUTTON_PADDING,
        )


class MainMenuItems(MenuItems):
    # BUTTON_FONT_NAME = 'Arial'
    # BUTTON_FONT_SIZE = 20
    # BUTTON_FONT_COLOR = (0, 0, 0)
    BUTTON_MARGIN = 5, 5
    # BUTTON_PADDING = 5
    BUTTON_WIDTH = 250
    BUTTON_HEIGHT = 50

    # BRICKS_WIDTH = 12
    # BRICKS_HEIGHT = 8

    def __init__(self, on_click):
        super().__init__()

        # self.font = TextObject.Font(
        #     config.BUTTON_FONT_NAME,
        #     config.BUTTON_FONT_SIZE,
        #     config.BUTTON_FONT_COLOR,
        # )

        # on_emit = lambda event_type, *args, **kwargs : print("BREAKOUT MENU ITEMS", event_type, args, kwargs)
        # self.events = Events({
        #     events.MOUSE_BUTTON_DOWN: self.emit,
        #     events.MOUSE_BUTTON_UP: self.emit,
        #     events.MOUSE_MOTION: self.emit,
        # }, on_emit)

        self.__on_item_click = on_click

        button_rect = pygame.Rect(
            self.BUTTON_MARGIN[0],
            self.BUTTON_MARGIN[1],
            self.BUTTON_WIDTH,
            self.BUTTON_HEIGHT,
        )
        # button_width = self.BUTTON_WIDTH + self.BUTTON_MARGIN[0] * 2
        button_height = self.BUTTON_HEIGHT + self.BUTTON_MARGIN[1] * 2

        self.add(
            MainMenuItem(
                button_rect.move(0, 0),
                'PLAY',
                self.on_select('events.MENU_PLAY'),
            ),
            MainMenuItem(
                button_rect.move(0, button_height),
                'QUIT',
                self.on_select('events.MENU_QUIT'),
            ),
        )

    def on_select(self, item_id):
        def handler(*args, **kwargs):
            logging.debug(f"SELECT {item_id} {args} {kwargs}")
            # self.events.emit(event_id, *args, **kwargs)
            self.__on_item_click(item_id, *args, **kwargs)

        return handler
