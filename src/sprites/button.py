"""Game button.

Typical usage example:

  button = Button(
    (0, 0, 100, 100),
    "Caption",
    on_click,
    padding=5,
  )
"""

import pygame
import events.mouse
from .label import Label


STATE_NORMAL = "BUTTON.STATE.NORMAL"
STATE_HOVER = "BUTTON.STATE.HOVER"
STATE_PRESSED = "BUTTON.STATE.PRESSED"


class Button(pygame.sprite.Sprite):
    def __init__(
        self,
        rect,
        text,
        on_click=lambda *args, **kwargs: None,
        padding=5,
        font=None,
        text_color=None,
    ):
        """Initialize button.

        Args:
            rect (pygame.Rect): Button rect.
            text (string): Button caption.
            on_click (function, optional): Button on_click event. Defaults to lambda*args.
            padding (int, optional): Padding for button text. Defaults to 5.
            font (Font, optional): Font for button text. Defaults to None.
        """
        super().__init__()

        self.image = pygame.Surface(rect.size)
        self.rect = rect

        self.on_click = on_click

        self.state = STATE_NORMAL

        self.colors = {
            STATE_NORMAL: (255, 255, 255),
            STATE_HOVER: (0, 255, 255),
            STATE_PRESSED: (0, 0, 255),
        }

        label_pos = self.image.get_rect().center
        self.label = Label(
            label_pos,
            text,
            font=font,
            color=text_color,
            center=True,
        )

        # Child sprite groups

        self.labels = pygame.sprite.GroupSingle(self.label)

    @property
    def is_hovered(self):
        """Get if button is hovered.

        Returns:
            bool: Button is hovered.
        """
        pos = pygame.mouse.get_pos()
        return self.rect.collidepoint(pos)

    @property
    def is_pressed(self):
        """Get if button is pressed.

        Returns:
            bool: Button is pressed.
        """
        return events.mouse.is_pressed(1)

    def __update_state(self):
        """On mouse move."""
        if self.state == STATE_PRESSED and not self.is_pressed:
            self.on_click()
            return STATE_HOVER
        elif not self.is_hovered:
            return STATE_NORMAL
        elif self.is_pressed:
            return STATE_PRESSED
        else:
            return STATE_HOVER

    def __draw_background(self):
        """Draw button background."""
        color = self.colors.get(self.state)
        if color is not None:
            self.image.fill(color)

    def update(self, *args, **kwargs):
        """Redraw button."""
        self.state = self.__update_state()

        self.labels.update(*args, **kwargs)

        self.__draw_background()
        self.labels.draw(self.image)
