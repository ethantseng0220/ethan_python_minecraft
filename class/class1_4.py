# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 15:38:23 2021

@author: USER
"""
from mcpi.minecraft import Minecraft as mcs
import time
mc = mcs.create()
t = 0
while True:
    time.sleep(2)
    mc.postToChat("t = "+str(t))
    t = t+1