from abc import ABC
class Vegetable:
    def __init__(self, name,price):
        self.name=name
        self.water = 5
        self.product = 0
        self.price=price
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

class Player:
    players_vegetables={}
    players_animals={}
    players_products={}
    def __init__(self, gender, name):
        self.gender=gender
        self.name=name
        self.money=0

adriana=Player('woman', 'adriana')
tomato=Vegetable('tomato',15)
tomato.water_plant(3)
tomato.buy_vegetable(adriana)
print(adriana.money)
