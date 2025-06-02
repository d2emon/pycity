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
        self.camera_pos = [0, 0]

        self.land = pygame.sprite.Group()
        self.inners = pygame.sprite.Group()
        self.points = pygame.sprite.Group()

        self.load(self.world)

    def get_map_rect(self, tile_pos):
        tile_x, tile_y = tile_pos

        x = tile_x * self.tile_size
        y = tile_y * self.tile_size

        return x, y

    def load(self, world):
        self.land.empty()
        for y in range(world.height):
            for x in range(world.width):
                tile = world.get_tile(x, y)
                tile.rect.topleft = self.get_map_rect((x, y))
                self.land.add(tile)

        for p in world.points:
            p.rect = world.get_tile_rect(*p.pos)
            self.points.add(p)

        for p in world.inners:
            p.rect = world.get_tile_rect(*p.pos)
            self.inners.add(p)

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
        player_x, player_y = pos

        # Камера следует за игроком
        self.camera_pos[0] = player_x - screen.get_width() // 2
        self.camera_pos[1] = player_y - screen.get_height() // 2

        rect = screen.get_rect()
        self.rect.left = rect.centerx - player_x - self.tile_size // 2
        self.rect.top = rect.centery - player_y - self.tile_size // 2

    def fill(self):
        self.image.blit(self.background.image, self.background.rect)
        self.land.draw(self.image)
        self.inners.draw(self.image)
        self.points.draw(self.image)

        self.level_map.fill(self.camera_pos)
        self.level_map.draw(self.image)
