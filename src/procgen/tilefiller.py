def create_map(world):
    tile_map = []

    for row in world:
        tile_row = []
        for value in row:
            if value < -0.1: tile_row.append("water")  # Вода
            elif value < 0.2: tile_row.append("grass") # Трава
            else: tile_row.append("mountain")          # Горы
        tile_map.append(tile_row)

    return tile_map


special_locations = {
    (12, 34): "castle", 
    (56, 78): "dungeon"
}
