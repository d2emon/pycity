import pygame
from sprites.image import Image
from sprites.screen import Screen, ScreenGroup
from .items import MainMenuItems


class MenuScreenGroup(ScreenGroup):
    background_image = "res/global/map.jpg"

    def __init__(self, game, *spites):
        super().__init__(game, *spites)

        rect = self.game.window.get_rect()
        self.background = Image(rect, self.background_image)
        self.add(self.background)

        self.menu_items = MainMenuItems({
            MainMenuItems.BUTTON_PLAY: self.on_play_click,
            MainMenuItems.BUTTON_QUIT: self.on_quit_click,
        })
        for menu_item in self.menu_items:
            self.add(menu_item, layer=10)

    def on_play_click(self, *args, **kwargs):
        self.game.game_play()

    def on_quit_click(self, *args, **kwargs):
        self.game.stop()


class MenuScreen(Screen):
    def create_group(self):
        return MenuScreenGroup(self.game)
