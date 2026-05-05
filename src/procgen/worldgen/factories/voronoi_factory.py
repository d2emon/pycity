from scipy.spatial import Voronoi


class GraphMap:
    def __init__(self):
        self.centers = []
        self.vertices = []
        self.ridges = []

    @property
    def points(self):
        yield from self.centers
        yield from self.vertices


class VoronoiFactory:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def generate(self, points):
        graph_map = GraphMap()
        graph_map.centers = list(points)

        vor = Voronoi(graph_map.centers)

        graph_map.vertices = [
            [int(x), int(y)]
            for x, y in vor.vertices
        ]

        for road_id, simplex in enumerate(vor.ridge_vertices):
            if -1 not in simplex:  # Игнорируем рёбра, уходящие в бесконечность
                start = graph_map.vertices[simplex[0]]
                end = graph_map.vertices[simplex[1]]
                graph_map.ridges.append([start, end])

        return graph_map
