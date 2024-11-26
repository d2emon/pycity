import pygame
from .button import Button
# from events import Events


class MenuItem(Button):
    def __init__(self, title, on_click=lambda *args, **kwargs: None):
        super().__init__(
            pygame.Rect(),
            title,
            on_click=on_click,
        )
        # return self.add(item)


class MenuItems(pygame.sprite.Group):
    """Game menu sprite.

    Attributes:
        events (Events): Menu events.
    """

    def __init__(self, *sprites):
        """Initialize game menu."""
        super().__init__(*sprites)
        # self.events = Events()

"""


class MenuItems(pygame.sprite.Group):
    def emit(self, event_type, *args, **kwargs):
        ""Emit event in all manu items.

        Args:
            event_type (int): Event type.
        ""
        for item in self:
            item.events.emit(event_type, *args, **kwargs)
"""
