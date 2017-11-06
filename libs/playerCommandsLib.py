from libs import engineLib as engine
import libs.decs.playerDec as P

class PlayerCommands(object):##These are all the commands the player can perform, they are as dynamic as possible.
    def __init__(self):
        pass
    
    def search(self, Location, Character, Command):##Search the area, makes the Zone print its contents
        Location.searchRoom()
        engine.checkForEvent(Location, Character, Location, "searchZone")
    
    def examine(self, Location, Character, Command):##Examines the area, makes the Zone print its description
            
        if(len(Command) > 7):
            for i in Location.references:
                if(engine.stringContains(i, Command) == True):
                    Location.examineRoom()
                    engine.checkForEvent(Location, Character, Location, "examineZone")
                    break
                    
            for i in Location.contents:
                if(engine.stringContains(i, Command) == True):
                    engine.stringToClass(i).describeItem()
                    if(Location.contents[i] > 1):
                        print("There are " + str(Location.contents[i]) + " of them.")
                    engine.checkForEvent(Location, Character, engine.stringToClass(i), "examineItem")
                    break
                    
            for c in Location.npcs:
                if(engine.stringContains(c, Command) == True):
                    engine.stringToClass(c).describeNPC()
                    engine.checkForEvent(Location, Character, engine.stringToClass(c), "examineNPC")
                    break
                    
            for i in P.Player.inventory:
                if(engine.stringContains(i, Command) == True):
                    engine.stringToClass(i).describeItem()
                    if(P.Player.inventory[i] > 1):
                        print("You are carrying " + str(P.Player.inventory[i]) + " of them.")
                    engine.checkForEvent(Location, Character, engine.stringToClass(i), "examineItem")
                    break
                        
            for s in Location.structures:
                if(engine.stringContains(s, Command) == True):
                    engine.stringToClass(s).examineStructure(Location, Character)
                    break
            
        else:
            cmd = input("Examine what? >>>")
            
            for i in Location.references:
                if(cmd.lower() == i):
                    Location.examineRoom()
                    engine.checkForEvent(Location, Character, Location, "examineZone")
                    break
                    
            for i in Location.contents:
                if(cmd.lower() == i):
                    engine.stringToClass(i).describeItem()
                    if(Location.contents[i] > 1):
                        print("There are " + str(Location.contents[i]) + " of them.")
                    engine.checkForEvent(Location, Character, engine.stringToClass(i), "examineItem")
                    break

            for c in Location.npcs:
                if(cmd.lower() == c):
                    engine.stringToClass(c).describeNPC()
                    engine.checkForEvent(Location, Character, engine.stringToClass(c), "examineNPC")
                    break
                    
            for i in P.Player.inventory:
                if(cmd.lower() == i):
                    engine.stringToClass(i).describeItem()
                    if(P.Player.inventory[i] > 1):
                        print("You are carrying " + str(P.Player.inventory[i]) + " of them.")
                    engine.checkForEvent(Location, Character, engine.stringToClass(i), "examineItem")
                    break
            
            for s in Location.structures:
                if(cmd.lower() == s):
                    engine.stringToClass(s).examineStructure(Location, Character)
                    break
                
            else:
                if(cmd.lower() == "self"):
                    print("You are " + Character.name + ", a " + Character.description)
                    print("----------")
                    print("HP: %s" % (str(Character.HP)))
                    print("SP: %s" % (str(Character.SP)))
                    print("MP: %s" % (str(Character.MP)))
                    print("----------")
                    print("Body: %s" % (str(Character.Body)))
                    print("Spirit: %s" % (str(Character.Spirit)))
                    print("Mind: %s" % (str(Character.Mind)))
                    print("----------")
                    engine.Scene(Location, Character)
                else:
                    print("You don't see a %s here." % (cmd.lower()))
                    engine.Scene(Location, Character)
                        
    def inventory(self, Location, Character, Command):##Checks the players Inventory, printing its contents
        P.Player.checkInventory()
        engine.Scene(Location, Character)
        
    def quit(self, Location, Character, Command):##lets you quit, has a confirmation. NO SAVE BITCHES. YOLO
        cmd = input("Are you sure you want to quit?")
        
        if(cmd.lower() == "y" or cmd.lower() == "yes"):
            print("Shutting Down...")
            exit()
            
        else:
            engine.Scene(Location, Character)
        
    def help(self, Location, Character, Command):##simply prints all the commands, no descriptions for you GLHF
        print("Available Commands:")
        for c in Commands:
            print(c)
        engine.Scene(Location, Character)
        
    def open(self, Location, Character, Command):##used to open Container class items. toggles variables
            
        if(len(Command) > 4):
            for i in Location.contents:
                if(engine.stringContains(i, Command) == True):
                    if hasattr(engine.stringToClass(i), "bOpen"):
                        if(engine.stringToClass(i).bOpen == False):
                            engine.stringToClass(i).openContainer(Location, Character)
                            engine.checkForEvent(Location, Character, engine.stringToClass(i), "openContainer")

                        else:
                            print("It's already open.")
                            engine.Scene(Location, Character)
                            
                    else:
                        print("You can't open that.")
                        engine.Scene(Location, Character)
            
        else:
            cmd = input("Open what? >>>")
            
            for i in Location.contents:
                if(i == cmd.lower()):
                    if hasattr(engine.stringToClass(i), "bOpen"):
                        if(engine.stringToClass(i).bOpen == False):
                            engine.stringToClass(i).openContainer(Location, Character)
                            engine.checkForEvent(Location, Character, engine.stringToClass(i), "openContainer")

                        else:
                            print("It's already open.")
                            engine.Scene(Location, Character)
                            
                    else:
                        print("You can't open that.")
                        engine.Scene(Location, Character)
            else:
                print("You don't see a %s here." % (cmd.lower()))
                engine.Scene(Location, Character)
        
    def close(self, Location, Character, Command):##used to close open Containers. toggles variables and re-checks contents in case of deletion.
            
        if(len(Command) > 5):
            for i in Location.contents:
                if(engine.stringContains(i, Command) == True):
                    if hasattr(engine.stringToClass(i), "bOpen"):
                        if(engine.stringToClass(i).bOpen == True):
                            engine.stringToClass(i).closeContainer(Location, Character)
                            engine.checkForEvent(Location, Character, engine.stringToClass(i), "closeContainer")

                        else:
                            print("It's already closed.")
                            engine.Scene(Location, Character)
                    else:
                        print("You can't close that.")
                        engine.Scene(Location, Character)
            
        else:
            cmd = input("Close what? >>>")
            
            for i in Location.contents:
                if(i == cmd.lower()):
                    if hasattr(engine.stringToClass(i), "bOpen"):
                        if(engine.stringToClass(i).bOpen == True):
                            engine.stringToClass(i).closeContainer(Location, Character)
                            engine.checkForEvent(Location, Character, engine.stringToClass(i), "closeContainer")

                        else:
                            print("It's already closed.")
                            engine.Scene(Location, Character)
                    else:
                        print("You can't close that.")
                        engine.Scene(Location, Character)
            else:
                print("You don't see a %s here." % (cmd.lower()))
                engine.Scene(Location, Character)

    def take(self, Location, Character, Command):##lets the player pick up Items marked as pickupable.
            
        if(len(Command) > 4):
            for l in Location.contents:
                if(engine.stringContains(l, Command) == True):
                    if(engine.stringToClass(l).bPickUp == True):
                        Character.addToInventory(l, Location.contents[l])
                        Location.removeItem(l, Location.contents[l])
                        print("You pick up the %s." % (l))
                        engine.checkForEvent(Location, Character, engine.stringToClass(l), "pickupItem")

                    else:
                        print("You can't pick that up.")
                        engine.Scene(Location, Character)
            
        else:
            cmd = input("What would you like to pick up? >>>")
            
            for l in Location.contents:
                if(l == cmd.lower()):
                    if(engine.stringToClass(cmd.lower()).bPickUp == True):
                        Character.addToInventory(cmd.lower(), Location.contents[cmd.lower()])
                        Location.removeItem(cmd.lower(), Location.contents[cmd.lower()])
                        print("You pick up the %s." % (l))
                        engine.checkForEvent(Location, Character, engine.stringToClass(l), "pickupItem")

                    else:
                        print("You can't pick that up.")
                        engine.Scene(Location, Character)
            else:
                print("There isn't a %s here." % (cmd.lower()))
                engine.Scene(Location, Character)
            
    def drop(self, Location, Character, Command):##drops an item from the inventory to the zone. will go back into a container it came from
        
        if(len(Command) > 4):
            for l in Character.inventory:
                if(engine.stringContains(l, Command) == True):
                    q = input("Drop how many? >>>")
                        
                    try:
                        if(int(q) <= Character.inventory[l]):
                            Character.removeFromInventory(l, int(q))
                            Location.addItem(l, int(q))
                            print("You drop the %s." % (l))
                            engine.checkForEvent(Location, Character, engine.stringToClass(l), "dropItem")

                        else:
                            print("You don't have that many " + l +"s.")
                            engine.Scene(Location, Character)
                    except:
                        print("That's not a number!")
                        engine.Scene(Location, Character)
                    
        else:
            cmd = input("What do you want to drop? >>>")
            
            for l in Character.inventory:
                if(l == cmd.lower()):
                    q = input("Drop how many? >>>")
                    
                    try:
                        if(int(q) <= Character.inventory[cmd.lower()]):
                            Character.removeFromInventory(cmd.lower(), int(q))
                            Location.addItem(cmd.lower(), int(q))
                            print("You drop the %s." % (l))
                            engine.checkForEvent(Location, Character, engine.stringToClass(cmd.lower()), "dropItem")

                        else:
                            print("You don't have that many " + cmd.lower() +"s.")
                            engine.Scene(Location, Character)
                    except:
                        print("That's not a number!")
                        engine.Scene(Location, Character)
            else:
                print("You're not carrying a %s." % (cmd.lower()))
                engine.Scene(Location, Character)
            
    def move(self, Location, Character, Command):##moves the character from one location to another.
        
        if(len(Command) > 4):
            for d in Location.exits:
                if(engine.stringContains(d, Command) == True):
                    if(engine.stringToClass(Location.exits[d]).bLocked == False):
                            engine.ChangeLocation(Location, engine.stringToClass(Location.exits[d]), Character)
                            break
                    else:
                        for k in Character.inventory:
                            if(k == engine.stringToClass(Location.exits[d]).keyItem):
                                engine.stringToClass(Location.exits[d]).bLocked = False
                                print(engine.stringToClass(Location.exits[d]).unlockText)
                                
                                if(engine.stringToClass(Location.exits[d]).bDestroyKey == False):
                                    engine.ChangeLocation(Location, engine.stringToClass(Location.exits[d]), Character)
                                    break
                                else:
                                    print(engine.stringToClass(Location.exits[d]).keyDestroyText)
                                    Character.removeFromInventory(engine.stringToClass(Location.exits[d]).keyItem, 1)
                                    engine.ChangeLocation(Location, engine.stringToClass(Location.exits[d]), Character)
                                    break
                        else:
                            print(engine.stringToClass(Location.exits[d]).blockedText)
                            engine.Scene(Location, Character)
                            break
                        
            else:
                print("You cannot go that way.")
                engine.Scene(Location, Character)
        
        else:
            cmd = input("Which direction do you want to go? >>>")
            
            for d in Location.exits:
                if(d == cmd.lower()):
                    if(engine.stringToClass(Location.exits[d]).bLocked == False):
                        engine.ChangeLocation(Location, engine.stringToClass(Location.exits[d]), Character)
                        break
                    else:
                        for k in Character.inventory:
                            if(k == engine.stringToClass(Location.exits[d]).keyItem):
                                engine.stringToClass(Location.exits[d]).bLocked = False
                                print(engine.stringToClass(Location.exits[d]).unlockText)
                            
                                if(engine.stringToClass(Location.exits[d]).bDestroyKey == False):
                                    engine.ChangeLocation(Location, engine.stringToClass(Location.exits[d]), Character)
                                    break
                                else:
                                    print(engine.stringToClass(Location.exits[d]).keyDestroyText)
                                    Character.removeFromInventory(engine.stringToClass(Location.exits[d]).keyItem, 1)
                                    engine.ChangeLocation(Location, engine.stringToClass(Location.exits[d]), Character)
                                    break
                        else:
                            print(engine.stringToClass(Location.exits[d]).blockedText)
                            engine.Scene(Location, Character)
                            break
            else:
                print("You cannot go that way.")
                engine.Scene(Location, Character)
    
    def use(self, Location, Character, Command):##Uses items, duh ISSUE HERE WITH THE SECOND USE WITH WHAT COMMAND NOT INTELLIGENT
        
        if(len(Command) > 3):
            for i in Character.inventory:
                if(engine.stringContains(i, Command) == True):
                    if(engine.stringToClass(i).bUseable == True):
                            if(engine.stringToClass(i).bUseAlone == True):
                                print(engine.stringToClass(i).useText)
                                engine.checkForEvent(Location, Character, engine.stringToClass(i), "useItem")
                                break

                            else:
                                u = input("Use with what? >>>")
                                for x in Character.inventory:
                                    if(engine.stringContains(x, u) == True):
                                        if(engine.stringToClass(i).useWith == x):
                                            print(engine.stringToClass(i).useText)
                                            engine.checkForEvent(Location, Character, engine.stringToClass(i), "useItem")
                                            break

                                        else:
                                            print("You can't use those together.")
                                            engine.Scene(Location, Character)
                                for x in Location.contents:
                                    if(engine.stringContains(x, u) == True):
                                        if(engine.stringToClass(i).useWith == x):
                                            print(engine.stringToClass(i).useText)
                                            engine.checkForEvent(Location, Character, engine.stringToClass(i), "useItem")
                                            break

                                        else:
                                            print("You can't use those together.")
                                            engine.Scene(Location, Character)
                                            break
                                else:
                                    print("There isn't a %s here." % (u.lower()))
                                    engine.Scene(Location, Character)
                                    break
                    else:
                        print("You can't use that.")
                        engine.Scene(Location, Character)
                        break

            for i in Location.contents:
                if(engine.stringContains(i, Command) == True):
                    if(engine.stringToClass(i).bUseable == True):
                        if(engine.stringToClass(i).bUseAlone == True):
                            print(engine.stringToClass(i).useText)
                            engine.checkForEvent(Location, Character, engine.stringToClass(i), "useItem")
                            break

                        else:
                            u = input("Use with what? >>>")
                            for x in Character.inventory:
                                if(engine.stringContains(x, u) == True):
                                    if(engine.stringToClass(i).useWith == x):
                                        print(engine.stringToClass(i).useText)
                                        engine.checkForEvent(Location, Character, engine.stringToClass(i), "useItem")
                                        break

                                    else:
                                        print("You can't use those together.")
                                        engine.Scene(Location, Character)
                                        break
                            for x in Location.contents:
                                if(engine.stringContains(x, u) == True):
                                    if(engine.stringToClass(i).useWith == x):
                                        print(engine.stringToClass(i).useText)
                                        engine.checkForEvent(Location, Character, engine.stringToClass(i), "useItem")
                                        break

                                    else:
                                        print("You can't use those together.")
                                        engine.Scene(Location, Character)
                                        break
                            else:
                                print("There isn't a %s here." % (u.lower()))
                                engine.Scene(Location, Character)
                                break
                    else:
                        print("You can't use that.")
                        engine.Scene(Location, Character)
                        break

            for s in Location.structures:
                if(engine.stringContains(s, Command) == True):
                    engine.stringToClass(s).useStructure(Location, Character)
                    break
            
            
        else:
            cmd = input("Use what? >>>")
            
            for i in Character.inventory:
                if(cmd.lower() == i):
                    if(engine.stringToClass(cmd.lower()).bUseable == True):
                        if(engine.stringToClass(cmd.lower()).bUseAlone == True):
                            print(engine.stringToClass(cmd.lower()).useText)
                            engine.checkForEvent(Location, Character, engine.stringToClass(i), "useItem")
                            break

                        else:
                            u = input("Use with what? >>>")
                            for x in Character.inventory:
                                if(u.lower() == x):
                                    if(engine.stringToClass(cmd.lower()).useWith == x):
                                        print(engine.stringToClass(cmd.lower()).useText)
                                        engine.checkForEvent(Location, Character, engine.stringToClass(i), "useItem")
                                        break

                                    else:
                                        print("You can't use those together.")
                                        engine.Scene(Location, Character)
                            for x in Location.contents:
                                if(u.lower() == x):
                                    if(engine.stringToClass(cmd.lower()).useWith == x):
                                        print(engine.stringToClass(cmd.lower()).useText)
                                        engine.checkForEvent(Location, Character, engine.stringToClass(i), "useItem")
                                        break

                                    else:
                                        print("You can't use those together.")
                                        engine.Scene(Location, Character)
                                        break
                            else:
                                print("There isn't a %s here." % (u.lower()))
                                engine.Scene(Location, Character)
                                break
                    else:
                        print("You can't use that.")
                        engine.Scene(Location, Character)
                        break
            
            for i in Location.contents:
                if(cmd.lower() == i):
                    if(engine.stringToClass(cmd.lower()).bUseable == True):
                        if(engine.stringToClass(cmd.lower()).bUseAlone == True):
                            print(engine.stringToClass(cmd.lower()).useText)
                            engine.checkForEvent(Location, Character, engine.stringToClass(i), "useItem")
                            break

                        else:
                            u = input("Use with what? >>>")
                            for x in Character.inventory:
                                if(u.lower() == x):
                                    if(engine.stringToClass(cmd.lower()).useWith == x):
                                        print(engine.stringToClass(cmd.lower()).useText)
                                        engine.checkForEvent(Location, Character, engine.stringToClass(i), "useItem")
                                        break

                                    else:
                                        print("You can't use those together.")
                                        engine.Scene(Location, Character)
                                        break
                            for x in Location.contents:
                                if(u.lower() == x):
                                    if(engine.stringToClass(cmd.lower()).useWith == x):
                                        print(engine.stringToClass(cmd.lower()).useText)
                                        engine.checkForEvent(Location, Character, engine.stringToClass(i), "useItem")
                                        break

                                    else:
                                        print("You can't use those together.")
                                        engine.Scene(Location, Character)
                                        break
                            else:
                                print("There isn't a %s here." % (u.lower()))
                                engine.Scene(Location, Character)
                                break
                    else:
                        print("You can't use that.")
                        engine.Scene(Location, Character)
                        break
            
            for s in Location.structures:
                if(cmd.lower() == s):
                    engine.stringToClass(s).useStructure(Location, Character)
                    break
            
            else:
                print("There isn't a %s here." % (cmd.lower()))
                engine.Scene(Location, Character)

    def talk(self, Location, Character, Command):##talk to NPCs and hear the shit they have to say
        
        if(len(Command) > 4):
            for c in Location.npcs:
                if(engine.stringContains(c, Command) == True):
                    print("<<" + engine.stringToClass(c).name + "<<" + engine.stringToClass(c).Convo["intro"]["introtext"])
                    engine.Conversation(Location, Character, engine.stringToClass(c), engine.stringToClass(c).Convo["intro"], engine.stringToClass(c).Convo["intro"])
                    break
        else:
            cmd = input("Who do you want to talk to? >>>")
            
            for c in Location.npcs:
                if(cmd.lower() == c):
                    print(engine.stringToClass(c).Convo["intro"]["introtext"])
                    engine.Conversation(Location, Character, engine.stringToClass(c), engine.stringToClass(c).Convo["intro"], engine.stringToClass(c).Convo["intro"])
                    break
            else:
                print("You don't see anyone called %s here." % (cmd))
                engine.Scene(Location, Character)
    
    def attack(self, Location, Character, Command):##Use this to attack people, you monster
    
        if(len(Command) > 6):
            for c in Location.npcs:
                if(engine.stringContains(c, Command) == True):
                    print("You make a move towards %s, and they turn to face you, seeing your intent. You've a fight on your hands." % engine.stringToClass(c).name)
                    engine.stringToClass(c).bAggressive = True
                    engine.Scene(Location, Character)
                    break
        else:
            cmd = input("Who do you want to attack? >>>")
            
            for c in Location.npcs:
                if(engine.stringContains(c, cmd) == True):
                    print("You make a move towards %s, and they turn to face you, seeing your intent. You've a fight on your hands." % (engine.stringToClass(c).name))
                    engine.stringToClass(c).bAggressive = True
                    engine.Scene(Location, Character)
                    break
                    
            else:
                print("You don't see %s here." % (cmd))
                engine.Scene(Location, Character)
            
    def self(self, Location, Character, Command):
        print("You are " + Character.name + ", a " + Character.description)
        print("----------")
        print("HP: %s" % (str(Character.HP)))
        print("SP: %s" % (str(Character.SP)))
        print("MP: %s" % (str(Character.MP)))
        print("----------")
        print("Body:   %s" % (str(Character.Body)))
        print("Spirit: %s" % (str(Character.Spirit)))
        print("Mind:   %s" % (str(Character.Mind)))
        engine.Scene(Location, Character)
    
## START PLAYER COMMANDS## NO TOUCHING ##
Commands = ["search", "examine", "inventory", "quit", "help", "open", "close", "take", "drop", "move", "use", "talk", "attack", "self"]
playerCommand = PlayerCommands()
## END PLAYER COMMANDS## NO TOUCHING ##