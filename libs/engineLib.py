import sys
import re
import random

from libs.playerCommandsLib import Commands
from libs.playerCommandsLib import playerCommand

from libs.decs.itemDecs import *
from libs.decs.eventDecs import *
from libs.decs.NpcDecs import *
from libs.decs.playerDec import *
from libs.decs.structureDecs import *
from libs.decs.zoneDecs import *

##Done with the includes

def stringContains(word, phrase):##this guy finds a word in a phrase, and can be asked in a manner consistent with the rest of python.
    if(findWord(word)(phrase)):
        return True
    else:
        return False

def findWord(w):##This guy finds if a word is in a phrase, intelligently
    return re.compile(r'\b({0})\b'.format(w), flags=re.IGNORECASE).search

def bDeeper(dictValue):##This checks if there i a deeper level of conversation
    try:
        x = len(dictValue.keys())
        return True
    except:
        return False
    
def Conversation(Location, Character, NPC, stage, previousStage):##conversation 'scene'. KISS STRIKES AGAIN, WAIT EVENT NOT WORKING
    
    cmd = input(">>Say>>")
    
    if(cmd.lower() == "back" or cmd.lower() == "nevermind"):
        print("<<" + NPC.name + "<<" + previousStage["introtext"])
        Conversation(Location, Character, NPC, previousStage, NPC.Convo["intro"])
        
    if("bye" in cmd.lower() or stringContains("leave", cmd) == True or "farewell" in cmd.lower()):
        print("<<" + NPC.name + "<<" + NPC.Convo["intro"]["goodbye"])
        Scene(Location, Character)

    for i in stage:
        if(stringContains(i, cmd.lower()) == True):
            if(bDeeper(stage[i]) == True):
                print("<<" + NPC.name + "<<" + stage[i]["introtext"])
                if(NPC.bEvent == False):
                    Conversation(Location, Character, NPC, stage[i], stage)
                    break
                else:
                    for e in NPC.Event.keys():
                        if(i in e):
                            stringToClass(NPC.Event[e]).triggerEvent(Location, Character)
                            break
                    else:
                        Conversation(Location, Character, NPC, stage[i], stage)
                        break
                    
            else:
                if(NPC.bEvent == False):
                    print("<<" + NPC.name + "<<" + stage[i])
                    Conversation(Location, Character, NPC, stage, previousStage)
                    break
                else:
                    print("<<" + NPC.name + "<<" + stage[i])
                    for e in NPC.Event:
                        if(i in e):##+++++++++++++++++++++++++++++++++++++++++++CLOSER
                            stringToClass(NPC.Event[e]).triggerEvent(Location, Character)
                            break
                    else:
                        Conversation(Location, Character, NPC, stage, previousStage)
                        break
    else:
        print("%s looks confused." % (NPC.name))
        print("<<" + NPC.name + "<<" + NPC.Convo["intro"]["none"])
        Conversation(Location, Character, NPC, stage, previousStage)
                
def checkForEvent(Location, Character, caller, situation):##Call this to check if an event should be run.

    if(caller.bEvent == True):

        if(caller.Trigger == situation):
            caller.Event.triggerEvent(Location, Character)
        else:
            Scene(Location, Character)
    else:
        Scene(Location, Character)

def ChangeLocation(oldLocation, newLocation, Character):##This moves the player from oldLocation to newLocation. Moves the character class to maintain inventory and stats.
    print("You step out of the " + oldLocation.name + " and into " + newLocation.name + ", " + newLocation.description)
    if(newLocation.npcs != []):
        for c in newLocation.npcs:
            print("%s is here." % (stringToClass(c).name))
    checkForEvent(newLocation, Character, newLocation, "enterZone")

def Scene(Location, Character):##====This is the current scene. All commands and events should come back to this.
    for c in Location.npcs:
        if stringToClass(c).bAggressive == True:
            print("Battle because %s wants to fight." % (stringToClass(c).name))
            print("----------")
            Battle(Character, stringToClass(c), Location)
            break
    else:
        print("----------")##clock could go here.
        cmd = input(">>>")
        
        for i in Commands:
            if(stringContains(i, cmd) == True):
                stringToClassDef(playerCommand, i)(Location, Character, cmd)## This is where all player input is passed to the relevant command
                
        else:
            print("Command not recognised.")
            Scene(Location, Character)

def stringToClass(s):##This is meant to turn strings into class names.
    return getattr(sys.modules[__name__], s)

def stringToClassDef(className, defName):##This takes strings and makes them a def name within a class. className.defName is the result. can be handed arguments
    return getattr(className, defName)
    
