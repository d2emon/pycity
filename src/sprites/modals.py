import pygame


class Modals(pygame.sprite.Group):
    def on_game_event(self, event):
        for modal in self:
            modal.on_game_event(event)

    def update(self, *args, **kwargs):
        super().update(*args, **kwargs)

        for modal in self:
            if not modal.visible:
                self.remove(modal)
