import pygame


def draw_brick(width, height):
    image = pygame.Surface((width, height), pygame.SRCALPHA)
    image.fill((0, 0, 255))
    return image
