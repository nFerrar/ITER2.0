from libs import engineLib as engine
from libs.decs.playerDec import Player
from libs.decs import zoneDecs as zones

if __name__ == "__main__":
    print("ITER: The Journey.")
    print("Coming Soon.")
    print("----------")
    print("Type your name to enter the test room.")
    cmd = input(">>>")
    Player.name = cmd
    print("Welcome %s." % (Player.name))
    print("----------")
    engine.ChangeLocation(zones.TestRoom, zones.TestRoom, Player)