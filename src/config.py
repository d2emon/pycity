import logging
import os


logging.basicConfig(level=logging.DEBUG)


class WindowConfig:
    caption = "Mapper"
    block_size = 8
    width = block_size * 80
    height = block_size * 60


class BigWindowConfig(WindowConfig):
    width = 800
    height = 640


class SmallWindowConfig(WindowConfig):
    width = 640
    height = 480


class ColorSchema:
    background = 0, 0, 0


class ColorSchema1:
    background = 30, 150, 50


class ColorSchema2:
    background = 0, 153, 255


window_config = SmallWindowConfig
color_schema = ColorSchema2

CAPTION = window_config.caption
WIN_WIDTH = window_config.width
WIN_HEIGHT = window_config.height

WINDOW_SIZE = WIN_WIDTH, WIN_HEIGHT

BACKGROUND_COLOR = color_schema.background

DELAY = 16
# FPS = 60

## Player

# PLAYER_POS = (WIN_WIDTH / 2, WIN_HEIGHT / 2)
# MAP_POS = (0, 0)
# GRID_SIZE = 32

## Files

BASE_PATH = os.path.abspath(os.path.join(__file__, '..', '..', 'res'))

## Config

## > space

"""
FRAME_RATE = 60
GRID_SIZE = 32

PLAYER_SIZE = 10
PLAYER_VIEW = 5 * SCALE
PLAYER_COLOR = (255, 255, 0)
PLAYER_VIEW_COLOR = (0, 0, 255)
"""

## > games.walker.resource

"""
class Universe:
    GLOBAL_MAP = os.path.join(BASE_PATH, 'universe.png')
    PLAYER = os.path.join(BASE_PATH, 'saucer.png')
"""

## Services

"""
# > services.auth
HOST_MACHINE = "DAVIDPOOTER"
"""
