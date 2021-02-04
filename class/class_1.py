# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 11:36:00 2021

@author: USER
"""
from mcpi.minecraft import Minecraft as mcs
mc = mcs.create()
mc.player.setTilePos(100,100,100)
print(mc.player.getTilePos())
