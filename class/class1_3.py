# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 14:36:49 2021

@author: USER
"""

from mcpi.minecraft import Minecraft as mcs
mc = mcs.create()
while True:
    time.sleep(0.5)
    x,y,z = mc.player.getTilePos()
    mc.setBlock(x,y,z,46)
    mc.setBlock(x+1,y,z,152)