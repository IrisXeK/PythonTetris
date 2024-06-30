import sys
import pygame
from colors import Colors

title_font = pygame.font.Font(None, 70)


class StartScreen:
    def __init__(self, screen) -> None:
        screen.fill(Colors.cyan)
        self.instrction_text = title_font.render(
            "游戏说明", True, Colors.light_blue)
        self.game_instructions = ["左,右,下箭头将方块向对应方向移动一步",
                                  "A键逆时针旋转方块, D键顺时针旋转方块",
                                  "P键暂停游戏, R键重置游戏"]
        self.screen.blit(self.instrction_text, (screen.get_width() // 2 -
                                                self.instrction_text.get_width() // 2, 100))


# 初始化 Pygame
pygame.init()

# 设置屏幕大小
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("开始游戏示例")

# 颜色定义
black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 255)

# 字体设置
font = pygame.font.Font(None, 74)
small_font = pygame.font.Font(None, 36)

# 游戏状态
START, PLAYING, PAUSED = 0, 1, 2
game_state = START

# 按钮设置
button_rect = pygame.Rect(300, 400, 200, 50)
button_color = blue
button_text = small_font.render("开始游戏", True, white)

# 加载背景音乐
pygame.mixer.music.load("./Sounds/bgm.ogg")
pygame.mixer.music.play(-1)  # 循环播放背景音乐


def show_start_screen():
    screen.fill(black)
    title_text = font.render("游戏说明", True, white)
    instructions = [
        "使用箭头键移动",
        "按P键暂停",
        "按ESC键退出"
    ]
    screen.blit(title_text, (screen.get_width() //
                2 - title_text.get_width() // 2, 100))
    for i, line in enumerate(instructions):
        instruction_text = small_font.render(line, True, white)
        screen.blit(instruction_text, (screen.get_width() // 2 -
                    instruction_text.get_width() // 2, 200 + i * 40))
    pygame.draw.rect(screen, button_color, button_rect)
    screen.blit(button_text, (button_rect.x + (button_rect.width - button_text.get_width()) //
                2, button_rect.y + (button_rect.height - button_text.get_height()) // 2))


def game_loop():
    screen.fill(black)
    # 在这里添加游戏逻辑和绘图代码
    pygame.draw.circle(screen, white, (400, 300), 50)  # 示例：绘制一个白色圆圈


def pause_screen():
    screen.fill(black)
    pause_text = font.render("Paused", True, white)
    screen.blit(pause_text, (screen.get_width() // 2 - pause_text.get_width() //
                2, screen.get_height() // 2 - pause_text.get_height() // 2))


# 主循环
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if game_state == START and button_rect.collidepoint(event.pos):
                game_state = PLAYING
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_p:
                if game_state == PLAYING:
                    game_state = PAUSED
                    pygame.mixer.music.pause()  # 暂停音乐
                elif game_state == PAUSED:
                    game_state = PLAYING
                    pygame.mixer.music.unpause()  # 恢复音乐

    if game_state == START:
        show_start_screen()
    elif game_state == PLAYING:
        game_loop()
    elif game_state == PAUSED:
        pause_screen()

    # 刷新屏幕
    pygame.display.flip()

# 退出 Pygame
pygame.quit()
sys.exit()
