import pygame
import sys
import time
from colors import Colors
from game import Game

BKGRD_COLOR = Colors.dark_blue
START_SCREEN = True
GAME_SCREEN = False
CHS_FONT_PATH = "./ChineseFont/msyh.ttc"


pygame.init()

game_over_font = pygame.font.Font(None, 80)
chs_font = pygame.font.Font(CHS_FONT_PATH, 25)
chs_font_small = pygame.font.Font(CHS_FONT_PATH, 20)

# render将字体渲染为可显示的图片
score_surface = chs_font.render("   分数", True, Colors.white)
next_block_surface = chs_font.render(" 下个方块", True, Colors.white)
game_over_surface = chs_font.render("     游戏结束", True, Colors.red)
instruction_text = chs_font.render("游戏说明", True, Colors.red)
game_instructions = ["左,右,下箭头将方块向对应方向移动一步",
                     "A键逆时针旋转方块, D键顺时针旋转方块",
                     "P键暂停游戏, R键重置游戏"]

screen = pygame.display.set_mode((500, 620))
start_screen_img = pygame.image.load("./BkgrdImgs/Sky.jpg")
start_screen_img = pygame.transform.scale(start_screen_img, (500, 620))
game_start_button = pygame.Rect(220, 270, 170, 180)
start_button_surface = pygame.Surface((150, 75), pygame.SRCALPHA)
start_button_surface.fill((*Colors.cyan, 128))  # 设置 alpha 值为128，实现半透明效果

pygame.display.set_caption("Tetris")
clock = pygame.time.Clock()

while START_SCREEN:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # 检查关闭事件
            START_SCREEN, GAME_SCREEN = False, True
    screen.blit(start_screen_img, (0, 0))
    screen.blit(instruction_text, (190, 160, 170, 180))
    for idx, line in enumerate(game_instructions):
        instruction_text = chs_font_small.render(line, True, Colors.red)
        screen.blit(instruction_text, (screen.get_width() // 2 -
                    instruction_text.get_width() // 2, 200 + idx * 40))
    screen.blit(start_button_surface, (170, 380))
    pygame.display.flip()
    clock.tick(60)

score_rect = pygame.Rect(320, 55, 170, 60)
next_block_rect = pygame.Rect(320, 240, 170, 180)
game = Game()

custom_update = pygame.USEREVENT
pygame.time.set_timer(custom_update, 150)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # 检查关闭事件
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:  # 检测键盘活动
            if event.key == pygame.K_r:  # 按r重置游戏
                game.game_over = False
                game.reset_game()
            if event.key == pygame.K_p and game.game_over == False:
                if game.game_pause:
                    pygame.mixer.music.unpause()
                else:
                    pygame.mixer.music.pause()
                game.game_pause = not game.game_pause
            if event.key == pygame.K_LEFT and game.game_over == False:
                game.move_cur_block_left()
            if event.key == pygame.K_RIGHT and game.game_over == False:
                game.move_cur_block_right()
            if event.key == pygame.K_DOWN and game.game_over == False:
                game.move_cur_block_down()
                game.update_score(0, 1)
            if event.key == pygame.K_a and game.game_over == False:  # A键顺时针旋转
                game.rotate_cur_block_anticlkwise()
            if event.key == pygame.K_d and game.game_over == False:  # D键逆时针旋转
                game.rotate_cur_block_clkwise()
        if event.type == custom_update and game.game_over == False and not game.game_pause:  # 检查自定义时间 即方块的自动下行
            game.move_cur_block_down()

    if not game.game_pause:
        screen.fill(BKGRD_COLOR)  # 设置背景
        score_value_surface = chs_font.render(
            str(game.score), True, Colors.cyan)  # 分数是动态变化的而非静态字体 要在游戏循环内部实时渲染
        screen.blit(score_surface, (365, 20, 50, 50))  # 在screen显示"分数"
        screen.blit(next_block_surface, (345, 190, 50, 50))  # 在screen显示"下一个方块"
        screen.blit(score_value_surface, score_value_surface.get_rect(
            centerx=score_rect.centerx, centery=score_rect.centery))  # 显示分数数值
        if game.game_over == True:
            screen.blit(game_over_surface, (320, 450, 50, 50))  # 显示游戏结束字体
        pygame.draw.rect(screen, Colors.light_blue,
                         score_rect, 0, border_radius=10)  # 分数方框
        pygame.draw.rect(screen, Colors.light_blue,
                         next_block_rect, 0, border_radius=10)  # 下一个方块方框
        game.draw(screen)
        pygame.display.update()  # 更新画面
        clock.tick(60)  # 一秒刷新60次
