import pygame
import directions
from loaders.load_map import load_map


class BlockMap:
    def __init__(self, map_file, blocks, block_size, block_pos):
        self.x, self.y = block_pos
        self.block_size = block_size
        self.sprite_group = pygame.sprite.Group()

        data = load_map(map_file)
        data = list(data)
        self.blocks = list(blocks.fill(data))

    @property
    def start_x(self):
        if self.x > 0:
            return self.x - 1
        else:
            return 0

    @property
    def start_y(self):
        if self.y > 0:
            return self.y - 1
        else:
            return 0

    def update(self, *groups):
        self.sprite_group.empty()
        end_y = self.y + 1 if self.y < len(self.blocks) else len(self.blocks)
        for y, row in enumerate(self.blocks[self.start_y:end_y + 1]):
            end_x = self.x + 1 if self.x < len(row) else len(row)
            for x, block in enumerate(row[self.start_x:end_x + 1]):
                x_offset = x * self.block_size
                y_offset = y * self.block_size
                block.update(x_offset, y_offset, self.sprite_group, *groups)

    def move(self, direction):
        can_move = False
        if direction == directions.UP and self.y > 1:
            self.y -= 1
            can_move = True
        if direction == directions.DOWN and self.y < len(self.blocks) - 1:
            self.y += 1
            can_move = True
        if direction == directions.LEFT and self.x > 1:
            self.x -= 1
            can_move = True
        if direction == directions.RIGHT and self.x < len(self.blocks[self.y]) - 1:
            self.x += 1
            can_move = True

        if can_move:
            self.update()

        return can_move

    def check_pos(self, sprite):
        if sprite.rect.top < self.block_size:
            if self.move(directions.UP):
                sprite.rect.top += self.block_size
            else:
                sprite.rect = sprite.last_rect
        if sprite.rect.bottom > self.block_size * 2:
            if self.move(directions.DOWN):
                sprite.rect.top -= self.block_size
            else:
                sprite.rect = sprite.last_rect
        if sprite.rect.left < self.block_size:
            if self.move(directions.LEFT):
                sprite.rect.left += self.block_size
            else:
                sprite.rect = sprite.last_rect
        if sprite.rect.right > self.block_size * 2:
            if self.move(directions.RIGHT):
                sprite.rect.left -= self.block_size
            else:
                sprite.rect = sprite.last_rect
