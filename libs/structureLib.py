from libs import engineLib as engine

class Structure(object):##Base class for things like doors, walls and pillars of interest. Cannot be picked up.

    def __init__(self, name, description, bUseable, bUseAlone, otherItem, useEvent, bExamineEvent, examineEvent):
        self.name = name
        self.description = description
        self.bUseable = bUseable
        self.bUseAlone = bUseAlone
        self.otherItem = otherItem
        self.useEvent = useEvent
        self.bExamineEvent = bExamineEvent
        self.examineEvent = examineEvent
        
    def examineStructure(self, Location, Character):
        print("It's %s" % (self.description))
        
        if(self.bExamineEvent == True):
            self.examineEvent.triggerEvent(Location, Character)
    
    def useStructure(self, Location, Character):
        if(self.bUseable == True):
            if(self.bUseAlone == True):
                self.useEvent.triggerEvent(Location, Character)
            else:
                cmd = input("What do you want use on it? >>>")
                
                if(cmd.lower() == self.otherItem):
                    for i in Character.inventory:
                        if(cmd.lower == i):
                            self.useEvent.triggerEvent(Location, Character)
                            break
                    else:
                        print("You don't have a %s." % (cmd.lower()))
                        engine.Scene(Location, Character)
                else:
                    for i in Character.inventory:
                        if(cmd.lower == i):
                            print("That doesn't seem to work.")
                            engine.Scene(Location, Character)
                            break
                    else:
                        print("You don't have a %s." % (cmd.lower()))
                        engine.Scene(Location, Character)
        else:
            print("You don't see a way to use that.")
            engine.Scene(Location, Character)