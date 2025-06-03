import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, tile_size=8, level=None, *groups):
        super().__init__(*groups)

        self.pos = [0, 0]
        self.speed = 3  # Базовая скорость
        self.vehicle = None
        self.size = tile_size

        self.image  = pygame.Surface((tile_size, tile_size))
        self.rect = self.image.get_rect()

        self.level = level

        self.create_image()

    def create_image(self):
        color = (255, 0, 0)
        pygame.draw.rect(self.image, color, self.image.get_rect())

    def move(self, dx, dy):
        new_x = self.pos[0] + dx
        new_y = self.pos[1] + dy

        if self.level:
            if not self.level.can_move(new_x, new_y):
                return

        self.pos = [new_x, new_y]

    def check_keys(self, keys):
        if keys[pygame.K_LEFT]: self.move(-self.speed, 0)
        if keys[pygame.K_RIGHT]: self.move(self.speed, 0)
        if keys[pygame.K_UP]: self.move(0, -self.speed)
        if keys[pygame.K_DOWN]: self.move(0, self.speed)

    # При смене транспорта
    def set_vehicle(self, vehicle_type):
        if vehicle_type == "horse":
            self.speed = 8
            self.vehicle = "horse"
