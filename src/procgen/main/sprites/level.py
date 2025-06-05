import pygame
from sprites.background import Background
from .map_points import MapPoint
from .road_map import RoadMap


class Level(pygame.sprite.Sprite):
    def __init__(
        self,
        rect,
        world,
        *groups,
    ):
        super().__init__(*groups)

        self.rect = pygame.Rect(rect)
        self.image  = pygame.Surface(self.rect.size, pygame.SRCALPHA)

        self.background = Background(self.image.get_rect(), (0, 128, 0))

        self.tiles = None

        self.land = pygame.sprite.Group()
        self.inners = pygame.sprite.Group()
        self.points = pygame.sprite.Group()

        self.road_map = RoadMap(self.rect.width, self.rect.height)
        self.road_map_group = pygame.sprite.GroupSingle(self.road_map)

    def load(self, world):
        self.tiles = world.tiles

        self.land.empty()
        for y in range(world.height):
            for x in range(world.width):
                tile = world.tiles.get_tile((x, y))
                self.land.add(tile)

        self.points.empty()
        for map_object in world.map_points:
            pos = map_object.pos
            point = MapPoint(pos, world.tile_size)
            point.rect = world.tiles.get_tile(pos)
            self.points.add(point)

        self.inners.empty()

        world.road_data.draw(self.road_map)

        self.fill()

    def can_move(self, x, y):
        tile = self.tiles.get_tile_by_pos((x, y))

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

    @classmethod
    def from_world(cls, world):
        rect = pygame.Rect(
            0,
            0,
            world.width * world.tile_size,
            world.height * world.tile_size,
        )
        level = cls(rect, world)
        level.load(world)
        return level
