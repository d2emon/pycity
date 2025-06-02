import pygame
import config
from sprites.background import Background
from ..game_map import GameMap


class Level(pygame.sprite.Sprite):
    def __init__(
        self,
        rect,
        world,
        tile_size=config.TILE_SIZE,
        *groups,
    ):
        super().__init__(*groups)

        self.rect = pygame.Rect(rect)
        self.image  = pygame.Surface(self.rect.size, pygame.SRCALPHA)

        self.background = Background(self.image.get_rect(), (0, 128, 0))

        self.world = world
        self.tile_size = tile_size
        self.level_map = GameMap(
            self.world,
            self.rect.size,
            self.tile_size,
        )

    def can_move(self, x, y):
        player_x = (x + self.tile_size // 2) // self.tile_size
        player_y = (y + self.tile_size // 2) // self.tile_size

        tile = self.world.get_tile(player_x, player_y)

        if tile is None:
            return False

        if tile.is_solid:
            return False

        return True

    def set_camera(self, screen, pos):
        return self.level_map.set_camera(screen, pos)

    def fill(self):
        self.image.blit(self.background.image, self.background.rect)

        self.level_map.fill()

        self.level_map.draw(self.image)
