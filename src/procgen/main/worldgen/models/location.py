from .model import Model


class Location(Model):
    def __init__(self, object_id, name, *children, factory=None, parent=None):
        super().__init__(object_id, name, *children, factory=factory, parent=parent)

        self.x = 0
        self.y = 0

        self.width = 0
        self.height = 0

    @property
    def pos(self):
        return self.x, self.y
