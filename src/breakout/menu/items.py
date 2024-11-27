import pygame
from sprites.button import Button
from sprites.menu_items import MenuItems


BUTTON_PLAY = "BUTTON_PLAY"
BUTTON_QUIT = "BUTTON_QUIT"


class MainMenuItem(Button):
    BUTTON_FONT_NAME = 'Arial'
    BUTTON_FONT_SIZE = 24
    BUTTON_FONT_COLOR = (0, 0, 0)
    BUTTON_PADDING = 5

    def __init__(self, rect, title, on_click=lambda *args, **kwargs: None):
        super().__init__(
            rect,
            title,
            on_click=on_click,
            font=pygame.font.SysFont(
                self.BUTTON_FONT_NAME,
                self.BUTTON_FONT_SIZE,
            ),
            text_color=self.BUTTON_FONT_COLOR,
            padding=self.BUTTON_PADDING
        )


class MainMenuItems(MenuItems):
    BUTTON_MARGIN = 5, 5
    BUTTON_WIDTH = 250
    BUTTON_HEIGHT = 50

    # BRICKS_WIDTH = 12
    # BRICKS_HEIGHT = 8

    def __init__(self, events):
        super().__init__()

        button_rect = pygame.Rect(
            self.BUTTON_MARGIN[0],
            self.BUTTON_MARGIN[1],
            self.BUTTON_WIDTH,
            self.BUTTON_HEIGHT,
        )
        # button_width = self.BUTTON_WIDTH + self.BUTTON_MARGIN[0] * 2
        button_height = self.BUTTON_HEIGHT + self.BUTTON_MARGIN[1] * 2

        titles = {
            BUTTON_PLAY: 'PLAY',
            BUTTON_QUIT: 'QUIT',
        }
        buttons = [
            BUTTON_PLAY,
            BUTTON_QUIT,
        ]
        for id, button in enumerate(buttons):
            self.add(MainMenuItem(
                button_rect.move(0, id * button_height),
                titles[button],
                events[button],
            ))
