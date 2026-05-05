import logging


game_logger = logging.getLogger('game.event')
game_logger.setLevel(logging.WARNING)

window_logger = logging.getLogger('window.event')
window_logger.setLevel(logging.WARNING)
