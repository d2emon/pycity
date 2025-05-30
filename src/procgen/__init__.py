"""Walking in procedure generated world.

Typical usage example:

  game = ProcGen()
  game()
"""

# import pygame
from game.state_game import StateGame
from .main import MainScreenGroup


class ProcGen(StateGame):
    state_screens = {
        StateGame.STATE_PLAYING: MainScreenGroup,
    }

    # State selectors

    def game_play(self):
        self.state = StateGame.STATE_PLAYING

    # Game loop methods

    def start(self):
        super().start()

        self.game_play()

    #   -   -   +   -
    def load(self, window):
        super().load(window)

        # # Игровые параметры
        # self.players = [
        #     Player(
        #         0,
        #         "Игрок 1",
        #         (255, 0, 0),
        #         # 0,
        #         # 1000,
        #         token=pygame.transform.scale(GameResources.get('portraits')[0], (64, 64)),
        #         avatar=GameResources.get('portraits')[0],
        #     ),
        #     Player(
        #         1,
        #         "Игрок 2",
        #         (0, 255, 0),
        #         # 0,
        #         # 1000,
        #         token=pygame.transform.scale(GameResources.get('portraits')[1], (64, 64)),
        #         avatar=GameResources.get('portraits')[1],
        #     ),
        # ]
        # self.current_player_id = None  # Индекс текущего игрока

        # # Создаем список клеток для игрового поля
        # self.field = Field(GameResources.get('logos'))

        # self.player_panel = self.main_gui.player_panel
        # self.tile_panel = self.main_gui.tile_panel

        # self.main_panel = MainPanel(
        #     self.main_gui,
        #     field=self.field,
        # )
        # self.main_gui.main_panel = self.main_panel

        # # Создание кнопки
        # self.next_turn_button = self.main_panel.turn_panel_group.next_turn_button
        # self.next_turn_button.on_click = self.on_next_turn_button_click

        # self.buy_property_button = self.main_panel.action_panel_group.buy_button
        # self.buy_property_button.on_click = self.offer_property

        # # Start player
        # self.current_player_id = 0
        # self.current_player.start_turn()

    #   -   -   +   -
    def update(self):
        super().update()

        # # if pygame.key.get_pressed()[pygame.K_SPACE]:
        # #     self.handle_turn(self.current_player_id)

        # if self.current_player is not None:
        #     self.main_panel.update_data(self.current_player, self.players)
        #     self.player_panel.render(self.current_player)
        #     self.tile_panel.render(self.current_player.turn, self.players)

        #     for e in GameEvent.load(self.current_player.last_event_id):
        #         self.process_event(e)

        # self.main_gui.rect = self.window.get_rect().inflate(0, -18)
        # self.main_gui.update()

    def draw_back(self, screen):
        screen.fill(self.background_color)

    #   -   -   +   -
    def draw(self, screen):
        # # Отрисовка игрового поля
        # self.main_gui.draw(self.window)
        # self.main_panel.draw_panels(self.window)

        super().draw(screen)

        # self.state_screen.draw_level(self)

    # Events

    def on_game_event(self, event):
        super().on_game_event(event)

        #   -   -   +   -
        # # Проверка нажатия кнопки мышью
        # self.next_turn_button.process_event(event)

        #   -   -   +   -
        # # Проверка нажатия клавиши (например, пробел для следующего хода)
        # if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
        #     self.on_next_turn_button_click()

        #   -   -   +   -
        # self.main_panel.process_event(event)


if __name__ == "__main__":
    game = ProcGen()
    game()
