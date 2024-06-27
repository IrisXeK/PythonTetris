import pygame
import sys
from colors import Colors
from game import Game

BKGRD_COLOR = Colors.dark_blue

pygame.init()

title_font = pygame.font.Font(None, 40)
game_over_font = pygame.font.Font(None, 80)

score_surface = title_font.render("Score", True, Colors.white)
next_block_surface = title_font.render(" Next\nBlock", True, Colors.white)
game_over_surface = title_font.render("GAME OVER", True, Colors.red)

score_rect = pygame.Rect(320, 55, 170, 60)
next_block_rect = pygame.Rect(320, 240, 170, 180)
screen = pygame.display.set_mode((500, 620))
pygame.display.set_caption("Tetris")

clock = pygame.time.Clock()
game = Game()

custom_update = pygame.USEREVENT
pygame.time.set_timer(custom_update, 300)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # 检查关闭事件
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:  # 检测方向键
            if event.key == pygame.K_r and game.game_over == True:  # game over时按r重置游戏
                game.game_over = False
                game.reset_game()
            if event.key == pygame.K_LEFT and game.game_over == False:
                game.move_cur_block_left()
            if event.key == pygame.K_RIGHT and game.game_over == False:
                game.move_cur_block_right()
            if event.key == pygame.K_DOWN and game.game_over == False:
                game.move_cur_block_down()
            if event.key == pygame.K_a and game.game_over == False:  # A键顺时针旋转
                game.rotate_cur_block_anticlkwise()
            if event.key == pygame.K_d and game.game_over == False:  # D键逆时针旋转
                game.rotate_cur_block_clkwise()
        if event.type == custom_update and game.game_over == False:  # 检查自定义时间 即方块的自动下行
            game.move_cur_block_down()

    screen.fill(BKGRD_COLOR)  # 设置背景
    # 渲染字体
    screen.blit(score_surface, (365, 20, 50, 50))
    screen.blit(next_block_surface, (375, 180, 50, 50))
    if game.game_over == True:
        screen.blit(game_over_surface, (320, 450, 50, 50))

    pygame.draw.rect(screen, Colors.light_blue, score_rect, 0, 10)
    pygame.draw.rect(screen, Colors.light_blue, next_block_rect, 0, 10)
    game.draw(screen)
    pygame.display.update()  # 更新画面
    clock.tick(60)  # 一秒刷新60次