def enemyAttack(player, enemy, location, bDefend):
    atk = random.randint(0, 2)
    
    if(bDefend == False):
        if atk == 0:
            if(player.Body + random.randint(1, 20) < enemy.Body + random.randint(1, 20)):
                Edmg = int(random.randint(0, enemy.HP) / 2)
                print(enemy.Attacks["HP"][random.randint(0, len(enemy.Attacks["HP"])-1)])
                print("You receive " + str(Edmg) + " HP damage.")
                player.HP -= Edmg
                print("----------")
                if player.HP <= 0:
                    enemy.bAggressive = False
                    BattleComplete("playerHP_Lose", player, enemy, location)
                else:
                    Battle(player, enemy, location)

            else:
                print(enemy.Attacks["HP"][random.randint(0, len(enemy.Attacks["HP"])-1)])
                print("You manage to avoid taking damage.")
                print("----------")
                Battle(player, enemy, location)
                
        if atk == 1:
            if(player.Spirit + random.randint(1, 20) < enemy.Spirit + random.randint(1, 20)):
                Edmg = int(random.randint(0, enemy.SP) / 2)
                print(enemy.Attacks["SP"][random.randint(0, len(enemy.Attacks["SP"])-1)])
                print("You receive " + str(Edmg) + " SP damage.")
                player.SP -= Edmg
                print("----------")
                if player.SP <= 0:
                    enemy.bAggressive = False
                    BattleComplete("playerSP_Lose", player, enemy, location)
                else:
                    Battle(player, enemy, location)
            else:
                print(enemy.Attacks["SP"][random.randint(0, len(enemy.Attacks["SP"])-1)])
                print("You manage to avoid taking damage.")
                print("----------")
                Battle(player, enemy, location)
                
        if atk == 2:
            if(player.Mind + random.randint(1, 20) < enemy.Mind + random.randint(1, 20)):
                Edmg = int(random.randint(0, enemy.MP) / 2)
                print(enemy.Attacks["MP"][random.randint(0, len(enemy.Attacks["MP"])-1)])
                print("You receive " + str(Edmg) + " MP damage.")
                player.MP -= Edmg
                print("----------")
                if player.MP <= 0:
                    enemy.bAggressive = False
                    BattleComplete("playerMP_Lose", player, enemy, location)
                else:
                    Battle(player, enemy, location)
            else:
                print(enemy.Attacks["MP"][random.randint(0, len(enemy.Attacks["MP"])-1)])
                print("You manage to avoid taking damage.")
                print("----------")
                Battle(player, enemy, location)
                
    else:
        if atk == 0:
            if(player.Body + random.randint(10, 30) < enemy.Body + random.randint(1, 20)):
                Edmg = int(random.randint(0, enemy.HP) / 2)
                print(enemy.Attacks["HP"][random.randint(0, len(enemy.Attacks["HP"])-1)])
                print("You receive " + str(Edmg) + " HP damage.")
                player.HP -= Edmg
                print("----------")
                if player.HP <= 0:
                    enemy.bAggressive = False
                    BattleComplete("playerHP_Lose", player, enemy, location)
                else:
                    Battle(player, enemy, location)
            else:
                print(enemy.Attacks["HP"][random.randint(0, len(enemy.Attacks["HP"])-1)])
                print("You manage to avoid taking damage.")
                print("----------")
                Battle(player, enemy, location)
                
        if atk == 1:
            if(player.Spirit + random.randint(10, 30) < enemy.Spirit + random.randint(1, 20)):
                Edmg = int(random.randint(0, enemy.SP) / 2)
                print(enemy.Attacks["SP"][random.randint(0, len(enemy.Attacks["SP"])-1)])
                print("You receive " + str(Edmg) + " SP damage.")
                player.SP -= Edmg
                print("----------")
                if player.SP <= 0:
                    enemy.bAggressive = False
                    BattleComplete("playerSP_Lose", player, enemy, location)
                else:
                    Battle(player, enemy, location)
            else:
                print(enemy.Attacks["SP"][random.randint(0, len(enemy.Attacks["SP"])-1)])
                print("You manage to avoid taking damage.")
                print("----------")
                Battle(player, enemy, location)
                
        if atk == 2:
            if(player.Mind + random.randint(10, 30) < enemy.Mind + random.randint(1, 20)):
                Edmg = int(random.randint(0, enemy.MP) / 2)
                print(enemy.Attacks["MP"][random.randint(0, len(enemy.Attacks["MP"])-1)])
                print("You receive " + str(Edmg) + " MP damage.")
                player.MP -= Edmg
                print("----------")
                if player.MP <= 0:
                    enemy.bAggressive = False
                    BattleComplete("playerMP_Lose", player, enemy, location)
                else:
                    Battle(player, enemy, location)
            else:
                print(enemy.Attacks["MP"][random.randint(0, len(enemy.Attacks["MP"])-1)])
                print("You manage to avoid taking damage.")
                print("----------")
                Battle(player, enemy, location)        

