#!/usr/bin/env python
class room():
    __artifact = set()
    __players = set()
    __npcs = set()
    __description = "Filler"
    
    def __init__(self, description):
        self.__description = description

    def addartifact(self, artifact):
        self.__artifact.add(artifact)

    def addnpc(self, player):
        self.__npcs.add(npc)

    def addplayer(self, player):
        self.__player.add(player)

    def look (self):
        print (self.__description)
        print ("\nIn this room you see")
        for a in self.__artifacts:
            print (a.name())
        if (len(self.__npcs) > 0):
            for np in self.__npcs:
                print ("\nThere is a %s here." % np.type())
    

