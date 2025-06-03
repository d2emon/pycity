import pygame
import config
from sprites.background import Background
from .road_map import RoadMap
from ..worldgen.tile_map import TileMap


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
        self.tile_map = TileMap(tile_size)

        self.land = pygame.sprite.Group()
        self.inners = pygame.sprite.Group()
        self.points = pygame.sprite.Group()

        self.road_map = RoadMap(self.rect.width, self.rect.height)
        self.road_map_group = pygame.sprite.GroupSingle(self.road_map)

        self.load(self.world)

    def load(self, world):
        self.world = world

        self.land.empty()
        for y in range(world.height):
            for x in range(world.width):
                tile = world.get_tile((x, y))
                self.land.add(tile)

        self.points.empty()
        for p in world.points:
            self.points.add(p)

        self.inners.empty()
        for p in world.inners:
            self.inners.add(p)

        world.roads.draw(self.road_map)

        self.fill()

    def can_move(self, x, y):
        player_pos = self.tile_map.get_pos((x, y))

        tile = self.world.get_tile(player_pos)

        if tile is None:
            return False

        if tile.is_solid:
            return False

        return True

    def set_camera(self, screen, pos):
        x, y = pos

        rect = screen.get_rect()
        self.rect.left = rect.centerx - x
        self.rect.top = rect.centery - y

    def fill(self):
        self.image.blit(self.background.image, self.background.rect)
        self.land.draw(self.image)
        self.inners.draw(self.image)
        self.points.draw(self.image)
        self.road_map_group.draw(self.image)
