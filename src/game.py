import pygame
import key_input


def create_screen(size, title):
    pygame.display.set_caption(title)
    screen = pygame.display.set_mode(size)
    return screen


class Game:
    def __init__(
        self,
        title="Game",
        window_size=(800, 600),
        background_color=(0, 0, 0),
        delay=16,
        map_size=(1000, 1000),
    ):
        pygame.init()
        pygame.font.init()

        self.screen = create_screen(window_size, title)
        self.background_color = background_color
        self.delay = delay

        self.player_group = pygame.sprite.GroupSingle()
        self.sprites = pygame.sprite.Group()

        self.fonts = {}

        self.running = False

    @property
    def player(self):
        return self.player_group.sprite

    @player.setter
    def player(self, value):
        self.player_group.sprite = value

    # @property
    # def camera(self):
    #     return self.camera.sprite

    # @camera.setter
    # def camera(self, value):
    #     self.camera.sprite = value

    def load(self):
        pass

    def get_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                key_input.keys_down.add(event.key)
            elif event.type == pygame.KEYUP:
                key_input.keys_down.remove(event.key)

            if pygame.K_ESCAPE in key_input.keys_down:
                self.running = False

    def update(self):
        pass

    def set_delay(self):
        pygame.time.delay(self.delay)

    def draw(self):
        self.screen.fill(self.background_color)
        self.sprites.draw(self.screen)

    def play(self):
        self.get_events()

        self.update()
        self.set_delay()
        self.draw()

        pygame.display.flip()

    def stop(self):
        pygame.quit()

    def __call__(self, *args, **kwargs):
        self.load()
        self.running = True

        while self.running:
            self.play()

        self.stop()
