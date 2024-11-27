import pygame
# import time
from .label import Label


class Message(Label):
    default_font_name = 'Arial'
    default_font_size = 20

    def __init__(
        self,
        rect,
        text,
        font=None,
        duration=5,
    ):
        super().__init__(
            rect.center,
            text,
            font,
            color=(255, 255, 255)
        )
        self.duration = duration

    def after_render(self):
        self.render()
        # time.sleep(duration)
