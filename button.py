import pygame
from pygame import display, event, image, transform
import game_config as gc
from abc import ABC, abstractmethod
class Button(ABC):
    def __init__(self, left, top, pic, surface, name):
        self.name=name
        self.left=left
        self.top=top
        self.button=pygame.Rect(left, top, gc.IMAGE_SIZE, gc.IMAGE_SIZE)
        self.but_pic=image.load(pic)
        self.but_pic_new = transform.scale(self.but_pic, (gc.IMAGE_SIZE - gc.MARGIN, gc.IMAGE_SIZE - gc.MARGIN))
        self.surface=surface

    def draw(self):
        self.but_pic = transform.scale(self.but_pic, (gc.IMAGE_SIZE - gc.MARGIN, gc.IMAGE_SIZE - gc.MARGIN))
        self.surface.blit(self.but_pic, (self.left, self.top))
        pygame.display.update()

    @abstractmethod
    def button_func(self, *arg):
        pass

#class VegetableButton(Button):




class ShopButton(Button):
    def button_func(self, products_dict):
        product_name=[*products_dict]
        for name in product_name:
            pic=image.load(name+'.png')
            pic=transform.scale(pic, (gc.IMAGE_SIZE - gc.MARGIN, gc.IMAGE_SIZE - gc.MARGIN))






