# file: ./extracted\c8fe3394_a458ab05.pyc
# cracked by asJony
import mod.server.extraServerApi as serverApi
import datetime
import random
import math
comp = serverApi.GetEngineCompFactory().CreateCommand(serverApi.GetLevelId())
compt = serverApi.GetEngineCompFactory().CreateGame(serverApi.GetLevelId())

def getName(entityId):
    """
    使用生物ID，返回其名称
    """
    compn = serverApi.GetEngineCompFactory().CreateName(entityId)
    return compn.GetName()


def goCommand(string):
    """
    使用命令，返回bool表示是否成功
    """
    success = comp.SetCommand(string)
    return success


def goCommands(string, playerId):
    """
    让某个玩家使用命令，返回bool表示是否成功
    """
    success = comp.SetCommand(string, playerId, False)
    return success


def setInterval(time, func):
    """
    延迟执行函数
    """
    compt.AddTimer(time, func)


def sneaking(playerId):
    """
    玩家是否正在潜行，返回bool
    """
    compsn = serverApi.GetEngineCompFactory().CreatePlayer(playerId)
    is_sneaking = compsn.IsSneaking()
    return is_sneaking


def dist(x1, y1, z1, x2, y2, z2):
    """
    运算3维空间距离，返回float
    """
    p = ((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2) ** 0.5
    re = float('%.1f' % p)
    return re


def getPos(playerId):
    """
    获取玩家位置，返回元组
    """
    compo = serverApi.GetEngineCompFactory().CreatePos(playerId)
    pos = compo.GetPos()
    return pos


def handUsing(playerId, itemName):
    """
    玩家是否手持某种物品，返回bool
    """
    compb = serverApi.GetEngineCompFactory().CreateItem(playerId)
    itemDict = compb.GetPlayerItem(serverApi.GetMinecraftEnum().ItemPosType.CARRIED, 0)
    if itemDict is not None:
        if itemDict['itemName'] == 'minecraft:' + itemName:
            return True
        else:
            return False
    else:
        return False


def textSay(playerId, text):
    """
    给某位玩家发送聊天栏消息
    """
    comps = serverApi.GetEngineCompFactory().CreateMsg(serverApi.GetLevelId())
    comps.NotifyOneMessage(playerId, text, '')


def textSayAll(text):
    """
    给全部玩家发送聊天栏消息
    """
    comps = serverApi.GetEngineCompFactory().CreateMsg(serverApi.GetLevelId())
    for playerId in playerList():
        comps.NotifyOneMessage(playerId, text, '')


def getOperation(playerId):
    """
    获取玩家权限,Visitor为0，Member为1，Operator为2，Custom为3
    """
    comppp = serverApi.GetEngineCompFactory().CreatePlayer(playerId)
    operation = comppp.GetPlayerOperation()
    return operation


def playerList():
    return serverApi.GetPlayerList()


def getBlock(x, y, z):
    """
    使用坐标，返回坐标的方块字典
    """
    compbb = serverApi.GetEngineCompFactory().CreateBlockInfo(serverApi.GetLevelId())
    blockDict = compbb.GetBlockNew((x, y, z), 0)
    return blockDict


def setBlock(x, y, z, name, aux):
    """
    在一个位置放置方块
    """
    goCommand('/setblock ' + str(x) + ' ' + str(y) + ' ' + str(z) + ' ' + name + ' ' + str(aux))


def blockPosChange(pos):
    """
    实体坐标转方块坐标
    """
    pos = list(pos)
    for i in range(3):
        if int(pos[i]) > 0:
            pos[i] = int(pos[i])
        else:
            pos[i] = math.floor(pos[i])

    pos = tuple(pos)
    return pos


def getLight(playerId):
    """
    获取玩家所处位置的光照度
    """
    pos = getPos(playerId)
    pos = blockPosChange(pos)
    comp = serverApi.GetEngineCompFactory().CreateBlockInfo(playerId)
    lightlevel = comp.GetBlockLightLevel(pos)
    return lightlevel


def direction(x1, y1, x2, y2):
    """
    运算(x2,y2)相对于(x1,y1)的角度
    """

    def tan(num):
        return math.atan(num) * 180 / math.pi

    try:
        a = tan(float(abs(y1 - y2)) / float(abs(x1 - x2)))
    except:
        a = 0

    if x2 > x1 and y2 > y1:
        return 90 - a
    if x2 > x1 and y2 < y1:
        return 90 + a
    if x2 < x1 and y2 < y1:
        return 270 - a
    if x2 < x1 and y2 > y1:
        return 270 + a
    if x2 == x1 and y2 > y1:
        return 0
    if x2 == x1 and y2 < y1:
        return 180
    if x2 < x1 and y2 == y1:
        return 270
    if x2 > x1 and y2 == y1:
        return 90
