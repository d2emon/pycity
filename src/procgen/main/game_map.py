import pygame
from .sprites.road_map import RoadMap
from .worldgen.roads import Roads


class GameMap(pygame.sprite.Group):
    def __init__(self, world, screen_size, tile_size):
        super().__init__()

        self.screen_width, self.screen_height = screen_size

        self.tile_size = tile_size

        self.camera_pos = [0, 0]
        self.world = world
        self.points = pygame.sprite.Group(*world.points)
        self.road_map = RoadMap(world.width * tile_size, world.height * tile_size)

        for point in self.points:
            point.rect.center = self.get_map_rect(*point.pos)

        roads = Roads.generate([point.rect.center for point in self.points])
        roads.draw(self.road_map)

    def set_camera(self, screen, pos):
        player_x, player_y = pos

        # Камера следует за игроком
        self.camera_pos[0] = player_x - screen.get_width() // 2
        self.camera_pos[1] = player_y - screen.get_height() // 2

    def get_map_rect(self, tile_x, tile_y):
        camera_x, camera_y = self.camera_pos

        x = tile_x * self.tile_size - camera_x
        y = tile_y * self.tile_size - camera_y

        return x, y

    def fill(self):
        self.empty()

        for y in range(self.world.height):
            for x in range(self.world.width):
                tile = self.world.get_tile(x, y)
                tile.rect.center = self.get_map_rect(x, y)
                if 0 <= tile.rect.left < self.screen_width and 0 <= tile.rect.top < self.screen_height:
                    self.add(tile)

        for point in self.points:
            point.rect.center = self.get_map_rect(*point.pos)
            self.add(*self.points)

        self.road_map.rect.topleft = self.get_map_rect(0, 0)
        self.add(self.road_map)

    def can_move(self, x, y):
        player_x = (x + self.tile_size // 2) // self.tile_size
        player_y = (y + self.tile_size // 2) // self.tile_size

        tile = self.world.get_tile(player_x, player_y)

        if tile is None:
            return False

        if tile.is_solid:
            return False

        return True
