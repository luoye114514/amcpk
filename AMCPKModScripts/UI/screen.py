# file: ./extracted\5989488_3642677f.pyc
# cracked by asJony
import mod.client.extraClientApi as clientApi
ClientSystem = clientApi.GetClientSystemCls()
ScreenNode = clientApi.GetScreenNodeCls()
ViewBinder = clientApi.GetViewBinderCls()
ViewRequest = clientApi.GetViewViewRequestCls()
import AMCPKModScripts.CliApi as api

class Screen(ScreenNode):

    def __init__(self, namespace, name, param):
        ScreenNode.__init__(self, namespace, name, param)

    def Init(self):
        print 'in screen'
        api.sButton(self, '/button1', self.killarua, 'down')
        api.sButton(self, '/button2', self.bugup, 'down')
        api.sButton(self, '/button3', self.fly, 'down')
        api.sButton(self, '/button4', self.tag, 'down')
        api.sButton(self, '/button5', self.lockback, 'down')
        api.sButton(self, '/button6', self.detach, 'down')
        api.sButton(self, '/button7', self.jump, 'down')
        api.sButton(self, '/button8', self.autoaiming, 'down')
        api.sButton(self, '/button9', self.rideplayer, 'down')
        api.sButton(self, '/button10', self.round, 'down')
        api.sButton(self, '/button', self.menu, 'down')
        api.sButton(self, '/button11', self.notauto, 'down')
        api.sButton(self, '/button12', self.ecgame, 'down')
        api.sButton(self, '/button13', self.showhealthbar, 'down')
        api.sButton(self, '/button14', self.jetpack, 'down')
        api.sButton(self, '/button15', self.airjump, 'down')
        api.sButton(self, '/button16', self.autosprint, 'down')

    def killarua(self, args):
        clientApi.GetSystem('AMCPKModSMod', 'AMCPKModClientSystem').killarua()

    def bugup(self, args):
        clientApi.GetSystem('AMCPKModSMod', 'AMCPKModClientSystem').bugup()

    def fly(self, args):
        clientApi.GetSystem('AMCPKModSMod', 'AMCPKModClientSystem').fly()

    def tag(self, args):
        clientApi.GetSystem('AMCPKModSMod', 'AMCPKModClientSystem').tag()

    def lockback(self, args):
        clientApi.GetSystem('AMCPKModSMod', 'AMCPKModClientSystem').lockback()

    def detach(self, args):
        clientApi.GetSystem('AMCPKModSMod', 'AMCPKModClientSystem').detach()

    def jump(self, args):
        clientApi.GetSystem('AMCPKModSMod', 'AMCPKModClientSystem').jump()

    def autoaiming(self, args):
        clientApi.GetSystem('AMCPKModSMod', 'AMCPKModClientSystem').autoaiming()

    def rideplayer(self, args):
        clientApi.GetSystem('AMCPKModSMod', 'AMCPKModClientSystem').rideplayer()

    def round(self, args):
        clientApi.GetSystem('AMCPKModSMod', 'AMCPKModClientSystem').round()

    def notauto(self, args):
        clientApi.GetSystem('AMCPKModSMod', 'AMCPKModClientSystem').notauto()

    def ecgame(self, args):
        clientApi.GetSystem('AMCPKModSMod', 'AMCPKModClientSystem').ecgame()

    def showhealthbar(self, args):
        clientApi.GetSystem('AMCPKModSMod', 'AMCPKModClientSystem').showhealthbar()

    def jetpack(self, args):
        clientApi.GetSystem('AMCPKModSMod', 'AMCPKModClientSystem').jetpack()

    def airjump(self, args):
        clientApi.GetSystem('AMCPKModSMod', 'AMCPKModClientSystem').airjump()

    def autosprint(self, args):
        clientApi.GetSystem('AMCPKModSMod', 'AMCPKModClientSystem').autosprint()

    def menu(self, args):
        platform = clientApi.GetPlatform()
        if platform == 0:
            api.sVisible(self, '/button10', not api.gVisible(self, '/button10'))
            api.sVisible(self, '/button1', not api.gVisible(self, '/button1'))
            api.sVisible(self, '/button2', not api.gVisible(self, '/button2'))
            api.sVisible(self, '/button3', not api.gVisible(self, '/button3'))
            api.sVisible(self, '/button4', not api.gVisible(self, '/button4'))
            api.sVisible(self, '/button5', not api.gVisible(self, '/button5'))
            api.sVisible(self, '/button6', not api.gVisible(self, '/button6'))
            api.sVisible(self, '/button7', not api.gVisible(self, '/button7'))
            api.sVisible(self, '/button8', not api.gVisible(self, '/button8'))
            api.sVisible(self, '/button9', not api.gVisible(self, '/button9'))
            api.sVisible(self, '/button11', not api.gVisible(self, '/button11'))
            api.sVisible(self, '/button12', not api.gVisible(self, '/button12'))
            api.sVisible(self, '/button13', not api.gVisible(self, '/button13'))
            api.sVisible(self, '/button14', not api.gVisible(self, '/button14'))
            api.sVisible(self, '/button15', not api.gVisible(self, '/button15'))
            api.sVisible(self, '/button16', not api.gVisible(self, '/button16'))
        else:
            api.sVisible(self, '/button10', not api.gVisible(self, '/button10'))
            api.sVisible(self, '/button1', not api.gVisible(self, '/button1'))
            api.sVisible(self, '/button2', not api.gVisible(self, '/button2'))
            api.sVisible(self, '/button3', not api.gVisible(self, '/button3'))
            api.sVisible(self, '/button4', not api.gVisible(self, '/button4'))
            api.sVisible(self, '/button5', not api.gVisible(self, '/button5'))
            api.sVisible(self, '/button6', not api.gVisible(self, '/button6'))
            api.sVisible(self, '/button7', not api.gVisible(self, '/button7'))
            api.sVisible(self, '/button8', not api.gVisible(self, '/button8'))
            api.sVisible(self, '/button9', not api.gVisible(self, '/button9'))
            api.sVisible(self, '/button11', not api.gVisible(self, '/button11'))
            api.sVisible(self, '/button12', not api.gVisible(self, '/button12'))
            api.sVisible(self, '/button13', not api.gVisible(self, '/button13'))
            api.sVisible(self, '/button14', not api.gVisible(self, '/button14'))
            api.sVisible(self, '/button15', not api.gVisible(self, '/button15'))
