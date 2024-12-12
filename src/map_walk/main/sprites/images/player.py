import pygame


__PLAYER_SIZE = 10
__PLAYER_COLOR = (255, 255, 0)

__PLAYER_VIEW = 5
__PLAYER_VIEW_COLOR = (0, 0, 255)


def __draw_player(image, size, color):
    """Draw player image.

    Args:
        image (pygame.Image): Sprite image.
        size (float): Player size.
        color (pygame.Color): Player color.
    """
    rect = image.get_rect()
    pygame.draw.circle(image, color, rect.center, size)


def __draw_view(image, size, color):
    """Draw player image.

    Args:
        image (pygame.Image): Sprite image.
        size (float): View area size.
        color (pygame.Color): View area color.
    """
    rect = image.get_rect()
    pygame.draw.circle(image, color, rect.center, size, 2)


def draw_player(scale=1.0):
    """Draw player image.

    Args:
        scale (float): Map scale.
    Returns:
        pygame.Surface: Loaded image.
    """
    radius = __PLAYER_VIEW * scale
    width = height = radius * 2
    image = pygame.Surface((width, height), flags=pygame.SRCALPHA)
    __draw_player(image, __PLAYER_SIZE, __PLAYER_COLOR)
    __draw_view(image, radius, __PLAYER_VIEW_COLOR)
    return image

    image = pygame.Surface((80, 20), pygame.SRCALPHA)
    image.fill((255, 0, 0))
    return image
