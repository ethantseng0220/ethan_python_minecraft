from mcpi.minecraft import Minecraft as mcs
mc = mcs.create()
ID = mc.getPlayerEntityId("easonku")
mc.postToTitle(ID,"hello")