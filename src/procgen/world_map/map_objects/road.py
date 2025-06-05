from .map_object import MapObject


class Road(MapObject):
    object_type = "road"
    object_subtype = "asphalt"
    scale = 1.0
    # RPG
    is_interactable = True
    is_enterable = True
    is_fast_travel = True

    def __init__(self, object_id, nodes, width=8.0, **metadata):
        super().__init__(object_id, None, **metadata)

        self.nodes = nodes
        self.width = width
