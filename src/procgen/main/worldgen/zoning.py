class Zone:
    def __init__(self, id, vertices):
        self.id = id
        self.vertices = vertices

    def export(self):
        return {
            "id": self.id,
            "vertices": self.vertices,
        }


class ResidentialZone(Zone):
    pass


class CommercialZone(Zone):
    pass


class IndustrialZone(Zone):
    pass
