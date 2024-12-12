"""Main map sprite.

Typical usage example:

  map_sprite = MapSprite(rect)
"""
import pygame
from .images.map import draw_map
from .. import data


class MapSprite(pygame.sprite.Sprite):
    """Main map sprite.

    Attributes:
        image (pygame.Surface): Sprite image.
        rect (pygame.Rect): Sprite rect.
        viewpoint (pygame.Rect): Source rect.
    """

    def __init__(self, rect, viewpoint):
        """Initialize sprite.

        Args:
            image (pygame.Image): Sprite image.
            rect (pygame.Rect): Sprite rect.
            viewpoint (pygame.Rect): Source rect.
            step (float): Step for movement.
        """
        super().__init__()

        self.image = pygame.Surface((rect.width, rect.height))
        self.rect = pygame.Rect(rect)

        self.viewpoint = pygame.Rect(rect)
        self.viewpoint.center = viewpoint

        image = draw_map(
            data.MAP_FILE,
            data.MAP_SCALE,
            data.SCALE,
        )

        self.__step = data.SCALE * data.TIME_SCALE
        self.__map_image = image

        self.draw()

    def move(self, x, y):
        """Move sprite viewpoint.

        Args:
            x (float): Moves by x.
            y (float): Moves by y.
        """
        self.viewpoint = self.viewpoint.move(x * self.__step, y * self.__step)
        self.draw()

    def background(self):
        self.image.fill((0, 0, 0))

    def draw(self):
        """Update map image."""
        self.background()
        self.image.blit(self.__map_image, self.rect, self.viewpoint)
