import pygame
from sprites.button import Button
from sprites.image import Image
from sprites.menu_items import MenuItems
from sprites.screen import Screen
from .item import MainMenuItem

class MenuScreen(Screen):
    background_image = "res/global/map.jpg"
    start_rect = pygame.Rect(8, 8, 240, 40)

    def __init__(self, game, *groups):
        super().__init__(game, *groups)

        background = Image(self.rect, self.background_image)
        self.background = pygame.sprite.GroupSingle(background)

        self.menu_items = MenuItems()

        # width = self.start_rect + 8
        height = self.start_rect.height + 8

        rect = self.start_rect.copy()
        MainMenuItem(
            rect,
            'PLAY',
            self.menu_items,
            on_click=self.on_play_click,
        )

        rect = rect.move(0, height)
        MainMenuItem(
            rect,
            'MAP WALK',
            self.menu_items,
            on_click=self.on_play_click,
        )

        rect = rect.move(0, height)
        MainMenuItem(
            rect,
            'QUIT',
            self.menu_items,
            on_click=self.on_quit_click,
        )

    def update(self, *args, **kwargs):
        super().update(*args, **kwargs)

        self.menu_items.update(*args, **kwargs)

        self.background.draw(self.image)
        self.menu_items.draw(self.image)

    # Events

    def on_play_click(self, *args, **kwargs):
        self.game.game_play()

    def on_map_walk_click(self, *args, **kwargs):
        self.game.game_map_walk()

    def on_quit_click(self, *args, **kwargs):
        self.game.stop()
