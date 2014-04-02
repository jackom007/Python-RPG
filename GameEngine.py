#!/usr/bin/env python
import random
import sys
import CommandResponder as Cr

class GameEngine(object):
    """the man adventure game engine"""
    ___currentState = None
    """a simple dice for generating randomness"""
    def __RollDice (faces):
        return random.randint(1,faces)
    
    def __init__(self) :
        print ("starting cd adventure")
        self.__currentState = MainMenuState();
        
    def Run (self) :
        while True:
            self.__currentState = self.__currentState.Run();
            if (slf.__currentState ==None):
                break   

class EngineState(object) :
    def Run (self) :
        raise Exception("Unknown State")
    
class MainMenuState (EngineState) :
    def Run (self):
        print ("    --- Main Menu ---")
        
        while True:
            
        print ("1 Start a new game")
        print ("2 Load a previously saved game")
        print ("3 Exit")
        
        menuChoice = int(input("choose 1-3: "))
        
        if (menuChoice == 1):
            return BuildCharacterState()
        
        if (menuChoice == 2):
            return LoadGameState()
        
        if (menuChoice == 3) :
            break
        
        print ("    ---Unknown Choice---")
                     
class BuildCharacterState (EngineState) :
    def Run (self):
        print ("   === Build a character for a new game ===")
        return RunningGameState()
    
class LoadGameState (EngineState) :
    def Run (self):
        print ("    *** Wouldnt it be nice if this worked")
        return MainMenuState()
    
class RunningGameState (EngineState) :
    __coreCammandResponder = none
    
    def __init__(self):
        bucket = Cr.BucketCr();
        self.__coreCommandResponder = Cr.GameEngineCommandResponder()
        seld.__coreCommandResponder.SetNext(bucket)
        
    def Run (self):
        print ("    ---Load a game map---")
        print ("   ---Load the character---")
        print ("    ----Run the command processor until such time as we quit----")
        while True
            nextCommand = input("what would you like to do now> ")
            self.__coreCommandResponder.HandleCommand(nextCommand)
        return    