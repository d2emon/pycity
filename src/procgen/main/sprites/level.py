import pygame
from sprites.background import Background


class Level(pygame.sprite.Sprite):
    def __init__(self, level_map, rect, *groups):
        super().__init__(*groups)

        self.level_map = level_map

        self.rect = pygame.Rect(rect)
        self.image  = pygame.Surface(self.rect.size, pygame.SRCALPHA)

        self.background = Background(self.image.get_rect(), (0, 128, 0))

    def can_move(self, x, y):
        return self.level_map.can_move(x, y)

    def set_camera(self, screen, pos):
        return self.level_map.set_camera(screen, pos)

    def fill(self):
        self.image.blit(self.background.image, self.background.rect)

        self.level_map.fill()

        self.level_map.draw(self.image)
