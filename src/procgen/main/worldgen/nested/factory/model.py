class Factory:
    def __call__(self, *args, **kwargs):
        raise NotImplementedError()
