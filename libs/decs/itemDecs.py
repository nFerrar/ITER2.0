import libs.itemLib as i

import libs.decs.eventDecs as events
##Done with the includes
## BEGIN ITEM/CONTAINER ASSIGNMENTS ##
key = i.Item("a small key", "a small tarnished key of silver. it looks as though it hasn't been touched in a very long time.", True, False, False, "none error", "none error", True, "none error", "none error")

boxContents = {
"key" : 1,
}
box = i.Container("a box", "a wooden crate, covered in dust. It looks old, and has hinges on the back edge.", False, "an open wooden box, emanating a musty small from it's dark interior.", boxContents, "As you slowly open the box it's hinges give a protesting groan and despite your gentle motions you are surrounded by a plume of dust which slowly settles to the floor.", "You close the box with a creak.", False, False, False, "None, error", "none, error", True, "openContainer", events.openBoxEvent, False, "none", "none", "none", "none", False, "none")
## END ITEM/CONTAINER ASSIGNMENTS ##

## BEGIN ITEM/CONTAINER LIST ##
itemList = ["box"]
## END ITEM/CONTAINER LIST ##