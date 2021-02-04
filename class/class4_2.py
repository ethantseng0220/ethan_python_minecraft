from mcpi.minecraft import Minecraft as mcs
import time
mc = mcs.create()
x,y,z=mc.player.getPos()
nuber = 1
e
    time.sleep(1)
    for i in range(nuber):
        mc.spawnEntity(x,y,z,60)
    nuber = nuber * 2
    mc.postToChat(str(nuber))