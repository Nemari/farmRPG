import pygame
import game_config as gc

class Player:
    def __init__(self, gender, name):
        self.players_vegetables = {}
        self.players_animals = {}
        self.players_products = {}
        self.gender=gender
        self.name=name
        self.money=5

    def stall(self, farm_obj, farm, x, y): #set an animal to a place
        farm.farm_tiles[(x,y)]=farm_obj

maria = Player('woman', 'mariia')