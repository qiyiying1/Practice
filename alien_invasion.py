import pygame
from settings import Settings
from airplane import AirPlane
import game_functions as gf
def run_game():
# 初始化游戏并创建一个屏幕对象
    pygame.init()
#调用设置类，包含窗口长、宽和颜色
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
#设置窗口名称
    pygame.display.set_caption("QYY Invasion")
#创建一艘飞船
    airplane = AirPlane(ai_settings, screen)
# 开始游戏的主循环
    while True:
        #响应按键和鼠标事件
        gf.check_events(airplane)
        airplane.update()
        """更新屏幕上的图像，并切换到新屏幕"""
        # 每次循环时都重绘屏幕
        gf.update_screen(ai_settings, screen, airplane)
        airplane.blitme()
        # 刷新屏幕
        pygame.display.flip()
run_game()
