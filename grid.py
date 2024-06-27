import pygame
from colors import Colors


class Grid:
    def __init__(self) -> None:
        self.num_rows = 20
        self.num_cols = 10
        self.cell_size = 30
        self.grid = [[0 for j in range(self.num_cols)]
                     for i in range(self.num_rows)]
        self.colors = Colors.get_cell_colors()

    def is_inside(self, row, col):  # 检测一个坐标为(row,col)的方块在不在网格里
        if row >= self.num_rows or row < 0 or col >= self.num_cols or col < 0:
            return False
        return True

    def is_empty(self, row, col):  # 检测一个坐标为(row,col)的格子是否为空(0)
        if self.grid[row][col] == 0:
            return True
        return False

    def reset(self):
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                self.grid[row][col] = 0

    def get_cell_color(self):
        dark_grey = (26, 31, 40)
        green = (47, 230, 23)
        red = (232, 18, 18)
        orange = (226, 116, 17)
        yellow = (237, 234, 4)
        cyan = (21, 204, 209)
        blue = (13, 64, 216)
        return [dark_grey, green, red, orange, yellow, cyan, blue]

    def is_row_full(self, row):  # 检测一行是否已满
        for col in range(self.num_cols):
            if self.grid[row][col] == 0:
                return False
        return True

    def clear_row(self, row):  # 一行满了之后清除这一行
        for col in range(self.num_cols):
            self.grid[row][col] = 0

    def move_row_down(self, row, num_rows):  # 清除一行后要把本行的方块移下来 清除了几行就往下移动几行
        # row : 本行  num_rows : 下面清除了几行
        for col in range(self.num_cols):
            self.grid[row + num_rows][col] = self.grid[row][col]
            self.grid[row][col] = 0

    def clear_full_rows(self):  # 检查每一行 看哪些行要清除
        num_to_clear = 0
        for row in range(self.num_rows - 1, 0, -1):  # 倒序遍历
            if self.is_row_full(row):
                self.clear_row(row)
                num_to_clear += 1
            elif num_to_clear > 0:
                self.move_row_down(row, num_to_clear)
        return num_to_clear

    def draw(self, screen):
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                cell_value = self.grid[row][col]
                cell_rect = pygame.Rect(col*self.cell_size + 11, row*self.cell_size + 11,
                                        self.cell_size - 1, self.cell_size - 1)
                pygame.draw.rect(screen, self.colors[cell_value], cell_rect)
