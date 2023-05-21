# file: ./extracted\c8fe3394_2dab19cf.pyc
# cracked by asJony
import mod.client.extraClientApi as clientApi
import time
import math
from common.utils.mcmath import Vector3
import CliApi as api
import threading
ui = None
ClientSystem = clientApi.GetClientSystemCls()
maxSpeed = 3.0
fmaxSpeed = -3.0
circleKillSpeed = 150

def get_motion():
    """
    获取玩家移动向量
    """
    comp = clientApi.GetEngineCompFactory().CreateActorMotion(clientApi.GetLocalPlayerId())
    fh = comp.GetInputVector()
    re = tuple(fh)
    return re


def get_rot(entity):
    """
    获取角度
    """
    rot_comp = clientApi.GetEngineCompFactory().CreateRot(entity)
    meRot = rot_comp.GetRot()
    return meRot


def get_pos(entity):
    """
    获取坐标
    """
    pos_comp = clientApi.GetEngineCompFactory().CreatePos(entity)
    myPos = pos_comp.GetPos()
    return myPos


def set_motion(entity, motion):
    """
    移动向量
    """
    motionComp = clientApi.GetEngineCompFactory().CreateActorMotion(entity)
    return motionComp.SetMotion(motion)


def look_pos(entity, pos, boola):
    """
    看向坐标
    """
    comp = clientApi.GetEngineCompFactory().CreateRot(entity)
    return comp.SetPlayerLookAtPos(pos, 999, 999, boola)


def lock_rot(entity, boola):
    """
    锁定角度
    """
    comp = clientApi.GetEngineCompFactory().CreateRot(entity)
    return comp.LockLocalPlayerRot(boola)


