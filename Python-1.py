from random import *

dexterity = 5

def chance (dexterity):
    while True:
        hit = randint(0,10)
        print ("Range %s"% hit)
        if hit == dexterity:
          print "Hit"
          return 1
        else:
          print "Miss"
          return 0

chanceResult = 0

while chanceResult == 0:
  chanceResult = chance (dexterity)
  
