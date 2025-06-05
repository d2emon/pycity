from ..map_objects.map_object import MapObject


class Camp(MapObject):
    def __init__(self, id, pos):
        super().__init__(id, pos)
        self.radius = 20


class QuestMarker(MapObject):
    def __init__(self, id, pos, linked_quest):
        super().__init__(id, pos)
        self.linked_quest = linked_quest


class Dungeon(MapObject):
    def __init__(self, id, pos, linked_map):
        super().__init__(id, pos)
        self.linked_map = linked_map


class RPGMap:
    def __init__(self):
        self.player_start = [128, 128]
        self.points = []
