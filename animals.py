from abc import ABCMeta, abstractmethod, abstractproperty
import random
import pygame
import game_config as gc
class Product():

    def __init__(self, name, price, dim):
        self.name = name
        self.price = price
        self.amount = 0
        self.dim = dim

class Milk(Product):
    def __init__(self):
        super().__init__(name = "Milk", price = 7, dim = "litres")



class Egg(Product):
    def __init__(self):
        super().__init__(name="Egg", price=5, dim = "")


class Wool(Product):
    def __init__(self):
        super().__init__(name="Wool", price=10, dim = "kilos")


class Animal():
    def __init__(self, name, action, product, price):
        self.name = name
        self.action = action        #action you can do with animal
        self.price = price
        self.state = 'set'
        self.ripen = pygame.USEREVENT + 1
        self.hunger = 0
        self.product = Product(product.name, product.price, product.dim)
    def info(self):
        print("{} is an animal. It is in the amount of {}. It gives you {}.You can {} it.".format(self.name, self.amount, self.product, self.action))
    def event1(self):
        self.state='ready'

    def event2(self):
        self.state='sleep'

    def getting_ready(self, time1, time2):
        pygame.time.set_timer(self.event1(), int(time1))
        pygame.time.set_timer(self.event2(), int(time2))

    def buy_animal(self, player):
        if (player.money>=self.price):
            if (self.name in player.players_animals):
                player.players_animals[self.name]+=1
            else:
                player.players_animals[self.name]=1
            player.money-=self.price
            print("You bought {}".format(self.name))
        else:
            print("You don't have enough money")
    def get_product(self):
        self.product.amount = random.randint(1, 10)
        return self.product.amount

class Action():

    def feed(self, animal):
        animal.hunger += 1
        print('Your {} is feed on {}'.format(animal.name, animal.hunger))

    def get_product(self, animal):
        animal.state = 'sleep'
        print('Your {} gave you {} {} of {}!'.format(animal.name, animal.get_product(), animal.product.dim, animal.product.name))
        return animal.product


class Cow(Animal):
    def __init__(self):
        super().__init__(name="Cow", action="milk", price=10, product = Milk())

class Chicken(Animal):
    def __init__(self):
        super().__init__(name="Chicken", action="pick_eggs", price=3, product =Egg())

class Sheep(Animal):
    def __init__(self):
        super().__init__(name="Sheep", action="shear", price=5, product = Wool())


