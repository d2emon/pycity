import logging
from .a_star import AStar

def build_road(start, end, heightmap=None, smooth=True):
    """
    Построение дороги между тайлами start(x,y) и end(x,y)
    
    Параметры:
        start : tuple    - стартовая координата (x,y)
        end : tuple      - конечная координата (x,y)
        obstacles : set  - множество непроходимых тайлов {(x,y), ...}
        smooth : bool    - сглаживание углов
        
    Возвращает:
        list - [(x1,y1), (x2,y2), ...] координаты тайлов дороги
    """
    
    # 1. Применяем алгоритм Брезенхема для прямой
    points = bresenham_line(start, end)
    path = list(points)
    
    # 2. Обход препятствий (упрощенный A*)
    avoider = AStar(heightmap)
    path = avoider.avoid_obstacles(path, start, end)
    
    return path


def bresenham_line(start, end):
    """Классический алгоритм Брезенхема для прямой"""
    x1, y1 = start
    x2, y2 = end
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    steep = dy > dx

    if steep:
        x1, y1 = y1, x1
        x2, y2 = y2, x2
    
    if x1 > x2:
        x1, x2 = x2, x1
        y1, y2 = y2, y1

    dx = x2 - x1
    dy = abs(y2 - y1)
    error = dx // 2
    y_step = 1 if y1 < y2 else -1
    
    start_y = min(start[1], end[1])
    end_y = max(start[1], end[1])

    y = y1
    for x in range(x1, x2 + 1):
        yield (y, x) if steep else (x, y)

        error -= dy
        if error < 0:
            y += y_step
            error += dx


def generate_roads(road, heightmap):
    path = build_road(road.start, road.end, heightmap)

    prev_point = None
    for point in path:
        if prev_point is not None:
            yield prev_point, point
        
        prev_point = point
