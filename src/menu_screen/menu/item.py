import pygame
from sprites.button import Button


class MainMenuItem(Button):
    color = (0, 0, 0)
    padding = 5

    def __init__(self, rect, title, *groups, on_click=lambda *args, **kwargs: None):
        super().__init__(
            rect,
            title,
            on_click=on_click,
            font=pygame.font.SysFont('Arial', 24),
            text_color=self.color,
            padding=self.padding,
        )

        for group in groups:
            group.add(self)
