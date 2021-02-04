# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 09:43:11 2021

@author: USER
"""
from mcpi.minecraft import Minecraft as mcs
mc =mcs.create()
x,y,z = mc.player.getTilePos()
h = 8
w = 8
mc.setBlocks(x+w,y+h,z+w,x,y,z,87)
mc.setBlocks(x+w-1,y+h-1,z+w-1,x+1,y+1,z+1,0)