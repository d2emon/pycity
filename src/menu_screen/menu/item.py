import pygame
from sprites.button import Button


class MainMenuItem(Button):
    font_name = 'Arial'
    font_size = 24
    color = (0, 0, 0)
    padding = 5

    def __init__(self, rect, title, on_click=lambda *args, **kwargs: None):
        super().__init__(
            rect,
            title,
            on_click=on_click,
            font=pygame.font.SysFont(
                self.font_name,
                self.font_size,
            ),
            text_color=self.color,
            padding=self.padding,
        )
