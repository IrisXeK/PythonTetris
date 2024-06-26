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

    def get_cell_color(self):
        dark_grey = (26, 31, 40)
        green = (47, 230, 23)
        red = (232, 18, 18)
        orange = (226, 116, 17)
        yellow = (237, 234, 4)
        cyan = (21, 204, 209)
        blue = (13, 64, 216)
        return [dark_grey, green, red, orange, yellow, cyan, blue]

    def draw(self, screen):
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                cell_value = self.grid[row][col]
                cell_rect = pygame.Rect(col*self.cell_size + 1, row*self.cell_size + 1,
                                        self.cell_size - 1, self.cell_size - 1)
                pygame.draw.rect(screen, self.colors[cell_value], cell_rect)
