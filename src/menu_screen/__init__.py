import pygame
from game import states
from game.state_game import StateGame
from breakout.main import MainScreenGroup as BreakoutScreen
from map_walk.main import MainScreenGroup as MapWalkScreen
from my_game.main import MainScreenGroup as CityScreen
from .menu import MenuScreenGroup
from .menu.item import MainMenuItem


class MenuScreen(StateGame):
    MENU = 'BREAKOUT.MENU'
    PLAYING = states.PLAYING
    MAP_WALK = 'MAP_WALK'
    PLAY_CITY = 'PLAY_CITY'

    state_screens = {
        MENU: MenuScreenGroup,
        PLAYING: BreakoutScreen,
        MAP_WALK: MapWalkScreen,
        PLAY_CITY: CityScreen,
    }

    def __init__(self, window, **game_config):
        super().__init__(window, **game_config)

        # Set game fields
        # self.players = []
        # self.current_player_id = None  # Индекс текущего игрока
        # self.field = None

        # # Спрайты
        # self.main_gui = MainGUI()
        # self.player_panel = None
        # self.main_panel = None
        # self.tile_panel = None

        # # Создание кнопки
        # self.next_turn_button = None
        # self.buy_property_button = None

    def game_menu(self):
        self.state = self.MENU

    def game_play(self):
        self.state = self.PLAYING

    def game_map_walk(self):
        self.state = self.MAP_WALK

    def game_city(self):
        self.state = self.PLAY_CITY

    def start(self):
        super().start()
        self.game_menu()

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

    # Game loop methods

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

    def draw(self, screen):
        # # Отрисовка игрового поля
        # self.main_gui.draw(self.window)
        # self.main_panel.draw_panels(self.window)

        super().draw(screen)

    # Events

    def on_game_event(self, event):
        super().on_game_event(event)

        if event.type == MainMenuItem.EVENT_MENU_BUTTON:
            if event.button == "BREAKOUT":
                self.game_play()
            elif event.button == "MAP_WALK":
                self.game_map_walk()
            elif event.button == "CITY":
                self.game_city()
            elif event.button == "QUIT":
                self.stop()
            return

        # # Проверка нажатия кнопки мышью
        # self.next_turn_button.process_event(event)

        # # Проверка нажатия клавиши (например, пробел для следующего хода)
        # if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
        #     self.on_next_turn_button_click()

        # self.main_panel.process_event(event)


if __name__ == "__main__":
    MenuScreen.run()
