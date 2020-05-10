from abc import ABCMeta, abstractmethod, abstractproperty
import random
class Animal():
    def __init__(self, name, amount, product, action):
        self.name = name
        self.amount = amount        #amount of animals
        self.product = product      #product given by animal
        self.action = action        #action you can do with animal

    def info(self):
        print("{} is an animal. It is in the amount of {}. It gives you {}.You can {} it.".format(self.name, self.amount, self.product, self.action))


class Action():
    __metaclass__=ABCMeta
    
    @abstractmethod
    def feed(self):
        pass

    @abstractmethod
    def milk(self):
        pass

    @abstractmethod
    def pick_eggs(self):
        pass

    @abstractmethod
    def shear(self):
        pass

class Cow(Animal, Action):

    def __init__(self, name, amount, product, action, hunger, milk_amount):
        super().__init__(name, amount, product, action)
        self.hunger = hunger
        self.milk_amount = milk_amount

    def feed(self):
        self.hunger+=1
        print('Your cow is feed on {}'.format(self.hunger))

    def milk(self):
        self.milk_amount = random.randint(1, 10)
        print('Your cow gave you {} liters of milk!'.format(self.milk_amount))

class Chicken(Animal, Action):

    def __init__(self, name, amount, product, action, hunger, egg_amount):
        super().__init__(name, amount, product, action)
        self.hunger = hunger
        self.egg_amount = egg_amount

    def feed(self):
        self.hunger+=5
        print('Your chicken is feed on {}'.format(self.hunger))

    def pick_eggs(self):
        self.egg_amount = random.randint(1, 5)
        print('Your chicken gave you {} eggs!'.format(self.egg_amount))

class Sheep(Animal, Action):
    def __init__(self, name, amount, product, action, hunger, wool_amount):
        super().__init__(name, amount, product, action)
        self.hunger = hunger
        self.wool_amount = wool_amount

    def feed(self):
        self.hunger+=5
        print('Your sheep is feed on {}'.format(self.hunger))

    def shear(self):
        self.wool_amount = random.randint(10, 20)
        print('Your sheep gave you {} kilos of wool!'.format(self.wool_amount))

cow1= Cow('Cow', 1, 'milk', 'milk', 0, 0)
cow1.info()
cow1.feed()
cow1.milk()
chicken1 = Chicken('Chicken', 1, 'eggs', 'pick eggs from', 0, 0)
chicken1.info()
chicken1.feed()
chicken1.pick_eggs()
sheep1 = Sheep('Sheep', 1, 'wool', 'shear', 0,0)
sheep1.info()
sheep1.feed()
sheep1.shear()