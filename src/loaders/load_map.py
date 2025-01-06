def load_map(filename):
    with open(filename, 'r') as file:
        for line in file:
            row = []

            for tile_number in line.strip():
                tile_code = int(tile_number)
                row.append(tile_code)

            yield row


def load_map_block(filename):
    with open(filename, 'r') as file:
        for line in file:
            row = []
            char_id = 0
            tile_code = ''

            for tile_number in line.strip():
                tile_code += tile_number

                if char_id >= 1:
                    row.append(tile_code)
                    char_id = 0
                    tile_code = ''
                else:
                    char_id += 1

            yield row
