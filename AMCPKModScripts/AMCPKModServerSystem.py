# file: ./extracted\c8fe3394_2cfe7e82.pyc
# cracked by asJony
import mod.server.extraServerApi as serverApi
import api
ServerSystem = serverApi.GetServerSystemCls()

class AMCPKModServerSystem(ServerSystem):

    def __init__(self, namespace, systemName):
        super(AMCPKModServerSystem, self).__init__(namespace, systemName)
        print '==== AMCPKModServerSystem Init ===='
        self.ListenForEvent('AMCPKModSMod', 'AMCPKModClientSystem', 'killerEvent', self, self.killerEvent)

    def killerEvent(self, args):
        api.textSay(args['fid'], '尝试杀死' + args['id'])
        comp = serverApi.GetEngineCompFactory().CreateGame(serverApi.GetLevelId())
        comp.KillEntity(args['id'])
