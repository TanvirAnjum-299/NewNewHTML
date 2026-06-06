import random
import pygame


class Button():
    def __init__(self,x,y,position,width,height):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.pos=position



    def clicked(self,pos):

        self.pos=pygame.mouse.get_pos()

        if self.pos[0]>self.x and self.pos[0]<self.x + self.width:
            if self.pos[1]>self.y and self.pos[1]<self.y + self.height:
                return True
            
            return False


class RpsGame():
    def __init__(self):
        pygame.init()

        self.bg=pygame.display.set_mode((960, 640))
        pygame.display.set_caption("RPS Smasher")

        self.bg=pygame.image.load("background.jpg")
        self.r_btn=pygame.image.load("r_button.png").convert_alpha()
        self.p_btn=pygame.image.load("p_button.png").convert_alpha()
        self.s_btn=pygame.image.load("s_button.png").convert_alpha()