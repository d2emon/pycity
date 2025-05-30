import pygame
import noise
import sys
import config
from game_map import GameMap
from player import Player
from tiles import get_tile
from world import World


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.is_running = True

        self.background_color = (0, 0, 0)

        self.player = Player(tile_size=config.TILE_SIZE)
        self.world = World.generate_map(config.MAP_WIDTH, config.MAP_HEIGHT, config.TILE_SIZE)
        self.game_map = GameMap(
            self.world,
            (config.SCREEN_WIDTH, config.SCREEN_HEIGHT),
            config.TILE_SIZE,
        )

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False

        keys = pygame.key.get_pressed()
        self.player.check_keys(keys)

    def update(self):
        self.game_map.set_camera(self.screen, self.player.pos)

        self.screen.fill(self.background_color)
        self.game_map.fill(self.screen, self.player)

        # Рендер и логика здесь
        pygame.display.flip()
        self.clock.tick(60)

    def stop(self):
        pygame.quit()
        sys.exit()

    def __call__(self):
        while self.is_running:
            self.check_events()
            self.update()

        self.stop()


if __name__ == "__main__":
    game = Game()
    game()
