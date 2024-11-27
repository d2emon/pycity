import pygame


def draw_paddle():
    image = pygame.Surface((80, 20), pygame.SRCALPHA)
    image.fill((255, 0, 0))
    return image
