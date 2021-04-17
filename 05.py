from mcpi.minecraft import Minecraft
mc=Minecraft.create()

try:
    x,y,z=mc.player.getTilePos()
    blocktype=int(input('請輸入ID:'))
    mc.setBlock(x,y,z,blocktype)
 
except:
    print('bibibi')
    blocktype=int(input('請輸入Id:'))
    mc.setBlock(x,y,z,blocktype)



userName=input("請輸入姓名: ")
message=input('請輸入發言')
mc.postToChat("[" + usertime + "]" +message)


x,y,z=mc.player.getTilePos()
mc.setBlocks(x+3,y,z,x+13,y+10,z+10,1)
mc.setBlocks(x+4,y+1,z+1,x+12,y+9,z+9,z+9,0)


x,y,z=mc.player.getTilePos()


hight=int(input("請輸入高度"))
width= int(input("請輸入寬"))
length=int(innput("請輸入長"))
blockid=int(input("請輸入id"))

mc.setBlocks(x,y,z,x+length-1,y+hight,z+wid-1,blockid)

mc.setBlocks(x+1,y+2,z+1,x+length-2,y+hight-1,z+wid-2,0)
mc.setBlocks(x+2,y+2,z,x+2,y+3,z,0)