import pygame
from image_loader import load_sprite


class MapSprite(pygame.sprite.Sprite):
    def __init__(self, image, pos, *groups):
        super().__init__(*groups)

        load_sprite(self, image)
        self.rect.center = pos

    @property
    def x(self):
        return self.rect.centerx        

    @x.setter
    def x(self, value):
        self.rect.centerx = value

    @property
    def y(self):
        return self.rect.centery

    @y.setter
    def y(self, value):
        self.rect.centery = value
