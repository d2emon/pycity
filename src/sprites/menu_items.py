import pygame


class MenuItems(pygame.sprite.Group):
    """Game menu sprite."""

    margins = 5, 5

    def __init__(self, *items):
        super().__init__(*items)

        self.horyzontal = False

        self.align_items()

    def align_items(self):
        top = 0
        left = 0

        for item in self:
            item.rect.left = left + self.margins[0]
            item.rect.top = top + self.margins[1]

            if self.horyzontal:
                left = item.rect.right + self.margins[0]
            else:
                top = item.rect.bottom + self.margins[1]
