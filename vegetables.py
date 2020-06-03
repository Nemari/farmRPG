from abc import ABC
import pygame
import game_config as gc

class Action(ABC):
    def plant(self, farm_obj):
        pass

    def ripen_timer(self, time1, time2):
        pass

class Vegetable(Action):
    def __init__(self, name,price):
        self.name=name
        self.water = 5
        self.product = 0
        self.price=price
        self.state='seed'
        self.ripen=pygame.USEREVENT+1
    def water_plant(self, litreage):
        if (litreage==1):
            self.water+=1
        if (litreage==3):
            self.water+=3
        if (litreage==5):
            self.water+=5
        print("You watered your {}. Current water level:{}".format(self.name, self.water))

    def buy_vegetable(self, player):
        if (player.money>=self.price):
            if (self.name in player.players_vegetables):
                player.players_vegetables[self.name]+=1
            else:
                player.players_vegetables[self.name]=1
            player.money-=self.price
            print("You bought {}".format(self.name))
        else:
            print("You don't have enough money")

    def event1(self):
        self.state='ripened'

    def event2(self):
        self.state='rotten'

    def ripen(self, time1, time2):
        pygame.time.set_timer(self.event1(), int(time1))
        pygame.time.set_timer(self.event2(), int(time2))



class Player:
    def __init__(self, gender, name):
        self.players_vegetables = {}
        self.players_animals = {}
        self.players_products = {}
        self.gender=gender
        self.name=name
        self.money=0

    def plant(self, farm_obj, farm, x, y):
        farm.farm_tiles[(x,y)]=farm_obj.name

class FarmField():
    def __init__(self, num):
        self.farm_tiles = {}
        self.size=str(num)+'x'+str(num)
        '''for i in range(0, num**2):
            self.farm_tiles[i]=None'''

class FarmTile(Action):
    def __init__(self, x, y):
        self.x=0
        self.y=0
        self.index=x*gc.NUM_TILES_SIDE+y
        self.obj=None

    def plant(self, farm_obj):
        self.obj=farm_obj.name

adriana=Player('woman', 'adriana')
tomato=Vegetable('tomato',15)
tomato.water_plant(3)
tomato.buy_vegetable(adriana)
print(adriana.money)
farm_test=FarmField(3)
for i in range(0, 3):
    for j in range(0,3):
        farm_test.farm_tiles[i,j]=None
print(farm_test.farm_tiles)


