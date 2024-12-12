import pygame


__MAP_SCALE = 0.5


def __grid(image, step=10, start=(0, 0), size=(100, 100)):
    """Draw grid on image.

    Args:
        image (pygame.Surface): Image to draw grid.
        step (int): Grid step.
        start (tuple): Grid starting position.
        size (tuple): Grid size.
    """
    min_x, min_y = start
    width, height = size
    max_x = image.get_width() - width
    max_y = image.get_height() - height

    # Fill horyzontal lines
    for x in range(min_x, max_x, step):
        pygame.draw.line(image, (0, 0, 0), (x, min_y), (x, max_y))

    # Fill vertical lines
    for y in range(min_y, max_y, step):
        pygame.draw.line(image, (0, 0, 0), (min_x, y), (max_x, y))


def draw_map(filename, scale=1.0, step=None):
    """Draw map image.

    Args:
        filename (string): Filename with image.
        scale (float): Scale for image.
        step (int): Grid step.
    Returns:
        pygame.Surface: Loaded image.
    """
    image = pygame.image.load(filename)

    if scale:
        image = pygame.transform.scale(
            image,
            (
                int(image.get_width() * __MAP_SCALE),
                int(image.get_height() * __MAP_SCALE),
            ),
        )

    if step:
        __grid(
            image,
            size=(200, 300),
            start=(210, 185),
            step=step,
        )

    return image