def dist(x1, y1, z1, x2, y2, z2):
    """
    运算3维空间距离，返回float
    """
    p = ((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2) ** 0.5
    re = float('%.1f' % p)
    return re


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


def motionPosCount(enemyPos, myPos):
    """
    向量坐标运算
    """
    enemyPos = list(enemyPos)
    myPos = list(myPos)
    for i in range(3):
        Pc_x = (enemyPos[0] - myPos[0]) * 0.496
        Pc_y = (enemyPos[1] - myPos[1]) * 0.496
        Pc_z = (enemyPos[2] - myPos[2]) * 0.496
        Pc = [Pc_x, Pc_y, Pc_z]

    motionPos = tuple(Pc)
    return motionPos


def motionPosCountYadd(enemyPos, myPos, yAdd):
    """
    向量坐标运算，y轴加
    """
    enemyPos = list(enemyPos)
    myPos = list(myPos)
    for i in range(3):
        Pc_x = (enemyPos[0] - myPos[0]) * 0.496
        Pc_y = (enemyPos[1] - myPos[1] + yAdd) * 0.496
        Pc_z = (enemyPos[2] - myPos[2]) * 0.496
        Pc = [Pc_x, Pc_y, Pc_z]

    motionPos = tuple(Pc)
    return motionPos


def getCirclePos(xc, zc, distancec, angle):
    """
    a=input("输入X坐标:")
    b=input("输入Z坐标:")
    c=input("输入距离")
    d=input("输入角度")
    """
    posx = float(xc) + float(distancec) * math.cos(float(angle) * 3.1415926 / 180)
    posz = float(zc) + float(distancec) * math.sin(float(angle) * 3.1415926 / 180)
    return (posx, posz)


def motionPosRectify(mPos):
    """
    向量坐标纠正
    """
    mPos = list(mPos)
    nPos = [1, 1, 1]
    for i in range(3):
        if mPos[i] > maxSpeed:
            nPos[i] = maxSpeed
        elif mPos[i] < fmaxSpeed:
            nPos[i] = fmaxSpeed
        else:
            nPos[i] = mPos[i]

    motionPos = tuple(nPos)
    return motionPos


class AMCPKModClientSystem(ClientSystem):

    def __init__(self, namespace, systemName):
        super(AMCPKModClientSystem, self).__init__(namespace, systemName)
        print '==== AMCPKModClientSystem Init ===='
        self.ListenEvent()
        self.thisPlayer = clientApi.GetLocalPlayerId()
        self.level_id = clientApi.GetLevelId()
        self.ifType = 'minecraft:player'
        self.langw = 5
        self.round_timer = ''
        self.open = False
        self.openlb = False
        self.nota = False
        self.openrd = False
        self.open2 = False
        self.nt = False
        self.tmp = 0
        self.rangle = 0.0
        self.openm = False
        self.openmx = False
        self.openqpx = False
        self.open1x = False
        self.open2x = False
        self.openqp = False
        self.openhb = False
        self.openaj = False
        self.openas = False
        self.ttmmpp = (0, 0)
        self.safePos = ()
        self.show = 0
        self.whiteList = []
        self.cDown = False
        self.UIname = 'MCP'
        self.inCTD = False
        self.alerting = 0
        self.mEntity = '-1'
        self.m2Entity = '-1'
        self.m3Entity = '-1'
        self.m4Entity = '-1'
        self.LockEntity = ''
        self.alerting2 = 0

    def ListenEvent(self):
        self.ListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(), 'ClientJumpButtonPressDownEvent', self, self.ClientJumpButtonPressDownEvent)
        self.ListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(), 'GetEntityByCoordEvent', self, self.GetEntityByCoordEvent)
        self.ListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(), 'OnScriptTickClient', self, self.tick)
        self.ListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(), 'LeftClickBeforeClientEvent', self, self.LeftClickBeforeClientEvent)
        self.ListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(), 'OnKeyPressInGame', self, self.keyDownEvent)
        self.ListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(), 'UiInitFinished', self, self.UiFinish)
        self.ListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(), 'RemovePlayerAOIClientEvent', self, self.RemovePlayerAOIClientEvent)
        self.ListenForEvent('CTD_ScoreboardMod', 'CTD_ScoreboardServerSystem', 'setScoreboard', self, self.setScoreboard)

    def UnListenEvent(self):
        self.UnListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(), 'ClientJumpButtonPressDownEvent', self, self.ClientJumpButtonPressDownEvent)
        self.UnListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(), 'LeftClickBeforeClientEvent', self, self.LeftClickBeforeClientEvent)
        self.UnListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(), 'OnKeyPressInGame', self, self.keyDownEvent)
        self.UnListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(), 'OnScriptTickClient', self, self.tick)
        self.UnListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(), 'UiInitFinished', self, self.UiFinish)
        self.UnListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(), 'RemovePlayerAOIClientEvent', self, self.RemovePlayerAOIClientEvent)

    def setScoreboard(self, args):
        comp = clientApi.GetEngineCompFactory().CreateTextNotifyClient(clientApi.GetLevelId())
        comp.SetLeftCornerNotify('\xa7l\xa7f--------------------------\n\xa7c\xa7l 模式二\n\xa7l\xa7f--------------------------')
        self.langw = 0
        self.inCTD = False

    def RemovePlayerAOIClientEvent(self, args):
        if self.LockEntity == args['playerId'] and self.LockEntity != '':
            enemyPos = get_pos(args['playerId'])
            playerPos = get_pos(self.thisPlayer)
            minDist = dist(enemyPos[0], enemyPos[1], enemyPos[2], playerPos[0], playerPos[1], playerPos[2])
            if minDist <= 2.5:
                look_pos(self.thisPlayer, enemyPos, False)
                lock_rot(self.thisPlayer, False)
                self.alert('\xa7a玩家已阵亡')

    def UiFinish(self, args):
        global ui
        print 'UIFinish'
        clientApi.RegisterUI('AMCPKModSMod', self.UIname, 'AMCPKModScripts.UI.screen.Screen', self.UIname + '.main')
        self.UINode = clientApi.CreateUI('AMCPKModSMod', self.UIname, {'isHud': 1})
        self.UINode = clientApi.GetUI('AMCPKModSMod', self.UIname)
        self.UINode.Init()
        ui = clientApi.GetUI('AMCPKModSMod', self.UIname)
        platform = clientApi.GetPlatform()
        if platform == 0:
            api.sText(ui, '/label0', 'AMCPK PC')
            api.sVisible(ui, '/button', True)
            api.sVisible(ui, '/button1', False)
            api.sVisible(ui, '/button2', False)
            api.sVisible(ui, '/button3', False)
            api.sVisible(ui, '/button4', False)
            api.sVisible(ui, '/button5', False)
            api.sVisible(ui, '/button6', False)
            api.sVisible(ui, '/button7', False)
            api.sVisible(ui, '/button8', False)
            api.sVisible(ui, '/button9', False)
            api.sVisible(ui, '/button10', False)
            api.sVisible(ui, '/button11', False)
            api.sVisible(ui, '/button12', False)
            api.sVisible(ui, '/button13', False)
            api.sVisible(ui, '/button14', False)
            api.sVisible(ui, '/button15', False)
            api.sVisible(ui, '/button16', False)
        else:
            api.sText(ui, '/label0', 'AMCPK PE')
            api.sVisible(ui, '/button', True)
            api.sVisible(ui, '/button1', False)
            api.sVisible(ui, '/button2', False)
            api.sVisible(ui, '/button3', False)
            api.sVisible(ui, '/button4', False)
            api.sVisible(ui, '/button5', False)
            api.sVisible(ui, '/button6', False)
            api.sVisible(ui, '/button7', False)
            api.sVisible(ui, '/button8', False)
            api.sVisible(ui, '/button9', False)
            api.sVisible(ui, '/button10', False)
            api.sVisible(ui, '/button11', False)
            api.sVisible(ui, '/button12', False)
            api.sVisible(ui, '/button13', False)
            api.sVisible(ui, '/button14', False)
            api.sVisible(ui, '/button15', False)
            api.sVisible(ui, '/button16', False)
        api.sItem(ui, '/bg/item0', 'minecraft:skull', 3)
        api.sItem(ui, '/item1', 'minecraft:compass', 3)
        api.sVisible(ui, '/item1', True)
        api.sVisible(ui, '/bg2', False)
        api.sVisible(ui, '/bg', False)
        comp = clientApi.GetEngineCompFactory().CreateTextNotifyClient(clientApi.GetLevelId())
        comp.SetLeftCornerNotify('                                                  ')
        comp.SetLeftCornerNotify('                                                  ')
        comp.SetLeftCornerNotify('                                                  ')
        comp.SetLeftCornerNotify('                                                  ')
        comp.SetLeftCornerNotify('                                                  ')
        comp.SetLeftCornerNotify('                                                  ')
        comp.SetLeftCornerNotify('                                                  ')
        comp.SetLeftCornerNotify('                                                  ')
        comp.SetLeftCornerNotify('                                                  ')
        comp.SetLeftCornerNotify('                                                  ')
        comp.SetLeftCornerNotify('                                                  ')
        comp.SetLeftCornerNotify('                                                  ')
        comp.SetLeftCornerNotify('                                                  ')
        comp.SetLeftCornerNotify('                                                  ')
        comp.SetLeftCornerNotify('                                                  ')
        comp.SetLeftCornerNotify('                                                  ')
        comp.SetLeftCornerNotify('\xa7l\xa7e>>----------------------------------')
        comp.SetLeftCornerNotify('\xa7l\xa7e>>      \xa7r\xa7a Welcome to AMCPK\xa7l\xa7e      ')
        if platform == 0:
            comp = clientApi.GetEngineCompFactory().CreateTextNotifyClient(clientApi.GetLevelId())
            comp.SetLeftCornerNotify('\xa7l\xa7e>>      \xa7r\xa7a 快捷键：            ')
            comp.SetLeftCornerNotify('\xa7l\xa7e>>      \xa7r\xa7a R：选择       Y：自动瞄准\xa7l\xa7e      ')
            comp.SetLeftCornerNotify('\xa7l\xa7e>>      \xa7r\xa7a F：冲刺杀戮   G：锁背\xa7l\xa7e      ')
            comp.SetLeftCornerNotify('\xa7l\xa7e>>      \xa7r\xa7a H：环绕       J：骑人\xa7l\xa7e      ')
            comp.SetLeftCornerNotify('\xa7l\xa7e>>      \xa7r\xa7a X：手动备选   C：冲刺\xa7l\xa7e      ')
            comp.SetLeftCornerNotify('\xa7l\xa7e>>      \xa7r\xa7a V：高跳       B：喷气背包\xa7l\xa7e      ')
            comp.SetLeftCornerNotify('\xa7l\xa7e>>      \xa7r\xa7a Tab：虚空拉回\xa7l\xa7e      ')
            comp.SetLeftCornerNotify('\xa7l\xa7e>>      \xa7r\xa7a 功能菜单位于屏幕左上角\xa7l\xa7e      ')
            comp.SetLeftCornerNotify('\xa7l\xa7e>>----------------------------------')
        else:
            comp = clientApi.GetEngineCompFactory().CreateTextNotifyClient(clientApi.GetLevelId())
            comp.SetLeftCornerNotify('\xa7l\xa7e>>      \xa7r\xa7a 功能菜单位于屏幕左上角\xa7l\xa7e      ')
            comp.SetLeftCornerNotify('\xa7l\xa7e>>----------------------------------')
        self.alert('\xa7aUI 加载完成')

    def alert(self, text):
        api.sVisible(ui, '/bg2', True)
        api.sText(ui, '/bg2/text', text)
        self.alerting = 60

    def alert2(self, playerId):
        api.sVisible(ui, '/bg', True)
        api.sText(ui, '/bg/id', '玩家ID: ' + playerId)
        comp = clientApi.GetEngineCompFactory().CreateAttr(playerId)
        progressBarPath = '/bg/Hp'
        progressBarUIControl = ui.GetBaseUIControl(progressBarPath).asProgressBar()
        progressBarUIControl.SetValue(comp.GetAttrValue(0) / float(comp.GetAttrMaxValue(0)))
        api.sText(ui, '/bg/hp', str(round(comp.GetAttrValue(0), 2)) + 'HP')
        if self.alerting2 > 1 and self.alerting2 <= 43:
            self.alerting2 = 42
        elif self.alerting2 <= 1:
            self.alerting2 = 50

    def rideplayer_func(self):
        """
        //需要坐标 y+2
        //(需要坐标(敌人坐标)-我方坐标)*0.496
        //向量坐标纠正
        """
        myPos = get_pos(self.thisPlayer)
        nPos = ()
        if self.mEntity != '-1':
            entity = self.mEntity
            comp = clientApi.GetEngineCompFactory().CreateEngineType(entity)
            strType = comp.GetEngineTypeStr()
            strid = str(entity)
            strlang = len(strid)
            if strType == self.ifType and strlang > self.langw and entity not in self.whiteList:
                nePos = get_pos(entity)
                mPos = motionPosCountYadd(nePos, myPos, 2.0)
                nPos = motionPosRectify(mPos)
                set_motion(self.thisPlayer, nPos)

    def lockback_func(self):
        """
        //敌人坐标，函数获取需要坐标
        //(需要坐标-我方坐标)*0.496
        //向量坐标纠正
        //设置向量，设置自瞄
        """
        myPos = get_pos(self.thisPlayer)
        nePos = ()
        if self.mEntity != '':
            entity = self.mEntity
            comp = clientApi.GetEngineCompFactory().CreateEngineType(entity)
            strType = comp.GetEngineTypeStr()
            strid = str(entity)
            strlang = len(strid)
            if strType == self.ifType and strlang > self.langw and entity not in self.whiteList:
                mePos = get_pos(entity)
                meRot = get_rot(entity)
                neRot = meRot[1] - 90
                nePos_x, nePos_z = getCirclePos(mePos[0], mePos[2], 2, neRot)
                nePos = (nePos_x, mePos[1], nePos_z)
                mPos = motionPosCountYadd(nePos, myPos, 1.0)
                nPos = motionPosRectify(mPos)
                set_motion(self.thisPlayer, nPos)

    def round_func(self):
        """
        角度+0.2*circleKillSpeed
        大于359设置0
        getCirclePos(敌方x，z, 3 ,角度)
        向量运算
        向量纠正
        环绕
        """
        for i in range(128):
            if self.openrd:
                if self.rangle > 359.0:
                    self.rangle = 0.0
                self.rangle = self.rangle + 0.2
                rangle = self.rangle
                myPos = get_pos(self.thisPlayer)
                nePos = ()
                if self.mEntity != '':
                    entity = self.mEntity
                    comp = clientApi.GetEngineCompFactory().CreateEngineType(entity)
                    strType = comp.GetEngineTypeStr()
                    strid = str(entity)
                    strlang = len(strid)
                    if strType == self.ifType and strlang > self.langw and entity not in self.whiteList:
                        mePos = get_pos(entity)
                        nePos_x, nePos_z = getCirclePos(mePos[0], mePos[2], 2, rangle)
                        nePos = (nePos_x, mePos[1], nePos_z)
                        mPos = motionPosCountYadd(nePos, myPos, 1.0)
                        nPos = motionPosRectify(mPos)
                        set_motion(self.thisPlayer, nPos)

    def autoaiming_func(self):
        minDist = 999
        minPos = ()
        if self.mEntity != '':
            entity = self.mEntity
            comp = clientApi.GetEngineCompFactory().CreateEngineType(entity)
            strType = comp.GetEngineTypeStr()
            strid = str(entity)
            strlang = len(strid)
            if strType == self.ifType and strlang > self.langw and entity != self.thisPlayer and entity not in self.whiteList:
                enemyPos = get_pos(entity)
                minPos = enemyPos
                look_pos(self.thisPlayer, minPos, True)

    def tick(self):
        if self.openm:
            self.autoaiming_func()
        if self.openqp:
            for i in range(16):
                self.rideplayer_func()

        if self.openlb:
            for i in range(16):
                self.lockback_func()

        if self.openmx == True and self.open2 == True:
            self.mEntity = self.LockEntity
            if self.mEntity != '' and self.mEntity != '-1' and self.m2Entity != self.mEntity:
                self.alert('已锁定：' + self.mEntity)
                self.openmx = False
            self.m2Entity = self.mEntity
        if self.nota == True:
            comp = clientApi.GetEngineCompFactory().CreateCamera(self.level_id)
            self.mEntity = comp.GetChosenEntity()
            if self.mEntity != '' and self.mEntity != '-1' and self.m2Entity != self.mEntity:
                self.alert('已锁定：' + self.mEntity)
                self.nota = False
            self.m2Entity = self.mEntity
        if self.nt:
            localPlayerId = clientApi.GetLocalPlayerId()
            rot = get_rot(localPlayerId)
            x, y, z = clientApi.GetDirFromRot(rot)
            set_motion(self.thisPlayer, (x * 1.3, y * 1.3, z * 1.3))
            self.nt = False
        if self.alerting > 0:
            self.alerting -= 1
            if self.alerting >= 53:
                api.sAlpha(ui, '/bg2/text', 0.5 + (60 - self.alerting) / 20.0)
                api.sAlpha(ui, '/bg2', (60 - self.alerting) / 10.0)
            elif self.alerting <= 7:
                api.sAlpha(ui, '/bg2/text', 0.5 + self.alerting / 20.0)
                api.sAlpha(ui, '/bg2', self.alerting / 10.0)
            if self.alerting == 0:
                api.sVisible(ui, '/bg2', False)
        if self.alerting2 > 0:
            self.alerting2 -= 1
            if self.alerting2 >= 43:
                print (50 - self.alerting2) / 10.0
                api.sAlpha(ui, '/bg/id', 0.5 + (50 - self.alerting2) / 20.0)
                api.sAlpha(ui, '/bg/item0', 0.5 + (50 - self.alerting2) / 20.0)
                api.sAlpha(ui, '/bg/hp', 0.5 + (50 - self.alerting2) / 20.0)
                api.sAlpha(ui, '/bg/Hp', 0.5 + (50 - self.alerting2) / 20.0)
                api.sAlpha(ui, '/bg', (50 - self.alerting2) / 10.0)
            elif self.alerting2 <= 7:
                api.sAlpha(ui, '/bg/id', 0.7 + self.alerting2 / 20.0)
                api.sAlpha(ui, '/bg/item0', 0.7 + self.alerting2 / 20.0)
                api.sAlpha(ui, '/bg/Hp', 0.7 + self.alerting2 / 20.0)
                api.sAlpha(ui, '/bg/hp', 0.7 + self.alerting2 / 20.0)
                api.sAlpha(ui, '/bg', self.alerting2 / 10.0)
            if self.alerting2 == 0:
                api.sVisible(ui, '/bg', False)
        if self.show >= 0:
            self.show -= 1
        self.tmp += 1
        if self.tmp >= 3333:
            self.tmp = 0
        if self.tmp % 30 == 0 and self.show <= 0:
            localPlayerId = clientApi.GetLocalPlayerId()
            comp = clientApi.GetEngineCompFactory().CreateAttr(localPlayerId)
            now = comp.GetAttrValue(clientApi.GetMinecraftEnum().AttrType.HEALTH)
            Max = comp.GetAttrMaxValue(clientApi.GetMinecraftEnum().AttrType.HEALTH)
            other = Max - now
            self.ttmmpp = (now, other)
            api.sText(ui, '/label3', str(round(comp.GetAttrValue(0), 2)) + 'HP')
            progressBarPath = '/selfHp'
            progressBarUIControl = ui.GetBaseUIControl(progressBarPath).asProgressBar()
            progressBarUIControl.SetValue(comp.GetAttrValue(0) / float(comp.GetAttrMaxValue(0)))
        if self.tmp % 3 == 0:
            localPlayerId = clientApi.GetLocalPlayerId()
            comp = clientApi.GetEngineCompFactory().CreateAttr(localPlayerId)
            now = comp.GetAttrValue(clientApi.GetMinecraftEnum().AttrType.HEALTH)
            comp = clientApi.GetEngineCompFactory().CreateAttr(localPlayerId)
            Max = comp.GetAttrMaxValue(clientApi.GetMinecraftEnum().AttrType.HEALTH)
            other = Max - now
            if (now, other) != self.ttmmpp:
                text = '\xa7c-{}HP'.format(str(round(self.ttmmpp[0] - now, 2)))
                if self.ttmmpp[0] < int(now):
                    text = '\xa7a+{}HP'.format(str(round(now - self.ttmmpp[0], 2)))
                self.ttmmpp = (now, other)
                api.sText(ui, '/label3', str(round(comp.GetAttrValue(0), 2)) + 'HP   ' + text)
                progressBarPath = '/selfHp'
                progressBarUIControl = ui.GetBaseUIControl(progressBarPath).asProgressBar()
                progressBarUIControl.SetValue(comp.GetAttrValue(0) / float(comp.GetAttrMaxValue(0)))
                self.show = 66
            comp = clientApi.GetEngineCompFactory().CreatePos(self.thisPlayer)
            playerPos = comp.GetFootPos()
            playerPos = list(playerPos)
            playerPos[1] -= 1
            playerPos = tuple(playerPos)
            comp = clientApi.GetEngineCompFactory().CreateBlockInfo(clientApi.GetLevelId())
            footBlock = comp.GetBlock(blockPosChange(playerPos))[0]
            if 'air' not in footBlock:
                self.safePos = playerPos
        if self.tmp % 3 == 0:
            if self.cDown:
                localPlayerId = clientApi.GetLocalPlayerId()
                rot = get_rot(localPlayerId)
                x, y, z = clientApi.GetDirFromRot(rot)
                set_motion(localPlayerId, (x, y, z))

    def GetEntityByCoordEvent(self, args):
        self.LeftClickBeforeClientEvent({})

    def LeftClickBeforeClientEvent(self, args):
        if self.open:
            playerPos = get_pos(self.thisPlayer)
            comp = clientApi.GetEngineCompFactory().CreateGame(clientApi.GetLevelId())
            entities = comp.GetEntityInArea(self.thisPlayer, (playerPos[0] - 10, playerPos[1] - 10, playerPos[2] - 10), (playerPos[0] + 10, playerPos[1] + 10, playerPos[2] + 10))
            minDist = 999
            minPos = ()
            minEntity = ''
            for entity in entities:
                comp = clientApi.GetEngineCompFactory().CreateEngineType(entity)
                strType = comp.GetEngineTypeStr()
                strid = str(entity)
                strlang = len(strid)
                if strType == self.ifType and strlang > self.langw and entity != self.thisPlayer and entity not in self.whiteList:
                    enemyPos = get_pos(entity)
                    if dist(enemyPos[0], enemyPos[1], enemyPos[2], playerPos[0], playerPos[1], playerPos[2]) < minDist:
                        minDist = dist(enemyPos[0], enemyPos[1], enemyPos[2], playerPos[0], playerPos[1], playerPos[2])
                        minPos = enemyPos
                        minEntity = entity

            lock_rot(self.thisPlayer, False)
            look_pos(self.thisPlayer, minPos, True)
            lock_rot(self.thisPlayer, True)
            if minEntity != '':
                if self.LockEntity != minDist:
                    self.alert('\xa7l\xa7e>>  \xa7fAt Player:' + minEntity + '\xa7l\xa7e  <<')
                self.nt = False
                self.alert2(minEntity)
            if minEntity != '' and minDist >= 2.5 and minDist <= 6:
                self.alert('\xa7l\xa7e>>  \xa7fTo Player:' + minEntity + '\xa7l\xa7e  <<')
                lock_rot(self.thisPlayer, True)
                self.nt = True
            elif minEntity != '' and minDist > 6:
                lock_rot(self.thisPlayer, False)
                self.nt = True
            elif minEntity != '':
                self.LockEntity = minEntity
                lock_rot(self.thisPlayer, False)
                self.nt = False
        if self.openlb == True or self.openrd == True:
            if self.LockEntity != '' and self.LockEntity != '-1':
                pos = get_pos(self.LockEntity)
                look_pos(self.thisPlayer, pos, True)
        if self.open2:
            playerPos = get_pos(self.thisPlayer)
            comp = clientApi.GetEngineCompFactory().CreateGame(clientApi.GetLevelId())
            entities = comp.GetEntityInArea(self.thisPlayer, (playerPos[0] - 10, playerPos[1] - 10, playerPos[2] - 10), (playerPos[0] + 10, playerPos[1] + 10, playerPos[2] + 10))
            minDist = 999
            minPos = ()
            minEntity = ''
            for entity in entities:
                comp = clientApi.GetEngineCompFactory().CreateEngineType(entity)
                strType = comp.GetEngineTypeStr()
                strid = str(entity)
                strlang = len(strid)
                if strType == self.ifType and strlang > self.langw and entity != self.thisPlayer and entity not in self.whiteList:
                    enemyPos = get_pos(entity)
                    if dist(enemyPos[0], enemyPos[1], enemyPos[2], playerPos[0], playerPos[1], playerPos[2]) < minDist:
                        minDist = dist(enemyPos[0], enemyPos[1], enemyPos[2], playerPos[0], playerPos[1], playerPos[2])
                        minPos = enemyPos
                        minEntity = entity

            if minEntity != '':
                self.nt = False
                self.alert2(minEntity)
                self.LockEntity = minEntity
                comp = clientApi.GetEngineCompFactory().CreateAttr(self.LockEntity)
                nowh = comp.GetAttrValue(clientApi.GetMinecraftEnum().AttrType.HEALTH)
            if minEntity != '' and nowh <= 1:
                lock_rot(self.thisPlayer, False)
                self.LockEntity = ''
                self.openmx = False

                def func():
                    self.openmx = True

                comp = clientApi.GetEngineCompFactory().CreateGame(clientApi.GetLocalPlayerId())
                comp.AddTimer(0.4, func)
            if minEntity != '' and minDist >= 4.5:
                lock_rot(self.thisPlayer, False)
                self.LockEntity = ''
                self.openmx = True
            if minEntity == '' or minEntity == '-1':
                lock_rot(self.thisPlayer, False)
                self.openmx = True
            else:
                self.LockEntity = minEntity
            Lockbool = False
            entities = comp.GetEntityInArea(self.thisPlayer, (playerPos[0] - 10, playerPos[1] - 10, playerPos[2] - 10), (playerPos[0] + 10, playerPos[1] + 10, playerPos[2] + 10))
            for entity in entities:
                if entity == self.LockEntity and entity != self.thisPlayer and entity not in self.whiteList:
                    Lockbool = True

            if Lockbool == False:
                self.LockEntity = ''
                lock_rot(self.thisPlayer, False)
                self.openmx = True
            else:
                self.LockEntity = minEntity
                if self.openrd:
                    self.openrd = False

                    def funcs():
                        self.openrd = True

                    comp = clientApi.GetEngineCompFactory().CreateGame(clientApi.GetLocalPlayerId())
                    comp.AddTimer(0.4, funcs)

    def keyDownEvent(self, args):
        if self.inCTD:
            return
        if args['key'] in ('70'):
            if args['isDown'] == '1' and self.open == False:
                self.open = True
                comp = clientApi.GetEngineCompFactory().CreateCamera(clientApi.GetLevelId())
                comp.DepartCamera()
                lock_rot(self.thisPlayer, True)
                self.alert('\xa7a\xa7l冲刺杀戮已开启')
            elif args['isDown'] == '1' and self.open == True:
                self.open = False
                comp = clientApi.GetEngineCompFactory().CreateCamera(clientApi.GetLevelId())
                comp.UnDepartCamera()
                lock_rot(self.thisPlayer, False)
                self.alert('\xa7c\xa7l冲刺杀戮已关闭')
        if args['key'] == '66':
            if args['isDown'] == '1':
                self.cDown = True
                self.alert('\xa7a\xa7l喷气背包已开启')
            else:
                self.cDown = False
                self.alert('\xa7c\xa7l喷气背包已关闭')
        if args['key'] == '67' and args['isDown'] == '1':
            self.fly()
        if args['key'] == '9' and args['isDown'] == '1':
            self.bugup()
        if args['key'] == '80' and args['isDown'] == '1':
            self.tag()
        if args['key'] == '86' and args['isDown'] == '1':
            self.jump()
        if args['key'] == '88' and args['isDown'] == '1':
            self.notauto()
        if args['key'] == '82' and args['isDown'] == '1':
            self.detach()
        if args['key'] == '71' and args['isDown'] == '1':
            self.lockback()
        if args['key'] == '72' and args['isDown'] == '1':
            self.round()
        if args['key'] == '74' and args['isDown'] == '1':
            self.rideplayer()
        if args['key'] == '89' and args['isDown'] == '1':
            self.autoaiming()
        if args['key'] in ('87'):
            if args['isDown'] == '1' and self.openas == True:
                comp = clientApi.GetEngineCompFactory().CreateActorMotion(clientApi.GetLocalPlayerId())
                comp.BeginSprinting()
            elif args['isDown'] == '0' and self.openas == True:
                comp = clientApi.GetEngineCompFactory().CreateActorMotion(clientApi.GetLocalPlayerId())
                comp.EndSprinting()

    def ClientJumpButtonPressDownEvent(self, args):
        if self.openaj == True:
            comp = clientApi.GetEngineCompFactory().CreateAttr(clientApi.GetLocalPlayerId())
            isOnGound = comp.isEntityOnGround()
            if isOnGound == False:
                set_motion(self.thisPlayer, (0, 0.6, 0))

    def jump(self):
        set_motion(self.thisPlayer, (0, 1.2, 0))
        self.alert('\xa7b\xa7l高跳')

    def detach(self):
        if self.open2 == False:
            self.openmx = True
            self.open2 = True
            player = clientApi.GetLocalPlayerId()
            comp = clientApi.GetEngineCompFactory().CreateActorCollidable(player)
            success = comp.SetActorCollidable(1)
            self.alert('\xa7a\xa7l选择模式')
        elif self.open2 == True:
            self.openmx = False
            self.open2 = False
            self.LockEntity = ''
            self.mEntity = ''
            player = clientApi.GetLocalPlayerId()
            comp = clientApi.GetEngineCompFactory().CreateActorCollidable(player)
            success = comp.SetActorCollidable(0)
            self.LockEntity = ''
            self.alert('\xa7c\xa7l脱离模式')

    def notauto(self):
        if self.nota == False:
            self.nota = True
            player = clientApi.GetLocalPlayerId()
            comp = clientApi.GetEngineCompFactory().CreateActorCollidable(player)
            success = comp.SetActorCollidable(1)
            self.alert('\xa7a\xa7l手动备选模式')
        elif self.nota == True:
            self.nota = False
            self.LockEntity = ''
            self.mEntity = ''
            player = clientApi.GetLocalPlayerId()
            comp = clientApi.GetEngineCompFactory().CreateActorCollidable(player)
            success = comp.SetActorCollidable(0)
            self.LockEntity = ''
            self.alert('\xa7c\xa7l手动选择关闭(脱离)')

    def ecgame(self):
        if self.langw == 5:
            self.langw = 0
            player = clientApi.GetLocalPlayerId()
            comp = clientApi.GetEngineCompFactory().CreateActorCollidable(player)
            success = comp.SetActorCollidable(0)
            self.alert('\xa7a\xa7lEC模式')
        elif self.langw == 0:
            self.langw = 5
            player = clientApi.GetLocalPlayerId()
            comp = clientApi.GetEngineCompFactory().CreateActorCollidable(player)
            success = comp.SetActorCollidable(1)
            self.alert('\xa7c\xa7l其他服模式')

    def autoaiming(self):
        if self.openm == True:
            self.alert('\xa7c\xa7l自瞄已关闭')
            self.openm = False
        elif self.openm == False:
            self.alert('\xa7a\xa7l自瞄已开启')
            self.openm = True

    def rideplayer(self):
        self.openrd = False
        self.openlb = False
        if self.openqp == False:
            self.alert('\xa7a\xa7l骑人已开启')
            self.openqp = True
        elif self.openqp == True:
            self.alert('\xa7c\xa7l骑人已关闭')
            self.openqp = False

    def killarua(self):
        if self.open == False:
            self.alert('\xa7a\xa7l冲刺杀戮已开启')
            self.open = True
            comp = clientApi.GetEngineCompFactory().CreateCamera(clientApi.GetLevelId())
            comp.DepartCamera()
            lock_rot(self.thisPlayer, True)
        elif self.open == True:
            self.alert('\xa7c\xa7l冲刺杀戮已关闭')
            self.open = False
            comp = clientApi.GetEngineCompFactory().CreateCamera(clientApi.GetLevelId())
            comp.UnDepartCamera()
            lock_rot(self.thisPlayer, False)

    def lockback(self):
        self.openrd = False
        self.openqp = False
        if self.openlb == False:
            self.alert('\xa7a\xa7l锁背已开启')
            self.openlb = True
        elif self.openlb == True:
            self.alert('\xa7c\xa7l锁背已关闭')
            self.openlb = False

    def round(self):
        self.openlb = False
        self.openqp = False
        comp = clientApi.GetEngineCompFactory().CreateGame(self.level_id)
        if self.openrd == False:
            self.alert('\xa7a\xa7l环绕已开启')
            self.openrd = True
            self.round_timer = comp.AddRepeatedTimer(1e-31, self.round_func)
        elif self.openrd == True:
            self.alert('\xa7c\xa7l环绕已关闭')
            self.openrd = False
            comp.CancelTimer(self.round_timer)

    def bugup(self):
        comp = clientApi.GetEngineCompFactory().CreateAttr(clientApi.GetLocalPlayerId())
        isOnGound = comp.isEntityOnGround()
        if isOnGound == False:
            self.alert('\xa7e\xa7l虚空拉回')
            comp = clientApi.CreateComponent(clientApi.GetLocalPlayerId(), 'Minecraft', 'pos')
            entityFootPos = comp.GetFootPos()
            posVec = Vector3(entityFootPos)
            vec2 = Vector3(self.safePos)
            tup = (vec2 - posVec).Normalized().ToTuple()
            set_motion(self.thisPlayer, (0, tup[1] + 0.6, 0))

            def func(tup):
                set_motion(self.thisPlayer, (tup[0], 0.1, tup[2]))

            comp = clientApi.GetEngineCompFactory().CreateGame(clientApi.GetLocalPlayerId())
            comp.AddTimer(0.4, func, tup)

    def fly(self):
        self.alert('\xa7b\xa7l冲刺')
        localPlayerId = clientApi.GetLocalPlayerId()
        comp = clientApi.GetEngineCompFactory().CreatePlayer(localPlayerId)
        comp.isGliding()
        rot = get_rot(localPlayerId)
        x, y, z = clientApi.GetDirFromRot(rot)
        set_motion(self.thisPlayer, (x * 4.6, y * 4.6, z * 4.6))

    def tag(self):
        self.whiteList = []
        playerPos = get_pos(self.thisPlayer)
        comp = clientApi.GetEngineCompFactory().CreateGame(clientApi.GetLevelId())
        entities = comp.GetEntityInArea(self.thisPlayer, (playerPos[0] - 10, playerPos[1] - 10, playerPos[2] - 10), (playerPos[0] + 10, playerPos[1] + 10, playerPos[2] + 10))
        for entity in entities:
            comp = clientApi.GetEngineCompFactory().CreateEngineType(entity)
            strType = comp.GetEngineTypeStr()
            if strType == self.ifType and entity != self.thisPlayer:
                self.whiteList.append(entity)

        self.alert('\xa7d\xa7l白名单：\xa76{}\xa7d\xa7l人'.format(str(len(self.whiteList))))

    def showhealthbar(self):
        if self.openhb == False:
            self.alert('\xa7a\xa7l血量显示已开启')
            comp = clientApi.GetEngineCompFactory().CreateGame(clientApi.GetLevelId())
            comp.ShowHealthBar(True)
            self.openhb = True
        elif self.openhb == True:
            self.alert('\xa7c\xa7l血量显示已关闭')
            comp = clientApi.GetEngineCompFactory().CreateGame(clientApi.GetLevelId())
            comp.ShowHealthBar(False)
            self.openhb = False

    def airjump(self):
        if self.openaj == False:
            self.alert('\xa7a\xa7l踏空已开启')
            self.openaj = True
        elif self.openaj == True:
            self.alert('\xa7c\xa7l踏空已关闭')
            self.openaj = False

    def jetpack(self):
        if self.cDown == False:
            self.alert('\xa7a\xa7l喷气背包已开启')
            self.cDown = True
        elif self.cDown == True:
            self.alert('\xa7c\xa7l喷气背包已关闭')
            self.cDown = False

    def autosprint(self):
        if self.openas == False:
            self.alert('\xa7a\xa7l自动疾跑已开启')
            self.openas = True
        elif self.openas == True:
            self.alert('\xa7c\xa7l自动疾跑已关闭')
            self.openas = False

    def Destroy(self):
        self.UnListenEvent()
