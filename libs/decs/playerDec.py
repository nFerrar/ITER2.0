from libs import personLib as person

## BEGIN PLAYER CREATION ##
pInv = {}
playerAttacks = {
    "HP": ["You strike out at the enemy,", "With a yell you batter your opponent with a series of blows,"],
    "SP" : ["You yell in an attempt intimidate the enemy,", "You sling a slew of insults at your opponent,"],
    "MP" : ["Summoning your inner reserves, you focus energy at your enemy,", "You thrust forward your arm, letting out a stream of energy,"]
    }
Player = person.PC("Dickbutt", "short, ugly and kind of intangible being who is the closest thing to a human without actually being one. Weird.", pInv, 10, 10, 10, 100, 100, 100, playerAttacks)
## END PLAYER CREATION ##