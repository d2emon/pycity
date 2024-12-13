import logging
import pygame
from sprites.image import Image
from sprites.label import Label
from sprites.screen import ScreenGroup
# from . import data
# from .sprites.map import MapSprite
# from .sprites.player import Player

from block_map import BlockMap, MapBlock
from blocks import block_files
from map import TileKind, Map
from my_game.sprites.building import Building
from my_game.sprites.camera import Camera
from my_game.sprites.player import Player


class MainScreenGroup(ScreenGroup):
    """Sprites for main screen.

    Attributes:
      map_sprite (MapSprite): Map sprite.
      player (Player): Player sprite.
    """

    backgroundImage = "res/global/map.jpg"

    ####

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

    def __init__(self, game, *spites):
        """Intialize main sprites

        Args:
            rect (pygame.Rect): Screen rect
        """
        super().__init__(game, *spites)

        rect = game.window.get_rect()
        # self.background = Image(rect, self.backgroundImage)

        ####

        self.player = Player(self.player_image, self.start_pos)

        self.camera = Camera(
            self.game.window_size,
            (16 * 32 * 3, 16 * 32 * 3),
            self.game.background_color,
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
                # camera.foreground_sprites,
            )

        self.game.fonts["my"] = pygame.font.SysFont('Comic Sans MS', 24)
        # myfont = pygame.font.SysFont('Sans', 16)

        # bg = Background(config.WINDOW_SIZE)

        # game_map = BgMap(*config.MAP_POS)
        # hero = Player(*config.PLAYER_POS)
        # xvel = yvel = 0

        # show_grid = False
        # map_grid = MapGrid(game_map.rect.width, game_map.rect.height, config.GRID_SIZE)

        self.player_pos = Label(
            (0, 0),
            f"{self.player.x}, {self.player.y}",
            font=self.game.fonts["my"],
            color=(255, 0, 0),
        )

        self.block_pos = Label(
            (0, 24),
            f"{self.block_map.x}, {self.block_map.y}",
            font=self.game.fonts["my"],
            color=(255, 0, 0),
        )

        self.start()

    def start(self):
        # if not self.player.has_started:
        #     self.player.start(self.map_sprite)
        pass

    def update(self, *args, **kwargs):
        self.empty()
        # self.add(self.background)

        # logging.debug("Event: MY_GAME.UPDATE")

        super().update(*args, **kwargs)

        player_group = pygame.sprite.GroupSingle(self.player)

        self.camera.update(player=player_group)
        self.add(self.camera, layer=5)
        # self.sprites.update(player=self.player_group)

        self.player.update(game_map=self.block_map)
        self.add(self.player, layer=10)
        # self.player_group.update(game_map=self.block_map)

        ####

        # bg.draw(window)

        # self.player_pos_text = self.game.fonts["my"].render(f"{self.player.x}, {self.player.y}", False, (255, 0, 0))
        # self.block_pos_text = self.game.fonts["my"].render(f"{self.block_map.x}, {self.block_map.y}", False, (255, 0, 0))

        self.player_pos.text = f"{self.player.x}, {self.player.y}"
        self.add(self.player_pos, layer=50)

        self.block_pos.text = f"{self.block_map.x}, {self.block_map.y}"
        self.add(self.block_pos, layer=50)

        logging.debug(f"{list(self)}")
        logging.debug(f"{self.player_pos.text}")
        logging.debug(f"{self.block_pos.text}")

        # game_map.update(xvel, yvel)
        # game_map.draw(window)

        # if show_grid:
        #     map_grid.draw(window)

        # hero.draw(window)

        # coords = "{}, {}".format(game_map.x, game_map.y)
        # text_surface = myfont.render(coords, False, (0, 0, 0))
        # window.blit(text_surface, (0, 0))

        # pygame.display.update()
