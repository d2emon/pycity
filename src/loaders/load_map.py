def load_map(filename):
        with open(filename, 'r') as file:
            for line in file:
                row = []

                for tile_number in line.strip():
                    row.append(int(tile_number))

                yield row
