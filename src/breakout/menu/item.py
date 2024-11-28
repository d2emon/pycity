import pygame
from sprites.button import Button


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
