import pygame


class Label(pygame.sprite.Sprite):
    default_font_name = 'Arial'
    default_font_size = 8

    def __init__(
        self,
        pos,
        text,
        font = None,
        color = (0, 0, 0),
        center = False,
    ):
        super().__init__()

        self.pos = pos
        self.__text = text
        self.center = center
        self.color = color

        self.font = font or pygame.font.SysFont(
            self.default_font_name,
            self.default_font_size,
        )

        self.render()

    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, value):
        self.__text = value
        self.render()

    def render(self):
        """Redraw text."""
        self.image = self.font.render(self.__text, False, self.color)
        self.rect = self.image.get_rect()
        if self.center:
            self.rect.centerx, self.rect.centery = self.pos
        else:
            self.rect.left, self.rect.top = self.pos
