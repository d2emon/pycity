import pygame


class Background(pygame.sprite.Sprite):
    def __init__(
        self,
        rect,
        color=(0, 0, 0),
    ):
        """Initialize background.

        Args:
            rect (pygame.Rect): Background rect.
            color (tuple, optional): Background color. Defaults to (0, 0, 0).
        """
        super().__init__()

        # Create sprite

        self.image = pygame.Surface(rect.size)
        self.rect = rect

        # Set properties

        self.color = color

        # Draw self

        self.update()

    def update(self, *args, **kwargs):
        """Redraw background."""
        self.image.fill(self.color)
