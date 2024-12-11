import pygame


class Solid(pygame.sprite.Sprite):
    @property
    def hitbox(self):
        return self.rect

    def is_colliding(self, other):
        return pygame.sprite.collide_rect(self, other)

    def get_collides(self, bodies):
        for body in bodies:
            if self.is_colliding(body):
                yield body
