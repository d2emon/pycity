import math
import random
from collections import deque


class RoadData:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.is_correct = True

    @property
    def width(self):
        return self.end[0] - self.start[0]

    @property
    def height(self):
        return self.end[1] - self.start[1]

    @property
    def nodes(self):
        return [self.start, self.end]

    @property
    def line(self):
        # np.array([road[0], road[1]])
        return [self.start, self.end]

    @property
    def points(self):
        samples = 10

        dx = self.width / samples
        dy = self.height / samples
        for i in range(samples + 1):
            x = int(self.start[0] + dx * i)
            y = int(self.start[1] + dy * i)
            yield x, y

    @classmethod
    def build(cls, start, angle, length=10):
        """Вычисляем следующую точку"""
        end = [
            int(start[0] + length * math.cos(math.radians(angle))),
            int(start[1] + length * math.sin(math.radians(angle))),
        ]
        return cls(start, end)


class RoadFactory:
    max_road_height = 0.8

    def __init__(self, heightmap):
        self.heightmap = heightmap

    # Validators

    def is_valid_road(self, road):
        for pos in road.points:
            if self.heightmap.is_water(pos):
                return False

            if self.heightmap.get_value(pos) > self.max_road_height:
                return False

        return True

    # Road helpers

    def smooth_road(self, road):
        simplified = list(road.line)  # rdp(line, epsilon=2.0)  # Параметр "epsilon" контролирует уровень упрощения
        if len(simplified) > 1:
            return simplified

    @classmethod
    def road_weight(self, city1, city2):
        # city1 = np.argmin([np.linalg.norm(road[0] - p) for p in points])
        # city2 = np.argmin([np.linalg.norm(road[1] - p) for p in points])
        return city1.size + city2.size

    # L Roads

    # Левое ответвление
    @classmethod
    def left_branch(cls, pos, angle, steps):
        return (
            pos,
            angle - random.randint(30, 45),  # Угол поворота
            steps - 1
        )

    # Продолжаем текущую ветку
    @classmethod
    def right_branch(cls, pos, angle, steps):
        return (
            pos,
            angle + random.randint(30, 45),  # Небольшой изгиб
            steps - 1
        )

    # Правое ответвление
    @classmethod
    def current_branch(cls, pos, angle, steps):
        return (
            pos,
            angle + random.randint(-15, 15),
            steps - 1
        )

    def from_nodes(self, start, end):
        road = RoadData(start, end)
        road.is_correct = self.is_valid_road(road)
        return road

    def generate_l_roads(self, start_pos, start_angle, max_steps, branch_prob=0.3):
        """Генерирует дорогу с ответвлениями через L-систему."""
        
        min_length = 1
        max_length = 5

        # Инициализация
        stack = deque()
        stack.append((start_pos, start_angle, max_steps))
        
        while stack:
            pos, angle, steps = stack.pop()
            
            if steps <= 0:
                continue

            length = random.randint(min_length, max_length)
            road = RoadData.build(pos, angle, length)
            new_pos = road.end
            road.is_correct = self.is_valid_road(road)
            yield road
            
            # Решаем, создавать ли ветвление
            if random.random() < branch_prob and steps > 1:
                stack.append(self.left_branch(new_pos, angle, steps))
                stack.append(self.right_branch(new_pos, angle, steps))
            else:
                stack.append(self.current_branch(new_pos, angle, steps))

    def generate_from_centre(self, pos, max_steps, branch_prob=0.3):
        angle = random.randint(45, 360)
        while angle < 360:
            yield from self.generate_l_roads(pos, angle, max_steps, branch_prob)
            angle += random.randint(45, 360)
