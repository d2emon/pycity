import noise
import numpy as np

def generate():
    world_shape = (100, 100)  # Чанков, не пикселей!
    scale = 50.0
    octaves = 6
    persistence = 0.5
    lacunarity = 2.0

    world = np.zeros(world_shape)
    for i in range(world_shape[0]):
        for j in range(world_shape[1]):
            world[i][j] = noise.pnoise2(
                i/scale,
                j/scale,
                octaves=octaves,
                persistence=persistence,
                lacunarity=lacunarity,
            )

    return world
