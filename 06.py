from mcpi.minecraft import Minecraft
mc=Minecraft.create()
import time
import random

x,y,z=mc.player.getPos()
mc.setSign(x,y,z,63,15,"20","20","   ","20")

while True:
    hits=mc.events.pollBlockHits()
    if len(hits) >0:
        hit = hits[0]
        x,y,z=hit.pos.x,hit.pos.y,hit.pos.z
        blockid=mc.getBlock(x,y,z)
        print("恭喜你獵到了"+str(blockid))
        
        
        
        
        
while True:
    hits=mc.events.pollBlockHits()
    if len(hits) >0:
        hit = hits[0]
        x,y,z=hit.pos.x,hit.pos.y,hit.pos.z
        mc.setBlocks(x,y,z,57)
        
import time
pos=mc.player.getPos()
while True:
    x=pos.x+random.uniform(20,-20)
    z=pos.z+random.uniform(20,-20)
    y=pos.y+50
    mc.spawnEntity(x,y,z,50)
    time.sleep(0.1)
    
    
    
while True:
    hits=mc.events.pollProjectileHits()
    if len(hits) >0:
        hit = hits[0]
        x,y,z=hit.pos.x,hit.pos.y,hit.pos.z
        mc.createExplosion(x,y,z)
        
        
        
        
        
        
    
    
    
    
    
    
    
    
    
    
    
    
    