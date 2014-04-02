#!/usr/bin/env python

class artifact():
    
    __name = "Place Filler"
    
    def __init__(self, name):
        self.__name = name
    
    def Name(self):
        return self.__name
        pass
    
class magicartifact(artifact):
    __magicpower = 0
    
    def __init__(self, power):
        self.__magicpower = power
    
    def powerboost (self):
        return self.__magicpower
    
class weapon (artifact):
    __weapondamge = 0
    
    def __init__(self, power):
        self.__weapondamage = power

    def attackboost (self):
        return self.__weapondamage
    
    