def BattleComplete(cause, PC, NPC, location):##called when the battle is complete.
    if(len(NPC.inventory) > 0):
        print("The %s is defeated, dropping:" % NPC.name)
        for i in NPC.inventory:
            location.addItem(i, NPC.inventory[i])
            if NPC.inventory[i] > 1:
                print(str(NPC.inventory[i]) + " " + i + "s")
            else:
                print("a %s" % i)
    else:
        print("The %s is defeated, dropping no items." % NPC.name)
    print("----------")
    stringToClass(NPC.Event[cause]).triggerEvent(location, PC)
            
def Battle(player, enemy, location):

    print("You are battling a " + enemy.name + ", " + enemy.description)
    
    if enemy.HP >= (enemy.Body * 10 / 2):
        print("It looks in perfect health.")
    if enemy.HP <= (enemy.Body * 10 / 4):
        print("It looks a little shaky on its feet.")
    if enemy.HP <= (enemy.Body):
        print("It looks near death.")

    print("----------")
    print("HP: %s" % (str(player.HP)))
    print("SP: %s" % (str(player.SP)))
    print("MP: %s" % (str(player.MP)))
    print("----------")
    cmd = input(">>Attack>>")
    print("----------")
    
    if cmd.lower() == "help":
        print("Available Battle Commands:")
        print("'Body'   -   A basic attack.")
        print("'Spirit' -   Perform a spiritual attack on your enemy.")
        print("'Mind'   -   Attack your enemy's mind.")
        print("'Defend' -   Ready yourself for any enemy attack.")
        print("----------")
        Battle(player, enemy, location)
    
    if cmd.lower() == "body":
        if(player.Body + random.randint(1, 20) > enemy.Body + random.randint(1, 20)):
            dmg = int(random.randint(0, player.HP) / 2)
            print(player.Attacks["HP"][random.randint(0, len(player.Attacks["HP"]) -1)] + " causing " + str(dmg) + " HP damage.")
            enemy.HP -= dmg
            print("----------")
            
            if enemy.HP <= 0:
                enemy.bAggressive = False
                BattleComplete("playerHP_Victory", player, enemy, location)
            
            else:        
                enemyAttack(player, enemy, location, False)
        else:
            print(player.Attacks["HP"][random.randint(0, len(player.Attacks["HP"]) -1)] + " but your attack misses.")
            print("----------")
            enemyAttack(player, enemy, location, False)
                
    if cmd.lower() == "spirit":
        if(player.Spirit + random.randint(1, 20) > enemy.Spirit + random.randint(1, 20)):
            dmg = int(random.randint(0, player.SP) / 2)
            print(player.Attacks["SP"][random.randint(0, len(player.Attacks["SP"]) -1)] + " causing " + str(dmg) + " SP damage.")
            enemy.SP -= dmg
            print("----------")
            
            if enemy.SP <= 0:
                enemy.bAggressive = False
                BattleComplete("playerSP_Victory", player, enemy, location)
            
            else:        
                enemyAttack(player, enemy, location, False)
        else:
            print(player.Attacks["SP"][random.randint(0, len(player.Attacks["SP"]) -1)] + " but your attack fails.")
            print("----------")
            enemyAttack(player, enemy, location, False)
                
    if cmd.lower() == "mind":
        if(player.Mind + random.randint(1, 20) > enemy.Mind + random.randint(1, 20)):
            dmg = int(random.randint(0, player.MP) / 2)
            print(player.Attacks["MP"][random.randint(0, len(player.Attacks["MP"]) -1)] + " causing " + str(dmg) + " MP damage.")
            enemy.MP -= dmg
            print("----------")
            
            if enemy.MP <= 0:
                enemy.bAggressive = False
                BattleComplete("playerMP_Victory", player, enemy, location)
            
            else:        
                enemyAttack(player, enemy, location, False)
        else:
            print(player.Attacks["MP"][random.randint(0, len(player.Attacks["MP"]) -1)] + " but your attack fails.")
            print("----------")
            enemyAttack(player, enemy, location, False)

    if cmd.lower() == "defend":
        print("You ready yourself for any attacks that may come.")
        print("----------")
        enemyAttack(player, enemy, location, True)
            
    else:
        print("Command not recognized")
        print("----------")
        Battle(player, enemy, location)