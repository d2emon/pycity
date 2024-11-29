import pygame
# import time
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

    def pause(self):
        # time.sleep(duration)
        pass
