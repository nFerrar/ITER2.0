class Item(object):##this is a basic item, it has many many variables that cover its name and description and use, along with attached events
    
    def __init__(self, name, description, bPickUp, bUseable, bUseAlone, useWith, useText, bEvent, Trigger, Event):
        self.name = name
        self.description = description
        self.bPickUp = bPickUp
        self.bUseable = bUseable
        self.bUseAlone = bUseAlone
        self.useWith = useWith
        self.useText = useText
        self.bEvent = bEvent
        self.Trigger = Trigger
        self.Event = Event
        
    def describeItem(self):
        print("It's %s" % (self.description))

class Container(Item):##this is much like an item, except it has an inventory of its own, along with functionality to be opened and closed.
    
    tempD = {}

    def __init__(self, name, description, bPickUp, openDescription, contents, openText, closeText, bOpen, bUseable, bUseAlone, useWith, useText, bEvent, Trigger, Event, bLocked, keyItem, lockedText, unlockText, lockedDesc, bDestroyKey, keyDestroyText):
        self.name = name
        self.description = description
        self.bPickUp = bPickUp
        self.openDescription  = openDescription
        self.contents = contents
        self.openText = openText
        self.closeText = closeText
        self.bOpen = bOpen
        self.bUseable = bUseable
        self.bUseAlone = bUseAlone
        self.useWith = useWith
        self.useText = useText
        self.bEvent = bEvent
        self.Trigger = Trigger
        self.Event = Event
        self.bLocked = bLocked
        self.keyItem = keyItem
        self.lockedText = lockedText
        self.unlockText = unlockText
        self.lockedDesc = lockedDesc
        self.bDestroyKey = bDestroyKey
        self.keyDestroyText = keyDestroyText
        
    def describeItem(self):
        if(self.bOpen == False):
            if(self.bLocked == False):
                print("It's %s" % (self.description))
            else:
                print("It's %s" % (self.lockedDesc))
        else:
            print("It's %s" % (self.openDescription))
    
    def openContainer(self, Location, Character):
        if(self.bLocked == False):
            self.bOpen = True
            print(self.openText + " Inside you see")
            for i in self.contents:
                if(self.contents[i] > 1):
                    print(str(self.contents[i]) + " " + i)
                    Location.addItem(i, self.contents[i])
                else:
                    print(i)
                    Location.addItem(i, 1)
        else:
            for i in Character.inventory:
                if(i == self.keyItem):
                    print(self.unlockText)
                    self.bLocked = False
                    if(self.bDestroyKey == True):
                        print(self.keyDestroyText)
                    self.bOpen = True
                    print(self.openText + " Inside you see")
                    for i in self.contents:
                        if(self.contents[i] > 1):
                            print(str(self.contents[i]) + " " + i)
                            Location.addItem(i, self.contents[i])
                        else:
                            print(i)
                            Location.addItem(i, 1)
                    if(self.bDestroyKey == True):
                        Character.removeFromInventory(self.keyItem, 1)
                    break
            else:
                print(self.lockedText)
                
    def closeContainer(self, Location, Character):
        self.bOpen = False
        print(self.closeText)
        for i in self.contents:
            for x in Location.contents:
                if(i == x):
                    self.tempD[i] = Location.contents[x]
                    Location.removeItem(x, self.contents[i])
                    break
        self.contents = self.tempD
        self.tempD = {}