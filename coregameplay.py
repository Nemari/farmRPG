import pygame
import time
import random
from pygame import display, event, image, transform
import game_config as gc
import threading
from animals import Cow, Sheep, Animal, Action,  GameObject
from player import maria

pygame.init()

display_width = 800
display_height = 600

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 100, 0)
green = (0, 255, 100)

block_color = (53, 115, 255)


gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('FARM FAM')
clock = pygame.time.Clock()

menuImg = pygame.image.load('assets\menu.jpg')

def things_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Dodged: " + str(count), True, black)
    gameDisplay.blit(text, (0, 0))


def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width / 2), (display_height / 2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(2)

    game_loop()


def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))

        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))

    smallText = pygame.font.SysFont("bitstreamverasans",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)


def game_intro():
    intro = True

    while intro:
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.blit(menuImg, (0,0))
        largeText = pygame.font.SysFont("bitstreamverasans", 115)
        TextSurf, TextRect = text_objects("FAM FARM", largeText)
        TextRect.center = ((display_width / 2), (display_height / 2))
        gameDisplay.blit(TextSurf, TextRect)

        button("GO!", 150, 450, 100, 50, green, green, game_loop)
        button("Quit", 550, 450, 100, 50, red, red, gamequit)

        pygame.display.update()
        clock.tick(15)


def game_loop():
    class FarmField():
        def __init__(self, num):
            self.farm_tiles = {}
            self.size = str(num) + 'x' + str(num)
            '''for i in range(0, num**2):
                self.farm_tiles[i]=None'''

    farm_test = FarmField(3)
    for i in range(0, 3):
        for j in range(0, 3):
            farm_test.farm_tiles[i, j] = None

    def find_index(x, y):
        row = y // gc.IMAGE_SIZE
        col = x // gc.IMAGE_SIZE
        index = row * gc.NUM_TILES_SIDE + col
        return index

    def pic_load(gameobject):
        picture = pygame.image.load(gameobject.picture)
        picture = pygame.transform.scale(picture, (gc.IMAGE_SIZE - gc.MARGIN, gc.IMAGE_SIZE - gc.MARGIN))
        return picture

    def find_row(y):
        row = y // gc.IMAGE_SIZE
        return row

    def find_col(x):
        col = x // gc.IMAGE_SIZE
        return col

    class Clocks:
        def init(self, days, previous_time, hours):
            self.hours = hours
            self.days = days
            self.previous_time = previous_time

    pygame.init()
    display.set_caption('fam farm')
    screen = display.set_mode((384, 384))
    tiles = [*farm_test.farm_tiles]
    print(tiles)

    def change_pic(pic):
        new_pic = image.load(pic)
        new_pic = transform.scale(new_pic, (gc.IMAGE_SIZE - gc.MARGIN, gc.IMAGE_SIZE - gc.MARGIN))
        screen.blit(new_pic, (col * gc.IMAGE_SIZE, row * gc.IMAGE_SIZE))

    def stall(farm_obj, farm, x, y):  # set an animal to a place
        farm.farm_tiles[(x, y)] = farm_obj

    def choose(farm, x, y):
        return farm.farm_tiles[(x, y)]

    def draw_go(player, obj):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        index = find_index(mouse_x, mouse_y)
        row = find_row(mouse_y)
        col = find_col(mouse_x)
        player.stall(obj, farm_test, col, row)
        screen.blit(pic_load(obj), (col * gc.IMAGE_SIZE, row * gc.IMAGE_SIZE))

    class Shop():
        def __init__(self, player):
            self.player = player

        def buy_sheep(self):
            sheep = Sheep()
            return sheep

        def buy_cow(self):
            cow = Cow()
            return cow

        def shopping(self, event):
            if event.key == pygame.K_w:
                return shop.buy_cow()
            elif event.key == pygame.K_a:
                return shop.buy_sheep()

    act = Action()
    animal = Animal()
    shop = Shop(maria)
    running = True
    grass = pygame.image.load('assets\grass.jpg')
    # cow_pic=pygame.image.load('assets\cow.png')
    # cow_pic=pygame.transform.scale(cow_pic, (gc.IMAGE_SIZE-gc.MARGIN, gc.IMAGE_SIZE-gc.MARGIN))
    grass = transform.scale(grass, (gc.IMAGE_SIZE - gc.MARGIN, gc.IMAGE_SIZE - gc.MARGIN))
    for i in tiles:
        screen.blit(grass, (i[0] * gc.IMAGE_SIZE, i[1] * gc.IMAGE_SIZE))
    counter = 10
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Usually wise to be able to close your program.
                raise SystemExit
            if event.type == pygame.KEYDOWN:
                animal = shop.shopping(event)
            animal_l = Animal()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                index = find_index(mouse_x, mouse_y)
                row = find_row(mouse_y)
                col = find_col(mouse_x)
                if animal is not None:
                    maria.stall(animal, farm_test, col, row)
                    screen.blit(pic_load(animal), (col * gc.IMAGE_SIZE, row * gc.IMAGE_SIZE))

                animal_l = choose(farm_test, row, col)

            if animal_l is not None:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s:
                        act.feed(animal_l)
                    elif event.key == pygame.K_d:
                        act.get_product(animal_l)

                # elif animal is not None:
                #     maria.stall(animal, farm_test, col, row)
                #     screen.blit(pic_load(animal), (col * gc.IMAGE_SIZE, row * gc.IMAGE_SIZE))
                #     continue
                # else:
                #     continue

                # if animal.state == 'sleep':
                #     timer = threading.Timer(5.0, change_pic, ['assets\cow_sleep.png'])
                #     timer.start()

        display.flip()

def gamequit():
    pygame.quit()

game_intro()
game_loop()
pygame.quit()