import pygame


loaded = {}


def load_sprite(sprite, source):
    if source in loaded:
        image = loaded[source]
    else:
        image = pygame.image.load(source)
        loaded[source] = image

    sprite.image = image
    sprite.rect = image.get_rect()
