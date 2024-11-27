keys_down = set()


def set_pressed(key):
    keys_down.add(key)


def unset_pressed(key):
    keys_down.remove(key)


def is_key_pressed(keys):
    return keys in keys_down
