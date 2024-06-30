import random
import pygame
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
        self.game_over = False
        self.game_pause = False
        self.score = 0
        self.rotate_sound_efct = pygame.mixer.Sound("./Sounds/rotate.ogg")
        self.clear_sound_efct = pygame.mixer.Sound("./Sounds/clear.ogg")
        self.game_over_sound_efct = pygame.mixer.Sound(
            "./Sounds/game_over.wav")
        pygame.mixer.music.load("./Sounds/bgm.ogg")
        pygame.mixer.music.play(-1)

    def update_score(self, lines_cleared, mv_down_pts):
        """
        清除一行100分 两行300分 三行及以上500分
        向下移动一次方块加1分
        """
        if lines_cleared == 1:
            self.score += 100
        elif lines_cleared == 2:
            self.score += 300
        elif lines_cleared >= 3:
            self.score += 500
        self.score += mv_down_pts

    def move_cur_block_left(self):
        self.current_block.move(0, -1)
        if not self.is_in_grid() or not self.is_block_fit():  # 移动后不在范围内 就移动回去
            self.current_block.move(0, 1)

    def move_cur_block_right(self):
        self.current_block.move(0, 1)
        if not self.is_in_grid() or not self.is_block_fit():
            self.current_block.move(0, -1)

    def move_cur_block_down(self):
        self.current_block.move(1, 0)
        if not self.is_in_grid() or not self.is_block_fit():  # 下移后方块到底或者碰到其他方块，先移回来 再锁定
            self.current_block.move(-1, 0)
            self.lock_block()

    def lock_block(self):
        tiles = self.current_block.get_cell_positions()
        for position in tiles:
            self.grid.grid[position.row][position.col] = self.current_block.id
        self.current_block = self.next_block
        self.next_block = self.get_random_block()
        rows_cleared = self.grid.clear_full_rows()
        if rows_cleared > 0:
            self.clear_sound_efct.play()
        self.update_score(rows_cleared, 0)
        if self.is_block_fit() == False:  # 新生成的方块不能fit时 即game over
            pygame.mixer.music.pause()
            self.game_over_sound_efct.play()
            self.game_over = True

    def reset_game(self):
        self.grid.reset()
        self.blocks = [BlockI(), BlockJ(), BlockL(), BlockO(),
                       BlockT(), BlockZ(), BlockS()]
        self.current_block = self.get_random_block()
        self.next_block = self.get_random_block()
        self.score = 0
        pygame.mixer.music.play(-1)

    def is_in_grid(self):  # 检测一个方块在移动或旋转后是否超出边界
        tiles = self.current_block.get_cell_positions()
        for tile in tiles:
            if not self.grid.is_inside(tile.row, tile.col):
                return False
        return True

    def is_block_fit(self):  # 防止方块覆盖
        tiles = self.current_block.get_cell_positions()
        for position in tiles:
            if not self.grid.is_empty(position.row, position.col):
                return False
        return True

    def rotate_cur_block_clkwise(self):
        self.current_block.rotate_clkwise()
        self.rotate_sound_efct.play()
        if not self.is_in_grid():
            self.current_block.undo_clkwise_rotation()

    def rotate_cur_block_anticlkwise(self):
        self.current_block.rotate_anticlkwise()
        self.rotate_sound_efct.play()
        if not self.is_in_grid():
            self.current_block.undo_anticlkwise_rotation()

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
        self.current_block.draw(screen, 11, 11)
        if self.next_block.id == 3:  # I 方块
            self.next_block.draw(screen, 290, 257)
        elif self.next_block.id == 1:  # L 方块
            self.next_block.draw(screen, 285, 360)
        elif self.next_block.id == 4:  # O 方块
            self.next_block.draw(screen, 285, 255)
        else:
            self.next_block.draw(screen, 270, 270)
