import pygame
from loaders.load_map import load_map
from my_game.sprites.map_sprite import MapSprite


class TileKind:
    def __init__(self, name, image, is_solid):
        self.name = name
        self.image = pygame.image.load(image)
        self.is_solid = is_solid


class Map:
    def __init__(self, map_file, tile_kinds, tile_size):
        self.tile_kinds = tile_kinds
        self.tile_size = tile_size        
        self.tiles = list(load_map(map_file))
        self.sprite_group = pygame.sprite.pygame.sprite.Group()

    def update(self, *groups):
        for y, row in enumerate(self.tiles):
            for x, tile in enumerate(row):
                image = self.tile_kinds[tile].image
                pos = (
                    x * self.tile_size,
                    y * self.tile_size,
                )
                sprite = pygame.sprite.Sprite(self.sprite_group, *groups)
                sprite.image = image
                sprite.rect = image.get_rect()
                sprite.rect.centerx, sprite.rect.centery = pos
                sprite.is_solid = self.tile_kinds[tile].is_solid

    def draw(self, surface):
        self.sprite_group.draw(surface)
