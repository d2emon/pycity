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
from .background import Background
from .label import Label


class Button(pygame.sprite.Sprite):
    STATE_NORMAL = "BUTTON.STATE.NORMAL"
    STATE_HOVER = "BUTTON.STATE.HOVER"
    STATE_PRESSED = "BUTTON.STATE.PRESSED"

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

        # Create sprite

        self.image = pygame.Surface(rect.size)
        self.rect = rect
        self.inner_rect = self.image.get_rect()

        # Set properties

        self.on_click = on_click
        self.state = self.STATE_NORMAL

        self.backgrounds = {
            self.STATE_NORMAL: Background(self.inner_rect, (255, 255, 255)),
            self.STATE_HOVER: Background(self.inner_rect, (0, 255, 255)),
            self.STATE_PRESSED: Background(self.inner_rect, (0, 0, 255)),
        }

        # Create elements

        self.label = Label(
            self.inner_rect.center,
            text, # self.caption,
            font=font,
            color=text_color,
            center=True,
            # x=padding,
            # y=padding,
        ) # text

        # Fill child sprite groups

        self.__background_group = pygame.sprite.GroupSingle()
        self.labels = pygame.sprite.GroupSingle(self.label)

    # Getters and setters

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

    @property
    def title(self):
        """Get button title.

        Returns:
            string: Button title
        """
        return self.label.text

    # Actions

    def click(self, *args, **kwargs):
        """Button click action."""
        self.hover(*args, **kwargs)
        self.on_click(*args, **kwargs)

    def hover(self, *args, **kwargs):
        """Button hover action."""
        self.state = self.STATE_HOVER

    def leave(self, *args, **kwargs):
        """Button leave action."""
        self.state = self.STATE_NORMAL

    def press(self, *args, **kwargs):
        """Button press action."""
        self.state = self.STATE_PRESSED

    # Update button

    def __update_state(self):
        """Update button state."""
        if self.state == self.STATE_PRESSED and not self.is_pressed:
            self.click()
        elif not self.is_hovered:
            self.leave()
        elif self.is_pressed:
            self.press()
        else:
            self.hover()

    def __update_background(self):
        """Select background by state."""
        background = self.backgrounds.get(self.state)
        if background is not None:
            self.__background_group.sprite = background

    def update(self, *args, **kwargs):
        """Redraw button."""
        self.__update_state()
        self.__update_background()

        self.labels.update(*args, **kwargs)

        self.__background_group.draw(self.image)
        self.labels.draw(self.image)
