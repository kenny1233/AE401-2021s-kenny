from mcpi.minecraft import Minecraft

mc=Minecraft.create()

x,y,z=mc.player.getTilePos()
time.sleep(5)
mc.setBlock(x,y,z,8)
time.sleep(5)
mc.setBlock(x,y,z+10,8)
time.sleep(5)
mc.setBlock(x-1,y-1,z-1,169)


mc.setBlock(x+10,y,z,8)

mc.setBlocks(x+3,y,z,x+13,y+10,z+10,1)
mc.setBlocks(x+4,y+1,z+1,x+12,y+9,z+9,z+9,0)

























x,y,z=mc.player.getTilePos()


mc.setBlocks(x+2,y,z,1)
mc.setBlocks(x+2,y,z+2,1)
mc.setBlocks(x+2,y,z-2,1)
mc.setBlocks(x,y,z-2,1)
mc.setBlocks(x-2,y,z-2,1)
mc.setBlocks(x-2,y,z,1)
mc.setBlocks(x-2,y,z+2,1)
mc.setBlocks(x,y,z+2,1)








x,y,z=mc.player.getTilePos()







from mcpi.minecraft import Minecraft
import time
mc=Minecraft.create()

x,y,z=mc.player.getTilePos()

mc.setBlocks(x+3,y,z,x+13,y+10,z+10,1)
mc.setBlocks(x+4,y+1,z+1,x+12,y+9,z+9,z+9,0)







