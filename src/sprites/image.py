import pygame


class Image(pygame.sprite.Sprite):
    def __init__(
        self,
        rect,
        image,
        *groups,
    ):
        """Initialize image.

        Args:
            rect (pygame.Rect): Sprite rect.
            filename (string): File to load image.
        """
        super().__init__(*groups)

        self.image = image
        self.rect = rect
        self.layer = 0
