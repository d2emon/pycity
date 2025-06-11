import random
from .model import Factory, Location, Model


class NameFactory(Factory):
    def __init__(self, value):
        self.value = value

    def __call__(self, *args, **kwargs):
        return self.value


class SizeFactory(Factory):
    def __init__(self, min_size=8, max_size=32):
        self.min_width = min_size
        self.max_width = max_size
        self.min_height = min_size
        self.max_height = max_size

    def width(self):
        return random.randint(self.min_width, self.max_width) if self.min_width < self.max_width else self.min_width

    def height(self):
        return random.randint(self.min_height, self.max_height) if self.min_height < self.max_height else self.min_height

    def __call__(self, *args, **kwargs):
        return self.width(), self.height()


class NestedFactory(Factory):
    default_name = ''
    factory_id = ''

    model = Model

    def __init__(self, parent=None, **kwargs):
        self.parent = parent
        self.options = kwargs

        self.name_factory = NameFactory(self.default_name)

    def model_factory(self, parent=None):
        name = self.name_factory()
        return self.model(name, factory=self, parent=parent)

    def child_factories(self):
        yield from []

    def child(self, factory, parent=None):
        return factory(parent)

    def __call__(self, parent=None, *args, **kwargs):
        model = self.model_factory(parent=parent)

        model.add_children(self.child(factory, model) for factory in self.child_factories())

        return model

    @classmethod
    def multiple(cls, min_amount, max_amount=None):
        amount = min_amount if max_amount is None else random.randint(min_amount, max_amount)
        for _ in range(amount):
            yield cls


class NestedLocationFactory(NestedFactory):
    model = Location

    def __init__(self, parent=None, **kwargs):
        super().__init__(parent, **kwargs)

        self.size_factory = SizeFactory()
        self.size_factory.max_width = self.width
        self.size_factory.max_height = self.height

    @property
    def width(self):
        return self.options.get('width', 0)

    @property
    def height(self):
        return self.options.get('height', 0)

    def pos_factory(self):
        x = random.randint(0, self.width) if self.width > 0 else 0
        y = random.randint(0, self.height) if self.height > 0 else 0
        return x, y

    def child(self, factory, parent=None):
        if issubclass(factory, NestedLocationFactory):
            return factory(parent, width=parent.width, height=parent.height)
        else:
            return factory(parent)

    def __call__(self, parent=None, *args, **kwargs):
        model = self.model_factory(parent=parent)

        x, y = self.pos_factory()
        model.x = x
        model.y = y

        width, height = self.size_factory()
        model.width = width
        model.height = height

        model.add_children(self.child(factory, model) for factory in self.child_factories())

        return model
