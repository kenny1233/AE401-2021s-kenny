from mcpi.minecraft import Minecraft
mc=Minecraft.create()
import random

x,y,z=mc.player.getTilePos()

for i in range(20):
    r=random.randrange(1,5)
    
    if r==1:
        mc.setBlocks(x,y,z,x+4,y,z,57)
        x+=4
    elif r==2:
        mc.setBlocks(x,y,z,x-4,y,z,57)
        x-=4
    elif r == 3:
        mc.setBlocks(x,y,z,x,y,z+4,57)
        z+=4
    elif r==4:
        mc.setBlocks(x,y,z,x,y,z-4,57)
        z-=4
    
    

