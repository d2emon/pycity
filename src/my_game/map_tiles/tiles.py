from my_game.map_tiles.tileset_image import TilesetImage


def create_starter_tiles(source):
    tileset_image_starter = TilesetImage(source)
    return {
        'S0': tileset_image_starter.create_tile("start00", False, (0, 0, 64, 64)),
        'S1': tileset_image_starter.create_tile("start10", False, (0, 64, 64, 64)),
        'S2': tileset_image_starter.create_tile("start20", False, (0, 128, 64, 64)),
        'S3': tileset_image_starter.create_tile("start30", False, (0, 192, 64, 64)),
        'S4': tileset_image_starter.create_tile("start40", False, (0, 256, 64, 64)),
        'S5': tileset_image_starter.create_tile("start50", False, (0, 320, 64, 64)),

        'S8': tileset_image_starter.create_tile("start01", False, (64, 0, 64, 64)),
        'S9': tileset_image_starter.create_tile("start11", False, (64, 64, 64, 64)),
        'SA': tileset_image_starter.create_tile("start21", False, (64, 128, 64, 64)),
        'SB': tileset_image_starter.create_tile("start31", False, (64, 192, 64, 64)),
        'SC': tileset_image_starter.create_tile("start41", False, (64, 256, 64, 64)),
        'SD': tileset_image_starter.create_tile("start51", False, (64, 320, 64, 64)),

        'SG': tileset_image_starter.create_tile("start02", False, (128, 0, 64, 64)),
        'SH': tileset_image_starter.create_tile("start12", False, (128, 64, 64, 64)),
        'SI': tileset_image_starter.create_tile("start22", False, (128, 128, 64, 64)),
        'SJ': tileset_image_starter.create_tile("start32", False, (128, 192, 64, 64)),
        'SK': tileset_image_starter.create_tile("start42", False, (128, 256, 64, 64)),
        'SL': tileset_image_starter.create_tile("start52", False, (128, 320, 64, 64)),

        'SO': tileset_image_starter.create_tile("start03", False, (192, 0, 64, 64)),
        'SP': tileset_image_starter.create_tile("start13", False, (192, 64, 64, 64)),
        'SQ': tileset_image_starter.create_tile("start23", False, (192, 128, 64, 64)),
        'SR': tileset_image_starter.create_tile("start33", False, (192, 192, 64, 64)),
        'SS': tileset_image_starter.create_tile("start43", False, (192, 256, 64, 64)),
        'ST': tileset_image_starter.create_tile("start53", False, (192, 320, 64, 64)),
    }


def create_main_tiles(source):
    tileset_image_main = TilesetImage(source)
    return {
        '00': tileset_image_main.create_tile("tile0", True, (447, 128, 64, 64)),
        '01': tileset_image_main.create_tile("tile1", False, (447, 192, 64, 64)),
        'R0': tileset_image_main.create_tile("cross", False, (447, 0, 64, 64)),
        'R1': tileset_image_main.create_tile("roadH", False, (447, 640, 64, 64)),
        'R2': tileset_image_main.create_tile("roadV", False, (512, 640, 64, 64)),
        'T0': tileset_image_main.create_tile("railX", False, (447, 0, 64, 64)),
        'T1': tileset_image_main.create_tile("railH", False, (447, 640, 64, 64)),
        'T2': tileset_image_main.create_tile("railV", False, (512, 640, 64, 64)),
    }
