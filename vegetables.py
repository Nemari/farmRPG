from abc import ABC
import pygame
import game_config as gc

class Shop:
    def __init__(self, screen):
        self.products={}
        self.screen=screen
        self.state=False

    def draw(self):
        surf=pygame.Surface((384, 512))
        self.screen.blit(surf, (0,0))
        #for prod in [*self.products]:



class Action(ABC):
    def plant(self, farm_obj):
        pass

    def ripen_timer(self, time1, time2):
        pass

class GardenVagetables:
    def __init__(self, type, product, price, water_needed):
        self.type=type
        self.water = 5
        self.product = product
        self.state = 'seed'
        self.image = "assets\{}.png".format(self.type)
        self.sell_price=price
        self.water_needed=water_needed
        self.seed_image = "assets\{}_seed.png".format(self.type)

class Tomatos(GardenVagetables):
    def __init__(self,name):
        super().__init__('tomato', 1, 20, 10)
        self.name=name

class Cucumbers(GardenVagetables):
    def __init__(self, name):
        super().__init__('cucumber', 1, 25, 12)
        self.name=name

class Carrots(GardenVagetables):
    def __init__(self):
        super().__init__('carrot', 1, 30, 13)

tomato1=Tomatos('tomato')
print(tomato1.type)

class ShopVegetable(Action):
    def __init__(self, name,price,x,y , garden_class):
        self.name=name
        self.garden_class=garden_class
        self.price=price
        self.place_in_menu=(x,y)
        self.image="assets\{}.png".format(self.name)
        self.seed_image="assets\{}_seed.png".format(self.name)

    '''def water_plant(self, litreage):
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
        pygame.time.set_timer(self.event2(), int(time2))'''



class Player:
    def __init__(self, gender, name):
        self.players_vegetables = {}
        self.players_animals = {}
        self.players_products = {}
        self.gender=gender
        self.name=name
        self.money=0

    def plant(self, farm_obj, farm, x, y):
        if bool((x,y) in farm.farm_tiles) & bool(farm.farm_tiles[(x,y)] is None):
            farm.farm_tiles[(x,y)]=farm_obj
        else:
            pass

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
        self.obj=farm_obj

adriana=Player('woman', 'adriana')
tomato=ShopVegetable('tomato',15, 0,0, Tomatos)
cucumber=ShopVegetable('cucumber', 20, 1, 0, Cucumbers)
print(adriana.money)
farm_test=FarmField(3)
for i in range(0, 3):
    for j in range(0,3):
        farm_test.farm_tiles[i,j]=None
print(farm_test.farm_tiles)

products=[tomato, cucumber]
carrot=ShopVegetable('carrot', 10, 2,0, Carrots)
carrot1=carrot.garden_class()
print(carrot1.type)