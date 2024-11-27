buttons_down = set()


def set_pressed(button):
    buttons_down.add(button)


def unset_pressed(button):
    buttons_down.remove(button)


def is_pressed(buttons):
    return buttons in buttons_down
