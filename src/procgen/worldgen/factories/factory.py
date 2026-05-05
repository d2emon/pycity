class Factory:
    def __call__(self, *args, **kwargs):
        raise NotImplementedError()


class NameFactory(Factory):
    def __init__(self, value):
        self.value = value

    def __call__(self, *args, **kwargs):
        return self.value

    def multiple(self, *args, count=10, **kwargs):
        for _ in range(count):
            yield self(*args, **kwargs)
