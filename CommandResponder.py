#!/usr/bin/env python
import sys

class CommandResponder (object) :
    
    def __init__ (self):
        self.__next = None
        
    def SetNext (self, r):
        self.__next = r;
        
    def HandleCommand (self, command) :
        print("I dont know how to %s" % command)
        if (self.__next != None) :
            self.__next.HandleCommand(command)
            
    def Next (self) :
    
        if (self.__next is None) :
            print ("No idea!")
            
        return self.__next    
    
class BucketCr (CommandResponder) :
    
    def HandleCommand (self, command) :
        print("I dont know how to %s" % command)
        
        
class GameEngineCommandResponder(CommandResponder) :
    def HandleCOmmand (self, command):
        normalisedCommand = command.upper()
        if (normalisedCommand == "Quit") :
            print ("Bye bye")
            sys.exit(0)
        if (normalisedCommand == "HELP") :
            print "Im the help genie - heres what you can do")
            
        return self.Next().HandleCommand(command)
    
class RoomCr (CommandResponder) :
    
    def HandleCommand (self, command) :
        if (command == "N" or command == "North") :
            print ("I can move north")
            return
        if (command == "S" or command == "South") :
            print ("I can move south")
            return
        return self.Next().HandleCommand(command)
    
class PersonCr (CommandResponder) :
    def HandleCommand (self, command) :
        if (command == "Sit") :
            print ("I can sit")
            return
        
        if (command == "Stand") :
            print ("I can stand")
            return
        return self.Next().HandleCommand(command)
    
#chain = PersonCr()
#room = RoomCr()
#bucket = BucketCr()

#room.SetNext (bucket)

#chain.HandleCommand ("Stand")
#chain.HandleCommand ("North")
#chain.HandleCommand ("Go away")