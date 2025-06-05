from .map_object import MapObject


class Tree(MapObject):
    object_type = "tree"
    scale = 1.2
    # RPG
    is_interactable = True

    def __init__(self, object_id, position, **metadata):
        super().__init__(object_id, position, wood_yield=5, **metadata)


class Oak(Tree):
    object_subtype = "oak"
    scale = 1.2
