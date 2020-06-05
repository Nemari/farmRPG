
import pygame
from pygame import display, event, image, transform
import game_config as gc
import datetime
from button import *
from vegetables import *
currentColor = (255, 255, 255)
backgroundColor=(0,0,0)

class Clocks:
    def __init__(self, minutes, previous_time, seconds):
        self.minutes = minutes
        self.seconds = seconds
        self.previous_time = previous_time


def find_index(x, y):
        row = y // gc.IMAGE_SIZE
        col = x // gc.IMAGE_SIZE
        index = row * gc.NUM_TILES_SIDE + col
        return index


def find_row(y):
        row = y // gc.IMAGE_SIZE
        return row


def find_col(x):
        col = x // gc.IMAGE_SIZE
        return col


tomato_pic=image.load('tomato_seed.png')
tomato_pic=transform.scale(tomato_pic, (gc.IMAGE_SIZE-gc.MARGIN, gc.IMAGE_SIZE-gc.MARGIN) )


class FarmGame:
    def __init__(self, farm):
        pygame.init()
        self.farm=farm
        self.name=display.set_caption('FArM')
        self.screen=display.set_mode((384,512))
        self.soil=soil=image.load('SOIL.jpg')
        self.soil_new = transform.scale(soil, (gc.IMAGE_SIZE - gc.MARGIN, gc.IMAGE_SIZE - gc.MARGIN))
        self.tiles=[*farm.farm_tiles]
        self.panel={'shop': (0, 384),
                    'info': (256, 384),
                    'water': (128, 384),
                    'food': (128, 448)}
        self.clock=pygame.time.Clock()
        self.clocks=Clocks(0, datetime.datetime.now(), 0)
        self.player=Player('man', 'john')
        self.RAIN=pygame.USEREVENT
        self.ShopButton=ShopButton(0, 384, 'shop.png', self.screen, 'shop')
        self.InfoButton = ShopButton(256, 384, 'farmer.png', self.screen, 'farmer')
        self.WaterButton = ShopButton(128, 384, 'water.png', self.screen, 'farmer')
        self.shop=Shop(self.screen)
        self.products=[tomato, cucumber, carrot]
        self.bought_product=None
        self.water=False

    def draw(self, dict):
        for key in dict:
            self.screen.blit(self.soil_new, (key[0] * gc.IMAGE_SIZE, key[1] * gc.IMAGE_SIZE))
            if dict[key] is not None:
                if dict[key].state=='seed':
                    font = pygame.font.SysFont(None, 24)
                    text = font.render(str(dict[key].water) + '/10', True, currentColor)
                    temp_surface = pygame.Surface(text.get_size())
                    temp_surface.fill((192, 192, 192))
                    temp_surface.blit(text, (0, 0))
                    picture=image.load(dict[key].seed_image)
                    picture=transform.scale(picture, (gc.IMAGE_SIZE - gc.MARGIN, gc.IMAGE_SIZE - gc.MARGIN))
                    self.screen.blit(picture,(key[0]*gc.IMAGE_SIZE, key[1]*gc.IMAGE_SIZE))
                    self.screen.blit(temp_surface, (key[0] * gc.IMAGE_SIZE, key[1] * gc.IMAGE_SIZE))
                if dict[key].state == 'ripen':
                    #dict[key].state = 'ripen'
                    pic = image.load(dict[key].image)
                    pic = transform.scale(pic, (gc.IMAGE_SIZE - gc.MARGIN, gc.IMAGE_SIZE - gc.MARGIN))
                    self.screen.blit(pic, (key[0] * gc.IMAGE_SIZE, key[1] * gc.IMAGE_SIZE))
                elif dict[key].water > dict[key].water_needed:
                    dict[key].state = 'rotten'
                '''else:
                    tom_pic = image.load('tomato.png')
                    tom_pic = transform.scale(tom_pic, (gc.IMAGE_SIZE - gc.MARGIN, gc.IMAGE_SIZE - gc.MARGIN))
                    self.screen.blit(tom_pic, (key[0] * gc.IMAGE_SIZE, key[1] * gc.IMAGE_SIZE))
                    pygame.display.update()'''
        self.ShopButton.draw()
        self.InfoButton.draw()
        self.WaterButton.draw()


    def check_water(self, dict):
        for key in dict:
            if dict[key] is not None:
                if dict[key].water == dict[key].water_needed:
                    dict[key].state = 'ripen'
                    pic = image.load(dict[key].image)
                    pic = transform.scale(pic, (gc.IMAGE_SIZE - gc.MARGIN, gc.IMAGE_SIZE - gc.MARGIN))
                    self.screen.blit(pic, (key[0] * gc.IMAGE_SIZE, key[1] * gc.IMAGE_SIZE))
                    pygame.display.update()

    def run(self):
        run=True
        pygame.time.set_timer(self.RAIN, 10000)

        while run:
            if self.shop.state:
                i=0
                self.shop.draw()
                current_events = event.get()
                for prod in self.products:
                    font=pygame.font.SysFont(None, 24)
                    text=font.render(str(prod.price)+'$', True, currentColor)
                    picture=image.load(prod.image)
                    picture = transform.scale(picture, (gc.IMAGE_SIZE - gc.MARGIN, gc.IMAGE_SIZE - gc.MARGIN))
                    self.screen.blit(picture, (prod.place_in_menu[0] * gc.IMAGE_SIZE, prod.place_in_menu[1] * gc.IMAGE_SIZE))
                    self.screen.blit(text, (prod.place_in_menu[0] * gc.IMAGE_SIZE+50, prod.place_in_menu[1] * gc.IMAGE_SIZE+130))
                    i+=1
                    self.shop.products[i]=prod
                pygame.display.update()

                for e in current_events:
                    if e.type == pygame.QUIT:
                        run = False

                    if e.type == pygame.MOUSEBUTTONDOWN:
                        mouse_x, mouse_y = pygame.mouse.get_pos()
                        index = find_index(mouse_x, mouse_y)+1
                        if index in self.shop.products:
                            self.screen.fill(backgroundColor)
                            pygame.display.update()
                            self.bought_product=self.shop.products[index]
                            self.shop.state=False

            else:
                self.draw(self.farm.farm_tiles)
                elapsedTime = datetime.datetime.now() - self.clocks.previous_time
                x = divmod(elapsedTime.total_seconds(), 60)
                if int(x[1]) < 20:
                    pass
                else:
                    self.screen.blit(image.load('shop.png'), (128 * gc.IMAGE_SIZE, 128 * gc.IMAGE_SIZE))
                    print("works")
                    self.clocks.minutes += 1
                    self.clocks.previous_time = datetime.datetime.now()
                    self.clock.tick(60)
                    self.draw(self.farm.farm_tiles)
                    self.check_water(self.farm.farm_tiles)
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
                        if (row !=3) & bool(self.bought_product is not None):
                            name=self.bought_product.name+str(index)
                            veg=self.bought_product.garden_class(name)
                            print(name)
                            print(farm_test.farm_tiles)
                            self.player.plant(veg, self.farm, col, row)
                            self.screen.blit(self.soil_new, (col * gc.IMAGE_SIZE, row * gc.IMAGE_SIZE))
                            veggie_pic=image.load(self.bought_product.seed_image)
                            veggie_pic = transform.scale(veggie_pic,(gc.IMAGE_SIZE - gc.MARGIN, gc.IMAGE_SIZE - gc.MARGIN))
                            self.screen.blit(veggie_pic, (col * gc.IMAGE_SIZE, row * gc.IMAGE_SIZE))
                            #pygame.display.update()

                        elif (row !=3) & self.water:
                            if self.farm.farm_tiles[(col, row)] is not None:
                                self.farm.farm_tiles[(col, row)].water+=1
                                print(self.farm.farm_tiles[(col, row)].water)
                                self.draw(self.farm.farm_tiles)
                                pygame.display.update()
                        else:
                            if index==9:
                                self.shop.state=True
                            if index==10:
                                self.water=True
                            pass
                        print(col, self.farm.farm_tiles)

                    if e.type==pygame.USEREVENT:
                        tomato.water=10

                    if e.type == pygame.KEYDOWN:
                        if e.key == pygame.K_a:
                            self.bought_product=None

                    pass


