
import pygame
from pygame import display, event, image, transform
import game_config as gc
import datetime
from button import *
from vegetables import farm_test, adriana, tomato, Player
class Clocks:
    def __init__(self, minutes, previous_time, seconds):
        self.minutes = minutes
        self.seconds = seconds
        self.previous_time = previous_time


def find_index( x, y):
        row = y // gc.IMAGE_SIZE
        col = x // gc.IMAGE_SIZE
        index = row * gc.NUM_TILES_SIDE + col
        return index

def find_row( y):
        row = y // gc.IMAGE_SIZE
        return row

def find_col(x):
        col = x // gc.IMAGE_SIZE
        return col

tomato_pic=image.load('tomato_seed.png')
tomato_pic=transform.scale(tomato_pic, (gc.IMAGE_SIZE-gc.MARGIN, gc.IMAGE_SIZE-gc.MARGIN) )


class FarmGame():
    def __init__(self, farm):
        pygame.init()
        self.farm=farm
        self.name=display.set_caption('FArM')
        self.screen=display.set_mode((384,512))
        self.soil=soil=image.load('SOIL.jpg')
        self.soil_new = transform.scale(soil, (gc.IMAGE_SIZE - gc.MARGIN, gc.IMAGE_SIZE - gc.MARGIN))
        self.tiles=[*farm.farm_tiles]
        self.clock=pygame.time.Clock()
        self.clocks=Clocks(0, datetime.datetime.now(), 0)
        self.player=Player('man', 'john')
        self.RAIN=pygame.USEREVENT


    def draw(self, x1, x2):
        self.screen.blit(self.soil_new, (x1 * gc.IMAGE_SIZE, x2 * gc.IMAGE_SIZE))
        pygame.display.update()

    def change_pic(self, pic, col, row):
        new_pic = image.load(pic)
        new_pic = transform.scale(new_pic, (gc.IMAGE_SIZE - gc.MARGIN, gc.IMAGE_SIZE - gc.MARGIN))
        self.screen.blit(new_pic, (col * gc.IMAGE_SIZE, row * gc.IMAGE_SIZE))

    def run(self):
        run=True
        pygame.time.set_timer(self.RAIN, 10000)

        while run:
            elapsedTime = datetime.datetime.now() - self.clocks.previous_time
            x = divmod(elapsedTime.total_seconds(), 60)
            if int(x[1]) < 20:
                pass
            else:
                print("works")
                self.clocks.minutes += 1
                self.clocks.previous_time = datetime.datetime.now()
                self.clock.tick(60)
                for key in self.farm.farm_tiles:
                    if self.farm.farm_tiles[key] is None:
                        self.draw(key[0], key[1])
                    if self.farm.farm_tiles[key]=='tomato':
                        if tomato.water==10:
                            tom_pic = image.load('tomato.png')
                            tom_pic = transform.scale(tom_pic,(gc.IMAGE_SIZE - gc.MARGIN, gc.IMAGE_SIZE - gc.MARGIN))
                            self.screen.blit(tom_pic, (key[0] * gc.IMAGE_SIZE, key[1] * gc.IMAGE_SIZE))
                            pygame.display.update()

            for key in self.farm.farm_tiles:
                if self.farm.farm_tiles[key] is None:
                    self.draw(key[0], key[1])
            self.clock.tick(60)
            current_events = event.get()
            for e in current_events:
                if e.type == pygame.QUIT:
                    run = False
                if e.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    index = find_index(mouse_x, mouse_y)
                    row = find_row(mouse_y)
                    col = find_col(mouse_x)
                    self.player.plant(tomato, self.farm, col, row )
                    self.screen.blit(tomato_pic, (col * gc.IMAGE_SIZE, row * gc.IMAGE_SIZE))
                    pygame.display.update()
                    print(index, self.farm.farm_tiles)

                if e.type==pygame.USEREVENT:
                    tomato.water=10

