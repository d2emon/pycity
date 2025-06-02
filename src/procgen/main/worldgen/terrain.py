class Terrain:
    terrain_id = 0
    terrain_type = None
    is_walkable = True
    speed = 1

    @classmethod
    def export(cls):
        return {
            "id": cls.terrain_id,
            "type": cls.terrain_type,
            "rpg_walkable": cls.is_walkable,
            "rpg_speed": cls.speed,
        }


class Grass(Terrain):
    terrain_id = 0
    terrain_type = "grass"
    is_walkable = True


class Rock(Terrain):
    terrain_id = 1
    terrain_type = "rock"
    is_walkable = False


class Water(Terrain):
    terrain_id = 2
    terrain_type = "water"
    speed = 0.3


class TerrainData:
    def __init__(self, *textures):
        self.heightmap = "map_height.raw" # Бинарный файл (float32)
        self.texture_map = "texture_index.bin" # Индексы текстур (uint8)
        self.textures = list(textures)

    @property
    def __texture_defs(self):
        for texture in self.textures:
            yield texture.export()

    def export(self):
        return {
            "heightmap": self.heightmap,
            "texture_map": self.texture_map,
            "texture_defs": list(self.__texture_defs),
        }
