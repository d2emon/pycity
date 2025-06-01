import logging
import os


logging.basicConfig(level=logging.DEBUG)


WIN_WIDTH = 640 # 800 # 640
WIN_HEIGHT = 480 # 640 # 460 # 600

CAPTION = "Mapper"
WINDOW_SIZE = WIN_WIDTH, WIN_HEIGHT
BACKGROUND_COLOR = 0, 0, 0 # 30, 150, 50 # "#0099FF"
DELAY = 16
# FPS = 60


# PLAYER_POS = (WIN_WIDTH / 2, WIN_HEIGHT / 2)
# MAP_POS = (0, 0)
# GRID_SIZE = 32

## Files

BASE_PATH = os.path.abspath(os.path.join(__file__, '..', '..', 'res'))

## Config

"""
# > games.map_walk
# > games.walker
# > space
class SCREEN:
    WIDTH = WIN_WIDTH
    HEIGHT = WIN_HEIGHT
    SIZE = WIDTH, HEIGHT
    CAPTION = CAPTION
    CENTER = (WIDTH / 2, HEIGHT / 2)

PLAYER_POS = WIN_WIDTH / 2, WIN_HEIGHT / 2
MAP_POS = (0, 0)
BACKGROUND_COLOR = "#0099FF"
# > space
FRAME_RATE = 60
GRID_SIZE = 32

PLAYER_SIZE = 10
PLAYER_VIEW = 5 * SCALE
PLAYER_COLOR = (255, 255, 0)
PLAYER_VIEW_COLOR = (0, 0, 255)

# > games.walker.resource
class Universe:
    ### ???
    # BASE_PATH = os.path.join(files.BASE_PATH, 'walker', 'universe')
    GLOBAL_MAP = os.path.join(BASE_PATH, 'universe.png')
    PLAYER = os.path.join(BASE_PATH, 'saucer.png')
"""

## Services

"""
# > services.auth
HOST_MACHINE = "DAVIDPOOTER"
"""
