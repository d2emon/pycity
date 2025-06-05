class MapObject:
    object_type = None
    object_subtype = None
    scale = 1.0
    is_interactable = False

    def __init__(self, object_id, pos=None, **metadata):
        self.id = object_id
        self.pos = pos
        # RPG
        self.metadata = metadata
