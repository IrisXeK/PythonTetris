import pygame
import sys
from game import Game

BKGRD_COLOR = (44, 44, 127)

pygame.init()
screen = pygame.display.set_mode((300, 600))
pygame.display.set_caption("Tetris")

clock = pygame.time.Clock()
game = Game()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # 检查关闭事件
            pygame.quit()
            sys.exit()
        # 检测方向键
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                game.move_cur_block_left()
            if event.key == pygame.K_RIGHT:
                game.move_cur_block_right()
            if event.key == pygame.K_DOWN:
                game.move_cur_block_down()

    screen.fill(BKGRD_COLOR)  # 设置背景
    game.draw(screen)
    pygame.display.update()  # 更新画面
    clock.tick(60)  # 一秒刷新60次
