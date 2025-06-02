from .map_object import MapObject


class Building(MapObject):
    object_type = "building"
    scale = 1.0
    # RPG
    is_interactable = True
    is_enterable = True

    def __init__(self, object_id, footprint, **metadata):
        super().__init__(object_id, None, **metadata)

        self.footprint = footprint
        self.floors = 3
        self.npcs = ["mayor_npc"]


class GovernmentBuilding(Building):
    object_subtype = "government"
