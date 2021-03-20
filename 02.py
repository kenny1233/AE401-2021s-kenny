from mcpi.minecraft import Minecraft
mc=Minecraft.create()
"""
x=248.857
y=100
z=255.678

mc.player.setPos(x,y,z)

x,y,z=mc.player.getTilePos()
mc.player.setTilePos(x,y+100,z)

"""

import time

while True:
    x,y,z=mc.player.getTilePos()
    mc.postToChat("You are located at"+str(x)+","+str(y)+","+str(z))
    time.sleep(1)
    