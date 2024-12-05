import pygame
from sprites.image import Image
from sprites.screen import Screen
from .items import MainMenuItems


class MenuScreenGroup(pygame.sprite.LayeredUpdates):
    backgroundImage = "res/global/map.jpg"

    def __init__(self, game, *spites):
        super().__init__(*spites)


        self.game = game
 
        self.background = Image(self.rect, self.backgroundImage)
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
    def __init__(self, game, *groups):
        super().__init__(game, *groups)

        self.sprites = MenuScreenGroup(game)
