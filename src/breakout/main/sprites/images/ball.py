import pygame


def draw_ball():
    color = (0, 255, 0)
    r = 5

    image = pygame.Surface((10, 10), pygame.SRCALPHA)
    pygame.draw.circle(image, color, image.get_rect().center, r)
    return image
