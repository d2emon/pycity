class Model:
    def __init__(self, object_id, name, *children, factory=None, parent=None):
        self.children_data = []

        self.object_id = object_id
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
