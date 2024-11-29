import pygame


def draw_brick():
    image = pygame.Surface((80, 20), pygame.SRCALPHA)
    image.fill((0, 0, 255))
    return image
