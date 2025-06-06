import logging
from heapq import heappop, heappush


def heuristic(a, b):
    """Манхэттенское расстояние"""
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


class AStar:
    max_height = 0.2

    def __init__(self, heightmap):
        self.heightmap = heightmap

    def is_valid(self, pos):
        if not self.heightmap:
            return True

        if self.heightmap.is_water(pos):
            return False

        height = self.heightmap.get_value(pos)
        if height > self.max_height:
            return False

        return True

    def get_obstacles(self, path):
        for pos in path:
            if not self.is_valid(pos):
                yield pos

    def get_neighbors(self, pos, obstacles):
        """Возвращает соседние тайлы (4-направления)"""
        x, y = pos
        neighbors = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
        # return [n for n in neighbors if n not in obstacles]
        for n in neighbors:
            if self.is_valid(n):
                yield n

    @classmethod
    def build_path(cls, start_pos, end_pos, came_from):
        current = end_pos
        while current in came_from:
            yield current
            current = came_from[current]
        yield start_pos


    def avoid_obstacles(self, original_path, start, end):
        """Обход препятствий с помощью упрощенного A*"""
        if not self.heightmap:
            return original_path

        obstacles = list(self.get_obstacles(original_path))

        # Проверяем, есть ли препятствия на пути
        obstructed = any(not self.is_valid(pos) for pos in original_path)

        if not obstructed:
            return original_path
        
        # Реализация A*
        start_pos = (start[0], start[1])
        open_set = []
        heappush(open_set, (0, start_pos))
        came_from = {}

        start_g = 0
        start_f = heuristic(start_pos, end)
        g_score = {start_pos: start_g}
        f_score = {start_pos: start_f}

        loops = 500
        while open_set:
            loops -= 1
            current = heappop(open_set)[1]
            
            if current == end or loops < 0:
                # Восстанавливаем путь
                return list(self.build_path(start_pos, current, came_from))

            for neighbor in self.get_neighbors(current, obstacles):
                neighbor_pos = (neighbor[0], neighbor[1])
                tentative_g = g_score[current] + 1

                if neighbor_pos not in g_score or tentative_g < g_score[neighbor_pos]:
                    neighbor_g = tentative_g
                    neighbor_f = tentative_g + heuristic(neighbor_pos, end)
                    came_from[neighbor_pos] = current
                    g_score[neighbor_pos] = neighbor_g
                    f_score[neighbor_pos] = neighbor_f
                    heappush(open_set, (f_score[neighbor_pos], neighbor_pos))

        return original_path  # Если обход невозможен, возвращаем оригинальный путь
