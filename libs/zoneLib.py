from libs import engineLib as engine
##Done with the includes

class Zone(object):##this is all rooms and areas the player will be in. It has add/remove item functions and search/examine functions

    def __init__(self, name, references, description, contents, exits, bLocked, keyItem, blockedText, unlockText, bDestroyKey, keyDestroyText, bEvent, Trigger, Event, structures, npcs):
        self.name = name
        self.references = references
        self.description = description
        self.contents = contents
        self.exits = exits
        self.bLocked = bLocked
        self.keyItem = keyItem
        self.blockedText = blockedText
        self.unlockText = unlockText
        self.bDestroyKey = bDestroyKey
        self.keyDestroyText = keyDestroyText
        self.bEvent = bEvent
        self.Trigger = Trigger
        self.Event = Event
        self.structures = structures
        self.npcs = npcs
        
    def examineRoom(self):
        print("You are in a " + self.description)
        
    def searchRoom(self):
        print("You search the immediate area, and you find:")
        
        if(self.contents != {}):
            for i in self.contents:
                if(self.contents[i] == 1):
                    print(engine.stringToClass(i).name)
                else:
                    print(str(self.contents[i])+ " " + i + "s")
        else:
            print("Nothing.")
        
        if(self.structures != []):
            print("In the %s you also see:" % (self.references[0]))
            for s in self.structures:
                print(engine.stringToClass(s).name)
                
        if(self.exits != {}):
            print("And exits to the")
            for x in self.exits:
                print(x)
            
        if(self.npcs != []):
            for c in self.npcs:
                print("%s is here." % (engine.stringToClass(c).name))
                
    def addItem(self, item, quantity):
        if(len(self.contents) > 0):
            for i in self.contents:
                if(item == i):
                    self.contents[i] = self.contents[i] + quantity
                    break        
                else:
                    self.contents[item] = quantity
                    break
        else:
            self.contents[item] = quantity
    
    def removeItem(self, item, quantity):
        for i in self.contents:
            if(i == item):
                if(self.contents[i] > quantity):
                    self.contents[i] = self.contents[i] - quantity
                    break
                else:
                    del self.contents[i]
                    break
    
    def addExit(self, direction, zone):
        for x in self.exits:
            if(x == direction):
                print("There is already an exit that way.")
                break
        else:
            self.exits[direction] = zone

    def removeExit(self, direction):
        for x in self.exits:
            if(x == direction):
                del self.exits[x]
                break
    
    def addStructure(self, newStructure):
        for i in self.structures:
            if(newStructure == i):
                break        
        else:
            self.structures.append(newStructure)
                            
    def removeStucture(self, Structure):
        for i in self.structures:
            if(i == Structure):
                self.structures.remove(i)
                break
                
    def addNPC(self, NPC):
        for c in self.npcs:
            if(NPC == c):
                break
        else:
            self.npcs.append(NPC)
    
    def removeNPC(self, NPC):
        for c in self.npcs:
            if(c == NPC):
                self.npcs.remove(c)
                break