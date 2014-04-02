#!/usr/bin/env python
from random import *
class character ():
    
    # Basic Stats
    health = 10
    mana = 10
    stamina = 10
    armor = 3

    # Skills
    strength = 5 
    intelligence = 5 
    dexterity = 5 
    charisma = 5
    
    
    def attack(self, command, strength, weapondamge, damage, dexterity):
        if command == a:
            damage == weapondamge + strength
           
           

    def chance (self, dexterity):
        while True:
            hit = randint(0,10)
                #print ("Range %s"% hit)
            if hit == dexterity:
                print "Hit"
                return 1
            else:
                print "Miss"
                return 0
            
    def damagedone (self, damage):
        if chance == 1
            health - damage


class playerclass(character):
    __name = "Unknown"
    __backpack = set ()

   def __init__(self, name, strength):
    charater.__init__(self, strength)
    self.__name = name

    def name(self):
        retun self.__name

class nonplayercharacter(character):
    __charactertype = "PlaceFiller"
    
    def __init__(self, charactertype, strength):
        character.__init__(self, strength)
        self.__charactertype = charactertype

    def type (self):
        return self.__charactertype

    
   


    

 
    


  


