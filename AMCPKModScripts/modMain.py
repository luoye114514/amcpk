# file: ./extracted\c8fe3394_d6506f51.pyc
# cracked by asJony
from mod.common.mod import Mod
import mod.server.extraServerApi as serverApi
import mod.client.extraClientApi as clientApi

@Mod.Binding(name='AMCPKModSMod', version='0.0.1')

class AMCPKModSMod(object):

    def __init__(self):
        print '===== init AMCPKMod mod ====='

    @Mod.InitClient()
    def AMCPKModClientInit(self):
        print '===== init hugo fps client ====='
        clientApi.RegisterSystem('AMCPKModSMod', 'AMCPKModClientSystem', 'AMCPKModScripts.AMCPKModClientSystem.AMCPKModClientSystem')

    @Mod.InitServer()
    def AMCPKModServerInit(self):
        print '===== init hugo fps server ====='
        clientApi.RegisterSystem('AMCPKModSMod', 'AMCPKModServerSystem', 'AMCPKModScripts.AMCPKModServerSystem.AMCPKModServerSystem')

    @Mod.DestroyClient()
    def AMCPKModClientDestroy(self):
        print '===== destroy hugo fps client ====='

    @Mod.DestroyServer()
    def AMCPKModSeverDestroy(self):
        print '===== destroy hugo fps server ====='
