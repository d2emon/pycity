import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, tile_size=8, *groups):
        super().__init__(*groups)

        self.pos = [0, 0]
        self.speed = 1  # Базовая скорость
        self.vehicle = None
        self.size = tile_size

        self.image  = pygame.Surface((tile_size, tile_size))
        self.rect = self.image.get_rect()

        self.create_image()

    def create_image(self):
        color = (255, 0, 0)
        pygame.draw.rect(self.image, color, self.image.get_rect())


    def check_keys(self, keys):
        if keys[pygame.K_LEFT]: self.pos[0] -= self.speed
        if keys[pygame.K_RIGHT]: self.pos[0] += self.speed
        if keys[pygame.K_UP]: self.pos[1] -= self.speed
        if keys[pygame.K_DOWN]: self.pos[1] += self.speed

    # При смене транспорта
    def set_vehicle(vehicle_type):
        if vehicle_type == "horse":
            self.speed = 8
            self.vehicle = "horse"
