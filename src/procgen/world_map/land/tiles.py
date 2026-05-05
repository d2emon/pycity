from procgen.main.sprites import tiles


def by_value(size, value):
    water_level = -0.2
    grass_level = 0
    rock_level = 0.2

    if value < water_level:
        return tiles.Water(size, value)
    elif value < grass_level:
        return tiles.Sand(size, value)
    elif value < rock_level:
        return tiles.Grass(size, value)
    else:
        return tiles.Rock(size, value)
