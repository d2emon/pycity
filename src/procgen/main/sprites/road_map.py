import pygame


class RoadMap(pygame.sprite.Sprite):
    def __init__(self, width, height, *groups):
        super().__init__(*groups)

        self.width = width
        self.height = height

        self.image  = pygame.Surface((width, height), pygame.SRCALPHA)
        self.rect = self.image.get_rect()

    def create_image(self, points, color, width):
        pygame.draw.lines(self.image, color, False, points, width)
