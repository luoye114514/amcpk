# file: ./extracted\c8fe3394_8389bb6d.pyc
# cracked by asJony
import mod.client.extraClientApi as clientApi
ViewBinder = clientApi.GetViewBinderCls()
ClientSystem = clientApi.GetClientSystemCls()

def sPos(uiNode, path, pos):
    baseUIControl = uiNode.GetBaseUIControl(path)
    baseUIControl.SetPosition(pos)


def sSize(uiNode, path, size):
    baseUIControl = uiNode.GetBaseUIControl(path)
    baseUIControl.SetSize(size)


def sVisible(uiNode, path, Bool):
    baseUIControl = uiNode.GetBaseUIControl(path)
    baseUIControl.SetVisible(Bool)


def sText(uiNode, path, text):
    labelUIControl = uiNode.GetBaseUIControl(path).asLabel()
    labelUIControl.SetText(text)


def sAlpha(uiNode, path, num_range_0_1):
    baseUIControl = uiNode.GetBaseUIControl(path)
    baseUIControl.SetAlpha(num_range_0_1)


def sItem(uiNode, path, itemName, auxValue):
    itemRendererBaseControl = uiNode.GetBaseUIControl(path)
    itemRendererControl = itemRendererBaseControl.asItemRenderer()
    itemRendererControl.SetUiItem(itemName, auxValue)


def sToggle(uiNode, path, Bool):
    switchToggleUIControl = uiNode.GetBaseUIControl(path).asSwitchToggle()
    switchToggleUIControl.SetToggleState(Bool)


def sButton(uiNode, path, func, mode):
    buttonUIControl = uiNode.GetBaseUIControl(path).asButton()
    buttonUIControl.AddTouchEventParams({'isSwallow': True})
    if mode == 'down':
        buttonUIControl.SetButtonTouchDownCallback(func)
    if mode == 'up':
        buttonUIControl.SetButtonTouchUpCallback(func)
    if mode == 'cancel':
        buttonUIControl.SetButtonTouchCancelCallback(func)


def gPos(uiNode, path):
    baseUIControl = uiNode.GetBaseUIControl(path)
    textPosition = baseUIControl.GetPosition()
    return textPosition


def gSize(uiNode, path):
    baseUIControl = uiNode.GetBaseUIControl(path)
    Size = baseUIControl.GetSize()
    return Size


def gVisible(uiNode, path):
    baseUIControl = uiNode.GetBaseUIControl(path)
    textVisible = baseUIControl.GetVisible()
    return textVisible


def gText(uiNode, path):
    labelUIControl = uiNode.GetBaseUIControl(path).asLabel()
    return labelUIControl.GetText()


def gPath(uiNode, path):
    scrollViewUIControl = uiNode.GetBaseUIControl(path).asScrollView()
    Path = scrollViewUIControl.GetScrollViewContentPath()
    return Path
