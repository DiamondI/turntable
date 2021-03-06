import pygame
from pygame.locals import *
import sys
from draw_pie_chart import draw_pie_chart
import math
import random
 
pygame.init()  # 初始化pygame类
screen = pygame.display.set_mode((640, 480))  # 设置窗口大小
pygame.display.set_caption('幸运大转盘')  # 设置窗口标题
tick = pygame.time.Clock()
fps = 10  # 设置刷新率，数字越大刷新率越高

# 画背景图片
draw_pie_chart()

# 加载背景图片
bg_picture = pygame.transform.scale(pygame.image.load("images/pie.png"), (640, 480))
bg = bg_picture.convert()

# pointer_picture = pygame.transform.scale(pygame.image.load("images/pointer.png"), (24, 87))
# pointer = pointer_picture.convert()
pointer = pygame.image.load("images/pointer.png")

angle = 0

center_x, center_y = 320, 240
radius = 100

angles = random.randint(1800, 2160)

velocity = 100
level_num = 5
velocity_step = velocity / level_num
interval = angles / level_num


start = False
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == K_SPACE:
                start = True

    posx = center_x + int(radius * math.sin(angle * math.pi / 180))
    posy = center_y - int(radius * math.cos(angle * math.pi / 180))

    screen.fill((255, 255, 255))  # 设置背景为白色
    screen.blit(bg, (0, 0))
    new_pointer = pygame.transform.rotate(pointer, -angle)
    newRect = new_pointer.get_rect(center = (posx, posy))

    if start:
        if angle <= angles:
            angle += velocity - velocity_step * (angle // interval)
        else:
            # 一轮转盘结束，重置 angle, angles, start
            angle = angle % 360
            angles = random.randint(1800, 2160)
            interval = angles / level_num
            start = False
    
    screen.blit(new_pointer, newRect)
 
    tick.tick(fps)
    pygame.display.flip()  # 刷新窗口