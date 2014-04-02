#!/usr/bin/env python
import artifactclass.atrifact
class Backpack(Artifact):
    bp = ArtifactClass.a

    def ExecuteCommand(self, command):
        if command == "i":
            print self
        else: print "I don't understand that command"

    def ShowInventory(self):
        print 
bp= backpack()

command = raw_input()
bp.excute_command(command)



  
