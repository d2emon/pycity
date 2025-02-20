import logging
import pygame
import events.keys
from . import Game, states


game_logger = logging.getLogger('state-game')


class StateGame(Game):
    STATE_EXIT = states.EXIT
    STATE_GAME_OVER = states.GAME_OVER
    STATE_INITIALIZATION = states.INITIALIZATION
    STATE_PLAYING = states.PLAYING
    STATE_WIN = states.WIN

    screens = {}

    def __init__(
        self,
        title="Game",
        window_size=(640, 480),
        background_color=(0, 0, 0),
        delay=16,
        # fps=60,
        **config,
    ):
        """Initialize game window.

        Old Args:
            fps (int, optional): _description_. Defaults to 60.

        Args:
            title (str, optional): Window title (caption). Defaults to "Game".
            window_size (tuple, optional): Window width and height (size). Defaults to (800, 600).
            background_color (tuple, optional): Background color for screen. Defaults to (0, 0, 0).
            delay (int, optional): Delay before next tick. Defaults to 16.
        """
        super().__init__(
            title=title,
            window_size=window_size,
            background_color=background_color,
            delay=delay,
            # fps=fps,
            **config,
        )

        game_logger.debug("Initializing game with states")

        # Set game fields
        # self.players = []
        # self.current_player_id = None  # Индекс текущего игрока
        # self.field = None

        # self.game_is_over = False
        self.__state = self.STATE_INITIALIZATION
        # self.objects = []

        # # Спрайты
        # self.main_gui = MainGUI()
        # self.player_panel = None
        # self.main_panel = None
        # self.tile_panel = None

        self.__screen_group = pygame.sprite.Group()

        # # Создание кнопки
        # self.next_turn_button = None
        # self.buy_property_button = None

        # Set INIT error on init
        # Set UPDATE error on update
        # Set DRAW error on draw
        # Set KEY_UP error on key up
        # Set KEY_DOWN error on key down

    def load(self):
        # # Load resources
        # GameResources.load()

        super().load()

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

    # Getters and setters

    @property
    def screen(self):
        """Get current screen.

        Returns:
            pygame.sprite.Sprite: Current screen sprite.
        """
        return self.__screen_group

    @screen.setter
    def screen(self, value):
        """Set current screen.

        Args:
            value (pygame.sprite.Sprite): New screen sprite.
        """
        self.__screen_group = value

        # Add screen events to handlers
        # Add custom events to handlers
        # Add screen to event listeners

    @property
    def state(self):
        """Get current state.

        Returns:
            string: Current game state.
        """
        return self.__state

    @state.setter
    def state(self, value):
        """Set new state and change screen.

        Args:
            value (string): New game state.
        """
        game_logger.debug(f"[State: {value}]")

        self.__state = value

        screen = self.screens.get(value)
        if screen is None:
            return

        self.screen = screen(self)

    @property
    def is_running(self):
        """Get if game is running (playing).

        Returns:
            bool: Game is running.
        """
        return self.state != self.STATE_EXIT

    @is_running.setter
    def is_running(self, value):
        """Set game is running (playing).

        Args:
            value (bool): Game is running.
        """
        if value:
            self.__state = self.STATE_PLAYING
        else:
            self.__state = self.STATE_EXIT

    # Game loop setters

    def start(self):
        """Start game."""
        game_logger.debug("Starting game with states")

        self.__state = self.STATE_PLAYING

    def stop(self):
        """Stop game."""
        game_logger.debug("Stopping game with states")

        self.__state = self.STATE_EXIT

    def game_win(self):
        """Win game."""
        game_logger.debug("Winning game with states")

        self.__state = self.STATE_WIN

    def game_loose(self):
        """Loose game."""
        game_logger.debug("Loosing game with states")

        self.__state = self.STATE_GAME_OVER

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

        # self.main_gui.rect = self.screen.get_rect().inflate(0, -18)
        # self.main_gui.update()

        self.__screen_group.update()

    def draw(self):
        # # Отрисовка игрового поля
        # self.main_gui.draw(self.screen)
        # self.main_panel.draw_panels(self.screen)

        self.__screen_group.draw(self.window)

        super().draw()

    # Events

    def on_game_event(self, event):
        super().on_game_event(event)

        # # Проверка нажатия кнопки мышью
        # self.next_turn_button.process_event(event)

        # # Проверка нажатия клавиши (например, пробел для следующего хода)
        # if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
        #     self.on_next_turn_button_click()

        # self.main_panel.process_event(event)
