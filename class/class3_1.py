from mcpi.minecraft import Minecraft as mcs
mc =mcs.create()
while True:
    hits = mc.events.pollBlockHits()
     if len(hits) > 0 :
          hit = hits[0]
          x,y,z = hit.pos.x,hit.pos.y,hit.pos.z
          mc.setBlock(x,y,z,46)

        