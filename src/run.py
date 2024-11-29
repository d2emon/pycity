#! /usr/bin/python
import logging
import pygame
import config
from block_map import BlockMap, MapBlock
from blocks import block_files
# from breakout import Breakout as Game
from menu_screen import MenuScreen as Game
from map import TileKind, Map
from my_game.sprites.building import Building
from my_game.sprites.camera import Camera
from my_game.sprites.player import Player
# from my_game.player import Player
# from bgmap import BgMap
# from my_game.sprites.background import Background
# from grid import MapGrid

# from games.breakout import Breakout
# from games.map_walk import MapWalk
# from games.walker import Walker

# import uuid
# from gamelib.temp_mud.game import Game

# # from games.middleearth import MiddleEarth as Game
# from games.space import Space as Game

# from games.worlds import world_walker

"""
# from utils.state_game import StateGame
# from windows.controls import TextObject
# from . import events, states
"""


logging.basicConfig(level=config.LOG_LEVEL)


class MyGame(Game):
    tile_size = 16
    block_size = 32 * tile_size
    start_pos = 16 * tile_size, 16 * tile_size
    start_block = 32, 16

    image_folder = "images"
    player_image = f"{image_folder}/player.png"
    building_image = f"{image_folder}/building1.png"

    buildings = (
        # (3, 5),
        # (5, 9),
        # (10, 8),
        # (7, 3),
        # (13, 5),
        # (5, 7),
    )

    def load(self):
        self.player = Player(self.player_image, self.start_pos)

        self.camera = Camera(
            config.WINDOW_SIZE,
            (16 * 32 * 3, 16 * 32 * 3),
            self.background_color,
            self.sprites,
        )

        tile_kinds = [
            TileKind("tile0", f"{self.image_folder}/tile0.png", True),
            TileKind("tile1", f"{self.image_folder}/tile1.png", False),
            TileKind("cross", f"{self.image_folder}/cross.png", False),
            TileKind("roadH", f"{self.image_folder}/roadH.png", False),
            TileKind("roadV", f"{self.image_folder}/roadV.png", False),
            TileKind("railX", f"{self.image_folder}/railX.png", False),
            TileKind("railH", f"{self.image_folder}/railH.png", False),
            TileKind("railV", f"{self.image_folder}/railV.png", False),
        ]

        map_blocks = [
            MapBlock(filename, tile_kinds, self.tile_size)
            for filename in block_files
        ]
        self.block_map = BlockMap("maps/v0.map", map_blocks, self.block_size, self.start_block)
        self.block_map.update()
        self.camera.background_sprites = self.block_map.sprite_group

        self.camera.foreground_sprites.empty()
        for x, y in self.buildings:
            Building(
                self.building_image,
                (x * self.tile_size * 4, y * self.tile_size * 4),
                camera.foreground_sprites,
            )

        self.fonts["my"] = pygame.font.SysFont('Comic Sans MS', 24)
        # myfont = pygame.font.SysFont('Sans', 16)

        # bg = Background(config.WINDOW_SIZE)

        # game_map = BgMap(*config.MAP_POS)
        # hero = Player(*config.PLAYER_POS)
        # xvel = yvel = 0

        # show_grid = False
        # map_grid = MapGrid(game_map.rect.width, game_map.rect.height, config.GRID_SIZE)

    def update(self):
        super().update()

        # logging.debug("Event: MY_GAME.UPDATE")
        self.sprites.update(player=self.player_group)
        self.player_group.update(game_map=self.block_map)

        # bg.draw(window)

        self.player_pos_text = self.fonts["my"].render(f"{self.player.x}, {self.player.y}", False, (255, 0, 0))
        self.block_pos_text = self.fonts["my"].render(f"{self.block_map.x}, {self.block_map.y}", False, (255, 0, 0))

        # game_map.update(xvel, yvel)
        # game_map.draw(window)

        # if show_grid:
        #     map_grid.draw(window)

        # hero.draw(window)

        # coords = "{}, {}".format(game_map.x, game_map.y)
        # text_surface = myfont.render(coords, False, (0, 0, 0))
        # window.blit(text_surface, (0, 0))

        # pygame.display.update()

    def draw(self):
        super().draw()

        # logging.debug("Event: MY_GAME.DRAW")
        self.window.blit(self.player_pos_text, (0, 0))
        self.window.blit(self.block_pos_text, (0, 24))


def run():
    game = MyGame(
        title=config.CAPTION,
        window_size=config.WINDOW_SIZE,
        background_color=config.BACKGROUND_COLOR,
        delay=config.DELAY,
        # fps=60,
    )

    # start_pos = (
    #     16 * tile_size + 32 * tile_size,
    #     16 * tile_size + 32 * tile_size,
    # )


    game()
    """
    ## 2. map_walk

    game = MapWalk()

    ## 3. walker

    game = Walker()

    ## 4. mud

    # TODO: Move to log
    print(">", "mud.1", "-nName")
    game = Game(uuid.uuid1(), "Phantom", 0)

    ## 5. space

    game = Game(
        frame_rate=config.FRAME_RATE,
        width=config.SCREEN.WIDTH,
        height=config.SCREEN.HEIGHT,
        caption=config.SCREEN.CAPTION,
    )

    ----

    ## 1. 2. 3.

    game()

    ## 4. 5.

    game.play()
    game.end_game()

    ## 6.

    world_walker()
    """

if __name__ == "__main__":
    run()
