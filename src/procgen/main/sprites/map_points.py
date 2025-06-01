import pygame


class MapPoint(pygame.sprite.Sprite):
    def __init__(self, pos, tile_size=8, *groups):
        super().__init__(*groups)

        self.pos = pos
        self.size = tile_size

        self.image  = pygame.Surface((tile_size, tile_size), pygame.SRCALPHA)
        self.rect = self.image.get_rect()

        self.create_image()

    def create_image(self):
        color = (255, 0, 255)
        pygame.draw.circle(self.image, color, self.image.get_rect().center, self.size / 2)
