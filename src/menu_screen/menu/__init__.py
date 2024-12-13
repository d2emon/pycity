import pygame
from sprites.image import Image
from sprites.screen import Screen, ScreenGroup
from .item import MainMenuItem
from .items import MainMenuItems


class MenuScreenGroup(ScreenGroup):
    background_image = "res/global/map.jpg"
    start_rect = pygame.Rect(8, 8, 240, 40)

    def __init__(self, game, *spites):
        super().__init__(game, *spites)

        rect = self.game.window.get_rect()
        self.background = Image(rect, self.background_image)
        self.add(self.background)

        self.menu_items = MainMenuItems(
            MainMenuItem("Play", self.on_play_click),
            MainMenuItem("Walk Map", self.on_map_walk_click),
            MainMenuItem("City", self.on_city_click),
            MainMenuItem("Quit", self.on_quit_click),
        )

        for menu_item in self.menu_items:
            self.add(menu_item, layer=10)

    def on_play_click(self, *args, **kwargs):
        self.game.game_play()

    def on_map_walk_click(self, *args, **kwargs):
        self.game.game_map_walk()

    def on_city_click(self, *args, **kwargs):
        self.game.game_city()

    def on_quit_click(self, *args, **kwargs):
        self.game.stop()


class MenuScreen(Screen):
    def create_group(self):
        return MenuScreenGroup(self.game)
