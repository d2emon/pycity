import pygame
from sprites.button import Button


class MainMenuItem(Button):
    EVENT_MENU_BUTTON = 50200

    font_name = 'Arial'
    font_size = 24
    color = (0, 0, 0)
    padding = 5
    width = 250
    height = 50

    def __init__(self, title, event_type=None, **kwargs: None):
        super().__init__(
            pygame.Rect(0, 0, self.width, self.height),
            title,
            on_click=self.__handle_click,
            font=pygame.font.SysFont(
                self.font_name,
                self.font_size,
            ),
            text_color=self.color,
            padding=self.padding,
        )

        self.__event_type = event_type

        pygame.event.set_allowed([
            MainMenuItem.EVENT_MENU_BUTTON,
        ])

    def __handle_click(self, *args):
        if self.__event_type:
            pygame.event.post(pygame.event.Event(self.EVENT_MENU_BUTTON, button=self.__event_type))
            return
