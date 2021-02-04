# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 15:52:54 2021

@author: USER
"""
from mcpi.minecraft import Minecraft as mcs
import time
mc = mcs.create()
while True:
    time.sleep(1)
    x,y,z = mc.player.getTilePos()
    mc.postToChat('You are locat on x:'+str(x)+"y:"+str(y)+"z:"+str(z))