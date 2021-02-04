# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 13:53:13 2021

@author: USER
"""
from mcpi.minecraft import Minecraft as mcs
mc = mcs.create()
x,y,z = mc.player.getTilePos()
mc.setBlock(x,y,z,46)
mc.setBlock(x+1,y,z,152)
