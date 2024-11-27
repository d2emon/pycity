import logging
import pygame


class Moving(pygame.sprite.Sprite):
    def __init__(
        self,
        image,
        rect,
        speed=(0, 0),
        *groups,
    ):
        super().__init__(*groups)

        self.image = image
        self.rect = rect
        self.__speed = speed

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

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, value):
        self.__speed = value

    def update(self, game_map=None):
        self.rect = self.rect.move(*self.speed)
