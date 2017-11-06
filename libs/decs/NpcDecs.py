from libs import personLib as p
##Done with the includes

## BEGIN NPC CREATION ##
bobInv = {}
bobPronouns = {
"he" : "He",
"his" : "His",
"him" : "Him",
}
playerAttacks = {
    "HP": ["You strike out at the enemy,", "With a yell you batter your opponent with a series of blows,"],
    "SP" : ["You yell in an attempt intimidate the enemy,", "You sling a slew of insults at your opponent,"],
    "MP" : ["Summoning your inner reserves, you focus energy at your enemy,", "You thrust forward your arm, letting out a stream of energy,"]
    }
bobConvo = {
"intro" : {
    "introtext" : "'What can I help you with?'",
    "none" : "'I'm sorry. My responses are limited, you must ask the right questions.'",
    "who" : {
        "introtext" : "Who do you want to know about?",
        "me" : "'You? I don't know. If you can't remember then that's something you may want to look into.'",
        "i" : "'You? I don't know. If you can't remember then that's something you may want to look into.'",
        "you" : {
            "introtext" : "What do you want to know about me?",
            "who" : "'I'm Bob, the two dimensional test character who has even less programming behind him than a box. Give me time and I may become a bit more complicated. Until then fuck you and your organic privilege.",
            "where" : "'I'm from nowhere in particular, which is a lovely place this time of year.'",
            "why" : "'I'm only here because Nic needed a way to test NPCs quickly.'",
            "how" : "'I got here through the magic of code. I'm also in the wall.'"
            },
        },
    "here" : "'This is only a small test area. There are three different locations you can visit...well four technically, but as far as your concerned there are only three. Don't expect much from any of them though.'",
    "fuck" : "'Watch your profamity.'",
    "where" : "'This place is just a construct. A framework. Someday it may be a wondrous place of adventure, but right now it is the worldly equivalent of scaffolding held up by google and machete-like practises.'",
    "goodbye" : "'Get the fuck out.'",
    },
}
bobEvent = {
    "playerHP_Victory" : "victory",
    "playerHP_Lose" : "loss",
    "playerSP_Victory" : "victory",
    "playerSP_Lose" : "loss",
    "playerMP_Victory" : "victory",
    "playerMP_Lose" : "loss",}
bob = p.NPC("Bob", bobPronouns, bobInv, 10, 10, 10, 100, 100, 100, "a short, uninteresting fellow with strange, oddly arranged facial features that you'd think make him easy to remember, but somehow have the opposite effect.", False, "none", bobEvent, bobConvo, False, playerAttacks)
## END NPC CREATION ##