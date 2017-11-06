class Person(object):##this is a generic person, with a name, inventory and basic add/remove item functions
    def __init__(self, name, description, inventory, Mind, Body, Spirit, HP, SP, MP, Attacks):
        self.name = name
        self.description = description
        self.inventory = inventory
        self.Mind = Mind
        self.Body = Body
        self.Spirit = Spirit
        self.HP = HP
        self.SP = SP
        self.MP = MP
        self.Attacks = Attacks
    
    def addToInventory(self, newItem, quantity):
        if(len(self.inventory) > 0):
            for i in self.inventory:
                if(newItem == i):
                    self.inventory[i] = self.inventory[i] + quantity
                    break
                else:
                    self.inventory[newItem] = quantity
                    break
        else:
            self.inventory[newItem] = quantity
            
    def removeFromInventory(self, item, quantity):
        for i in self.inventory:
            if(item == i):
                if(self.inventory[i] > quantity):
                    self.inventory[i] = self.inventory[i] - quantity
                    break
                else:
                    del self.inventory[i]
                    break
        
        else:
            print("You're not carrying a %s." % (str(item)))
    
class PC(Person):##this is the player character class, it adds a checkInventory function to the Person class
    def checkInventory(self):
        print("You take a moment to check what you're carrying.")
        
        if(self.inventory != {}):
            print("You have on you:")
            for i in self.inventory:
                if(self.inventory[i] > 1):
                    print(str(self.inventory[i]) + " " + str(i) + "s")
                else:
                    print(str(i))
        
        else:
            print("You don't seem to be carrying anything.")

class NPC(Person):##NPCs. Anything other than the player.
    def __init__(self, name, pronouns, inventory, Mind, Body, Spirit, HP, SP, MP, description, bEvent, Trigger, Event, Convo, bAggressive, Attacks):
        self.name = name
        self.pronouns = pronouns
        self.inventory = inventory
        self.Mind = Mind
        self.Body = Body
        self.Spirit = Spirit
        self.HP = HP
        self.SP = SP
        self.MP = MP
        self.description = description
        self.bEvent = bEvent
        self.Trigger = Trigger
        self.Event = Event
        self.Convo = Convo
        self.bAggressive = bAggressive
        self.Attacks = Attacks
        
    def describeNPC(self):
        print("%s is %s" % (self.name, self.description))
        if(self.Body >= 100):
            print("%s looks in perfect health." % (self.pronouns["he"]))
        elif(self.Body >= 50):
            print("%s looks a little worse for ware." % (self.pronouns["he"]))
        else:
            print("%s looks near death." % (self.pronouns["he"]))