from mcpi.minecraft import Minecraft
mc=Minecraft.create()



while True:
    x,y,z=mc.player.getTilePos()

    a=mc.getBlock(x,y-1,z)
    b=mc.getBlock(x+1,y-1,z)
    c=mc.getBlock(x,y-1,z+1)
    d=mc.getBlock(x-1,y-1,z)
    e=mc.getBlock(x,y-1,z-1)
    if a==8 or a==9 or c==8 or c==9 or d==8 or d==9 or e==8 or e==9:
        mc.setBlocks(x-1,y-1,z-1,x+1,20)
        
        
        
from mcpi.minecraft import Minecraft
mc=Minecraft.create()
x,y,z=mc.player.getTilePos()

a=0
while a<20:
    mc.setBlocks(x+10,y-1,z,x-10,y-1,z,46)
    z=z-5
    a=a+1
    
        
import time

while True:
    x,y,z=mc.player.getTilePos()
    mc.setBlock(x,y,z,46)
    time.sleep(1)
    
    x,y,z=mc.player.getTilePos()
    mc.setBlock(x,y,z,46)
    time.sleep(1)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        