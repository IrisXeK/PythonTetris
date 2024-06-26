import random
from grid import Grid
from blocks import *
# 创建game类游戏容器以便之后的维护


class Game:
    def __init__(self) -> None:
        self.grid = Grid()
        self.blocks = [BlockI(), BlockJ(), BlockL(), BlockO(),
                       BlockT(), BlockZ(), BlockS()]
        self.current_block = self.get_random_block()
        self.next_block = self.get_random_block()

    def move_cur_block_left(self):
        self.current_block.move(0, -1)
        if not self.is_in_grid():  # 移动后不在范围内 就移动回去
            self.current_block.move(0, 1)

    def move_cur_block_right(self):
        self.current_block.move(0, 1)
        if not self.is_in_grid():
            self.current_block.move(0, -1)

    def move_cur_block_down(self):
        self.current_block.move(1, 0)
        if not self.is_in_grid():
            self.current_block.move(-1, 0)

    def is_in_grid(self):  # 检测一个方块在移动后是否超出边界
        tiles = self.current_block.get_cell_positions()
        for tile in tiles:
            if not self.grid.is_inside(tile.row, tile.col):
                return False
        return True

    def get_random_block(self):
        if len(self.blocks) == 0:
            self.blocks = [BlockI(), BlockJ(), BlockL(), BlockO(),
                           BlockT(), BlockZ(), BlockS()]
        # 每个方块都要出现至少一次 所以不直接进行随机选择
        block = random.choice(self.blocks)
        self.blocks.remove(block)
        return block

    def draw(self, screen):
        self.grid.draw(screen)
        self.current_block.draw(screen)
