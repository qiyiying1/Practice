import sys
import pygame
def check_keydown_events(event, airplane):
    if event.key == pygame.K_RIGHT:
        airplane.moving_right = True
    elif event.key == pygame.K_LEFT:
        airplane.moving_left = True

def check_keyup_events(event, airplane):
    if event.key == pygame.K_RIGHT:
        airplane.moving_right = False
    elif event.key == pygame.K_LEFT:
        airplane.moving_left = False

def check_events(airplane):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, airplane)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, airplane)




def update_screen(ai_settings, screen, airplane):
    """更新屏幕上的图像，并切换到新屏幕"""
    # 每次循环时都重绘屏幕
    screen.fill(ai_settings.bg_color)
    airplane.blitme()
    pygame.display.flip()