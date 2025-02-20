import pygame
from sprites.button import Button


class MainMenuItem(Button):
    EVENT_MENU_BUTTON = 50200

    BUTTON_FONT_NAME = 'Arial'
    BUTTON_FONT_SIZE = 24
    BUTTON_FONT_COLOR = (0, 0, 0)
    BUTTON_PADDING = 5

    def __init__(self, rect, title, event_type=None, on_click=lambda *args, **kwargs: None):
        super().__init__(
            rect,
            title,
            on_click=self.__handle_click,
            font=pygame.font.SysFont(
                self.BUTTON_FONT_NAME,
                self.BUTTON_FONT_SIZE,
            ),
            text_color=self.BUTTON_FONT_COLOR,
            padding=self.BUTTON_PADDING
        )

        self.__event_type = event_type

        pygame.event.set_allowed([
            MainMenuItem.EVENT_MENU_BUTTON,
        ])

    def __handle_click(self, *args):
        if self.__event_type:
            pygame.event.post(pygame.event.Event(self.EVENT_MENU_BUTTON, button=self.__event_type))
            return
