import os
import time
import random

from libs import engineLib as engine

class Event(object):##these are events, where the majority of the Engines power comes from, events can print, add/remove items to the room and player, and teleport the player to a new location without informing them. Each command can only be used once it seems.
    
    activeNPC = "none"
    
    def __init__(self, Location, Character, EventActions, EventOrder, Repeat, bToConversation, NPC):
        self.Location = Location
        self.Character = Character
        self.EventActions = EventActions
        self.EventOrder = EventOrder
        self.Repeat = Repeat
        self.bToConversation = bToConversation
        self.NPC = NPC
        
    def triggerEvent(self, activeLocation, activeCharacter):##this runs through all the event items
    
        self.Location = activeLocation
        self.Character = activeCharacter
        
        if(self.Repeat >= 0):
            for e in self.EventOrder:
                if(e != "EVENT"):
                    if(e != "RANDOMEVENT"):
                        engine.stringToClassDef(self, e)(self.EventActions[e])
                        time.sleep(0.1)
                    else:
                        self.Repeat -= 1
                        engine.stringToClassDef(self, e)(self.EventActions[e])
                else:
                    self.Repeat -= 1
                    engine.stringToClassDef(engine.stringToClass(self.EventActions[e]), "triggerEvent")(self.Location, self.Character)
            self.Repeat -= 1
            if(self.bToConversation == False):
                engine.Scene(self.Location, self.Character)
            else:
                engine.Conversation(self.Location, self.Character, engine.stringToClass(self.NPC), engine.stringToClass(self.NPC).Convo["intro"], engine.stringToClass(self.NPC).Convo["intro"])
        if(self.Repeat <= -1):
            for e in self.EventOrder:
                if(e != "EVENT"):
                    if(e != "RANDOMEVENT"):
                        engine.stringToClassDef(self, e)(self.EventActions[e])
                        time.sleep(0.1)
                    else:
                        self.Repeat -= 1
                        engine.stringToClassDef(self, e)(self.EventActions[e])
                else:
                    engine.stringToClassDef(engine.stringToClass(self.EventActions[e]), "triggerEvent")(self.Location, self.Character)
            if(self.bToConversation == False):
                engine.Scene(self.Location, self.Character)
            else:
                engine.Conversation(self.Location, self.Character, engine.stringToClass(self.NPC), engine.stringToClass(self.NPC).Convo["intro"], engine.stringToClass(self.NPC).Convo["intro"])
            
        else:
            if(self.bToConversation == False):
                engine.Scene(self.Location, self.Character)
            else:
                engine.Conversation(self.Location, self.Character, engine.stringToClass(self.NPC), engine.stringToClass(self.NPC).Convo["intro"], engine.stringToClass(self.NPC).Convo["intro"])

    def PRINT(self, text):##Call to print something to screen.
        print(text)
    
    def ADDTOINVENTORY(self, item):##Call to add an item to the player character
        self.Character.addToInventory(item[0], item[1])
        
    def REMOVEFROMINVENTORY(self, item):##Call to remove an item from the player character
        self.Character.removeFromInventory(item[0], item[1])
        
    def ADDITEM(self, item):##Call to add an item to the surround area
        self.Location.addItem(item[0], item[1])
        
    def REMOVEITEM(self, item):##Call to remove an item from the surrounding area
        self.Location.removeItem(item[0], item[1])
        
    def TELEPORT(self, newLocation):##Call to teleport the player to a different room without telling them. Good for making a room 'change'
        self.Location = engine.stringToClass(newLocation)

    def ADDEXIT(self, newExit):##This adds exits to the Location
        for x in newExit:
            self.Location.addExit(x, newExit[x])
            
    def REMOVEEXIT(self, delExit):##This removes and exit from the Location
        self.Location.removeExit(delExit)
    
    def WAIT(self, waitText):##Prints waitText and waits for input, does not save input. Use this for walls of text/page turning etc. I dont like the current functionality, but its the only way to actually make it reliable.
        os.system("echo %s" % (waitText))
        os.system("pause")
    
    def ADDSTRUCTURE(self, structure):##Adds a structure to the room
        self.Location.addStructure(structure)
    
    def REMOVESTRUCTURE(self, structure):## Removes a structure from the room.
        self.Location.removeStucture(structure)
    
    def ADDNPC(self, NPC):##Adds NPC to zone
        self.Location.addNPC(NPC)
        
    def REMOVENPC(self, NPC):##Removes an NPC from the zone
        self.Location.removeNPC(NPC)
    
    def ADDTONPCINVENTORY(self, item):##Adds item to the active NPCs inventory
        engine.stringToClass(item[0]).addToInventory(item[1], item[2])
    
    def REMOVEFROMNPCINVENTORY(self, item):##Removes item from active NPC inventory.
        engine.stringToClass(item[0]).removeFromInventory(item[1], item[2])

    def RANDOMEVENT(self, eventList):##Rolls through a list of events and picks one at random.
        engine.stringToClassDef(engine.stringToClass(eventList[random.randint(0, len(eventList)-1)]), "triggerEvent")(self.Location, self.Character)
    
    def MODIFYPCHP(self, mod):
        self.Character.HP += mod
    
    def MODIFYPCSP(self, mod):
        self.Character.SP += mod
    
    def MODIFYPCMP(self, mod):
        self.Character.MP += mod
        
    def MODIFYPCMIND(self, mod):
        self.Character.Mind += mod
        
    def MODIFYPCBODY(self, mod):
        self.Character.Body += mod
        
    def MODIFYPCSPIRIT(self, mod):
        self.Character.Spirit += mod
        
    def SETPCHP(self, mod):
        self.Character.HP = mod
    
    def SETPCSP(self, mod):
        self.Character.SP = mod
    
    def SETPCMP(self, mod):
        self.Character.MP = mod
        
    def SETPCMIND(self, mod):
        self.Character.Mind = mod
        
    def SETPCBODY(self, mod):
        self.Character.Body = mod
        
    def SETPCSPIRIT(self, mod):
        self.Character.Spirit = mod