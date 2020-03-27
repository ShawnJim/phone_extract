import os
import pygame
import itertools
import random

class ValidateUtil(object):

    #产生图片验证码的图像，保存在本地电脑
    def generate_picture(self):
        #pygame初始化
        pygame.init()
        #设置字体和字号
        font = pygame.font.SysFont('consolas', 64)
        #产生字母及数字列表，并重组，取其前四个作为图片验证码的文字
        chr_num_lst = list(itertools.chain([chr(ord('A')+_) for _ in range(26)],\
                                       [chr(ord('a')+_) for _ in range(26)],\
                                       [str(_) for _ in range(10)]))

        random.shuffle(chr_num_lst)
        self.val_text = chr_num_lst[0]+chr_num_lst[1]+chr_num_lst[2]+chr_num_lst[3]
        #渲染图片，设置背景颜色和字体样式,前面的颜色是字体颜色
        ftext = font.render(self.val_text, True, (0, 0, 255),(255,0,0))
        #保存图片
        pygame.image.save(ftext, r"%s/val.png"%os.getcwd())#图片保存地址