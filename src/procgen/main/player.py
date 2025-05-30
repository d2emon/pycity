import pygame


class Player:
    def __init__(self, tile_size=8):
        self.pos = [0, 0]
        self.speed = 3  # Базовая скорость
        self.vehicle = None

        self.tile_size = tile_size
        self.size = tile_size
        self.color = (255, 0, 0)
        self.rect = pygame.Rect(0, 0, tile_size, tile_size)

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

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
