import pygame
from sprites.image import Image
from sprites.screen import Screen
from .items import MainMenuItems


class MenuScreen(Screen):
    BACKGROUND_IMAGE = "res/global/map.jpg"

    def __init__(self, game, *groups):
        super().__init__(game, *groups)

        background = Image(self.rect, self.BACKGROUND_IMAGE)

        self.background = pygame.sprite.GroupSingle(background)
        self.menu_items = MainMenuItems({
            MainMenuItems.BUTTON_PLAY: self.on_play_click,
            MainMenuItems.BUTTON_QUIT: self.on_quit_click,
        })

    def update(self, *args, **kwargs):
        super().update(*args, **kwargs)

        self.menu_items.update(*args, **kwargs)

        self.background.draw(self.image)
        self.menu_items.draw(self.image)

    def on_play_click(self, *args, **kwargs):
        self.game.game_play()

    def on_quit_click(self, *args, **kwargs):
        self.game.stop()
