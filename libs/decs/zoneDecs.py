from libs import zoneLib as z
##Done with the includes

## BEGIN ZONE ASSGNMENTS ##
TestRoomReferences = ["room", "area", "surroundings", "zone",]
TestRoomDescription = "a small and uninteresting room. You don't remember how you got here, or even what this place is but you know it's the beginning of something much larger than you."
TestRoomContents = {
    "box" : 1,}
TestRoomExits = {}
TestRoomStructures = ["wall"]
TestRoomNPCs = ["bob"]
TestRoom = z.Zone("Test Room", TestRoomReferences, TestRoomDescription, TestRoomContents, TestRoomExits, False, "none", "Not Locked, this is an error.", "Wasn't locked, this is an error.", False, "No key item, this is an error.", False, "none", "none", TestRoomStructures, TestRoomNPCs)
## END ZONE ASSIGNMENTS ##