import pygame


class Camera(pygame.sprite.Sprite):
    def __init__(self, size, map_size, background_color, *groups):
        super().__init__(*groups)

        self.image = pygame.surface.Surface(map_size)
        self.rect = self.image.get_rect()
        self.background_color = background_color
        self.size = size

        self.background_sprites = pygame.sprite.Group()
        self.foreground_sprites = pygame.sprite.Group()

    def update(self, player):
        self.background_sprites.update()
        self.foreground_sprites.update()

        self.image.fill(self.background_color)

        self.background_sprites.draw(self.image)
        player.draw(self.image)
        self.foreground_sprites.draw(self.image)

        self.rect.left = self.size[0] / 2 - player.sprite.rect.centerx
        self.rect.top = self.size[1] / 2 - player.sprite.rect.centery
