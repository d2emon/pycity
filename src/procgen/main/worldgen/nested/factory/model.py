class Factory:
    def __call__(self, *args, **kwargs):
        raise NotImplementedError()


class Model:
    def __init__(self, name, *children, factory=None, parent=None):
        self.children_data = []

        self.name = name
        self.factory = factory
        self.parent = parent

        self.add_children(children)

    @property
    def children(self):
        for child_id, child in enumerate(self.children_data):
            if isinstance(child, Factory):
                child = child()
                self.children_data[child_id] = child
            yield child

    def add_children(self, children):
        for child in children:
            self.children_data.append(child)


class Location(Model):
    def __init__(self, name, *children, factory=None, parent=None):
        super().__init__(name, *children, factory=factory, parent=parent)

        self.x = 0
        self.y = 0

        self.width = 0
        self.height = 0

    @property
    def pos(self):
        return self.x, self.y
