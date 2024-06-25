import pygame
import sys
import grid
from blocks import *
BKGRD_COLOR = (44, 44, 127)

pygame.init()
screen = pygame.display.set_mode((300, 600))
pygame.display.set_caption("Tetris")

game_grid = grid.Grid()
clock = pygame.time.Clock()

block = BlockT()
while True:
    for event in pygame.event.get():  # 检查关闭事件
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(BKGRD_COLOR)  # 设置背景
    game_grid.draw(screen)  # 渲染画面
    block.draw(screen)
    pygame.display.update()  # 更新画面
    clock.tick(60)  # 一秒刷新60次
