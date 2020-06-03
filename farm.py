import pygame
from pygame import display, event, image, transform
import game_config as gc
from vegetables import farm_test, adriana, tomato
import threading

def find_index(x,y):
    row=y//gc.IMAGE_SIZE
    col=x//gc.IMAGE_SIZE
    index=row*gc.NUM_TILES_SIDE+col
    return index

def find_row(y):
    row=y//gc.IMAGE_SIZE
    return row

def find_col(x):
    col=x//gc.IMAGE_SIZE
    return col

class Clocks:
    def init(self, days, previous_time, hours):
        self.hours = hours
        self.days = days
        self.previous_time = previous_time

pygame.init()
display.set_caption('farm')
screen=display.set_mode((384,384))
tiles=[*farm_test.farm_tiles]
print(tiles)

def change_pic(pic):
    new_pic = image.load(pic)
    new_pic = transform.scale(new_pic, (gc.IMAGE_SIZE - gc.MARGIN, gc.IMAGE_SIZE - gc.MARGIN))
    screen.blit(new_pic, (col * gc.IMAGE_SIZE, row * gc.IMAGE_SIZE))


running=True
soil=image.load('SOIL.jpg')
tomato_pic=image.load('tomato_seed.png')
tomato_pic=transform.scale(tomato_pic, (gc.IMAGE_SIZE-gc.MARGIN, gc.IMAGE_SIZE-gc.MARGIN) )
soil=transform.scale(soil, (gc.IMAGE_SIZE-gc.MARGIN, gc.IMAGE_SIZE-gc.MARGIN) )
for i in tiles:
    screen.blit(soil, (i[0] * gc.IMAGE_SIZE, i[1] * gc.IMAGE_SIZE))
counter=10
pygame.time.set_timer(pygame.USEREVENT, 1000)
while running:
    current_events=event.get()
    for e in current_events:

        if e.type==pygame.QUIT:
            running=False

        if e.type==pygame.MOUSEBUTTONDOWN :
            mouse_x, mouse_y=pygame.mouse.get_pos()
            index=find_index(mouse_x, mouse_y)
            row=find_row(mouse_y)
            col=find_col(mouse_x)
            print(col, row)
            adriana.plant(tomato, farm_test, col, row)
            screen.blit(tomato_pic, (col*gc.IMAGE_SIZE, row*gc.IMAGE_SIZE))
            timer=threading.Timer(5.0, change_pic, ['tomato5.png'])
            timer.start()
            print(index)



    display.flip()