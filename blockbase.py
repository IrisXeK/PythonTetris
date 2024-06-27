import pygame
from colors import Colors
from position import Position


class BlockBase:

    def __init__(self, id) -> None:
        self.id = id
        self.cells = {}
        self.cell_size = 30
        self.row_offset = 0
        self.col_offset = 0
        self.rotation_state = 0
        self.color = Colors.get_cell_colors()

    def get_cell_positions(self):  # 获取移动后的方块位置
        tiles = self.cells[self.rotation_state]
        moved_tiles = []  # 记录移动后方块的位置
        for position in tiles:
            position = Position(position.row + self.row_offset,
                                position.col + self.col_offset)
            moved_tiles.append(position)
        return moved_tiles

    def move(self, rows, cols):  # 将一个方块移动rows行cols列
        self.row_offset += rows
        self.col_offset += cols

    def rotate_clkwise(self):  # 顺时针旋转方块
        self.rotation_state += 1
        if self.rotation_state == len(self.cells):
            self.rotation_state = 0

    def rotate_anticlkwise(self):  # 逆时针旋转方块
        self.rotation_state -= 1
        if self.rotation_state == -1:
            self.rotation_state = len(self.cells) - 1

    def undo_clkwise_rotation(self):  # 旋转后越界 要转回来
        self.rotation_state -= 1
        if self.rotation_state == -1:
            self.rotation_state = len(self.cells) - 1

    def undo_anticlkwise_rotation(self):
        self.rotation_state += 1
        if self.rotation_state == len(self.cells):
            self.rotation_state = 0

    def draw(self, screen):
        tiles = self.get_cell_positions()
        for tile in tiles:
            tile_rect = pygame.Rect(tile.col * self.cell_size + 11,
                                    tile.row * self.cell_size + 11,
                                    self.cell_size - 1, self.cell_size - 1)
            pygame.draw.rect(screen, self.color[self.id], tile_rect)
