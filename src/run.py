#! /usr/bin/python
import config
from menu_screen import MenuScreen as Game
# from bgmap import BgMap
# from grid import MapGrid

# from games.walker import Walker

# import uuid
# from gamelib.temp_mud.game import Game

# # from games.middleearth import MiddleEarth as Game
# from games.space import Space as Game

# from games.worlds import world_walker

"""
# from utils.state_game import StateGame
# from windows.controls import TextObject
# from . import events, states
"""


# start_pos = (
#     16 * tile_size + 32 * tile_size,
#     16 * tile_size + 32 * tile_size,
# )


"""
## 3. walker

    game = Walker()

## 4. mud

    # TODO: Move to log
    print(">", "mud.1", "-nName")
    game = Game(uuid.uuid1(), "Phantom", 0)

## 5. space

    game = Game(
        frame_rate=config.FRAME_RATE,
        width=config.SCREEN.WIDTH,
        height=config.SCREEN.HEIGHT,
        caption=config.SCREEN.CAPTION,
    )

    ----

    ## 1. 2. 3.

    game()

    ## 4. 5.

    game.play()
    game.end_game()

## 6.
    world_walker()
"""


if __name__ == "__main__":
    Game.run()
