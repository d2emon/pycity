import pygame
import time
from .label import Label


class Message(Label):
    def __init__(
        self,
        rect,
        text,
        font=None,
        duration=5,
        color=(255, 255, 255)
    ):
        super().__init__(
            rect.center,
            text,
            font,
            color=color,
            center=True
        )
        self.duration = duration
        self.is_showing = False
        self.layer = 25

    def update(self, *args, **kwargs):
        if self.is_showing:
            time.sleep(self.duration)
        else:
            self.is_showing = True
