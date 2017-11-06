import libs.eventLib as e
##Done with the includes

## BEGIN EVENT ASSIGNMENTS ##
testEventActions = {
"PRINT" : "You see the glint of metal through the dust in your eyes."}
testEventOrder = ["PRINT"]
openBoxEvent = e.Event("none", "none", testEventActions, testEventOrder, 1, False, "none")

victoryActions = {
"PRINT" : "You are victorious."}
victory = e.Event("none", "none", victoryActions, testEventOrder, 1, False, "none")

lossActions = {
"PRINT" : "You are defeated."}
loss = e.Event("none", "none", lossActions, testEventOrder, 1, False, "none")
## END EVENT ASSIGNMENTS ##