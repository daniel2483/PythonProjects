# pip install wxpython
# Calculator
# Made by: Jose Daniel Rodriguez Sanchez


import operations
import wx
from wx.lib.masked import NumCtrl

class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='Standard Calculator')
        panel = wx.Panel(self)
        
        pos_ini_y = 55
        pos_ini_x = 5
        dif_y = 40
        dif_x = 40

        self.value = NumCtrl(panel, pos=(10, 5), size=(500, 20),value = "0",decimalChar = '.',fractionWidth = 0)
        # pos=(x,y)
        
        my_btn_per = wx.Button(panel, label='%', pos=(5, 55), size=(40, 40))
        my_btn_raiz = wx.Button(panel, label='√', pos=(45, 55), size=(40, 40))
        my_btn_pot2 = wx.Button(panel, label='x^2', pos=(85, 55), size=(40, 40))
        my_btn_xdiv = wx.Button(panel, label='1/x', pos=(125, 55), size=(40, 40))
        
        self.my_btn_clear = wx.Button(panel, label='CE', pos=(5, 95), size=(40, 40))
        self.my_btn_clear2 = wx.Button(panel, label='C', pos=(45, 95), size=(40, 40))
        self.my_btn_del = wx.Button(panel, label='DEL', pos=(85, 95), size=(40, 40))
        my_btn_div = wx.Button(panel, label='÷', pos=(125, 95), size=(40, 40))
        
        self.my_btn_n7 = wx.Button(panel, label='7', pos=(5, 135), size=(40, 40))
        self.my_btn_n8 = wx.Button(panel, label='8', pos=(45, 135), size=(40, 40))
        self.my_btn_n9 = wx.Button(panel, label='9', pos=(85, 135), size=(40, 40))
        my_btn_mul = wx.Button(panel, label='X', pos=(125, 135), size=(40, 40))
        
        self.my_btn_n4 = wx.Button(panel, label='4', pos=(5, 175), size=(40, 40))
        self.my_btn_n5 = wx.Button(panel, label='5', pos=(45, 175), size=(40, 40))
        self.my_btn_n6 = wx.Button(panel, label='6', pos=(85, 175), size=(40, 40))
        my_btn_sub = wx.Button(panel, label='-', pos=(125, 175), size=(40, 40))
        
        self.my_btn_n1 = wx.Button(panel, label='1', pos=(5, 215), size=(40, 40))
        self.my_btn_n2 = wx.Button(panel, label='2', pos=(45, 215), size=(40, 40))
        self.my_btn_n3 = wx.Button(panel, label='3', pos=(85, 215), size=(40, 40))
        my_btn_sum = wx.Button(panel, label='+', pos=(125, 215), size=(40, 40))
        
        my_btn_sign = wx.Button(panel, label='+/-', pos=(5, 255), size=(40, 40))
        self.my_btn_n0 = wx.Button(panel, label='0', pos=(45, 255), size=(40, 40))
        my_btn_dot = wx.Button(panel, label='.', pos=(85, 255), size=(40, 40))
        self.my_btn_result = wx.Button(panel, label='=', pos=(125, 255), size=(40, 40))

        
        self.result = wx.StaticText(panel, label="", pos=(170, 55))
        self.result.SetForegroundColour(wx.RED)
        
        # Set event handlers
        # Numbers
        self.my_btn_n1.Bind(wx.EVT_BUTTON, self.OnButton1)
        self.my_btn_n2.Bind(wx.EVT_BUTTON, self.OnButton2)
        self.my_btn_n3.Bind(wx.EVT_BUTTON, self.OnButton3)
        self.my_btn_n4.Bind(wx.EVT_BUTTON, self.OnButton4)
        self.my_btn_n5.Bind(wx.EVT_BUTTON, self.OnButton5)
        self.my_btn_n6.Bind(wx.EVT_BUTTON, self.OnButton6)
        self.my_btn_n7.Bind(wx.EVT_BUTTON, self.OnButton7)
        self.my_btn_n8.Bind(wx.EVT_BUTTON, self.OnButton8)
        self.my_btn_n9.Bind(wx.EVT_BUTTON, self.OnButton9)
        self.my_btn_n0.Bind(wx.EVT_BUTTON, self.OnButton0)
        
        # operations
        self.my_btn_del.Bind(wx.EVT_BUTTON, self.OnButtonDel)
        
        self.my_btn_clear2.Bind(wx.EVT_BUTTON, self.OnButtonclear)
        self.my_btn_clear.Bind(wx.EVT_BUTTON, self.OnButtonclear)
    
        self.Show()
    
    def OnButton1(self, e):
        value = self.value.GetValue()
        if (value == 0):
            value = "1"
            self.value.SetLabel(value)
        else:
            value = str(value) + "1"
            self.value.SetLabel(value)
        
    def OnButton2(self, e):
        value = self.value.GetValue()
        if (value == 0):
            value = "2"
            self.value.SetLabel(value)
        else:
            value = str(value) + "2"
            self.value.SetLabel(value)
            
    def OnButton3(self, e):
        value = self.value.GetValue()
        if (value == 0):
            value = "3"
            self.value.SetLabel(value)
        else:
            value = str(value) + "3"
            self.value.SetLabel(value)
        
    def OnButton4(self, e):
        value = self.value.GetValue()
        if (value == 0):
            value = "4"
            self.value.SetLabel(value)
        else:
            value = str(value) + "4"
            self.value.SetLabel(value)

    def OnButton5(self, e):
        value = self.value.GetValue()
        if (value == 0):
            value = "5"
            self.value.SetLabel(value)
        else:
            value = str(value) + "5"
            self.value.SetLabel(value)
        
    def OnButton6(self, e):
        value = self.value.GetValue()
        if (value == 0):
            value = "6"
            self.value.SetLabel(value)
        else:
            value = str(value) + "6"
            self.value.SetLabel(value)

    def OnButton7(self, e):
        value = self.value.GetValue()
        if (value == 0):
            value = "7"
            self.value.SetLabel(value)
        else:
            value = str(value) + "7"
            self.value.SetLabel(value)
        
    def OnButton8(self, e):
        value = self.value.GetValue()
        if (value == 0):
            value = "8"
            self.value.SetLabel(value)
        else:
            value = str(value) + "8"
            self.value.SetLabel(value)

    def OnButton9(self, e):
        value = self.value.GetValue()
        if (value == 0):
            value = "9"
            self.value.SetLabel(value)
        else:
            value = str(value) + "9"
            self.value.SetLabel(value)
        
    def OnButton0(self, e):
        value = self.value.GetValue()
        if (value == 0):
            value = "0"
            self.value.SetLabel(value)
        else:
            value = str(value) + "0"
            self.value.SetLabel(value)
            
    def OnButtonDel(self, e):
        value = self.value.GetValue()
        if (value == 0 or value == ""):
            value = "0"
            self.value.SetLabel(value)
        else:
            value = str(value)
            value = value[:-1]
            if (value == ""):
                value = "0"
                self.value.SetLabel(value)
            else:
                self.value.SetLabel(value)
            
    def OnButtonclear(self, e):
            value = "0"
            self.value.SetLabel(value)
            
if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame()
    app.MainLoop()
