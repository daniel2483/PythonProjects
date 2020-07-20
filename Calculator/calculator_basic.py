# pip install wxpython
#   Calculator Standard
#   Made by: Jose Daniel Rodriguez Sanchez
#   Build on: 2020-07-18
#   Last Update: 2020-07-20


import operations as op
import wx
import re
import os
from wx.lib.masked import NumCtrl

class MyFrame(wx.Frame):
    
    def __init__(self):
        super().__init__(parent=None, title='Standard Calculator',size=(550, 500))
        panel = wx.Panel(self)
        
        #self.wx.Frame.
        
        operand1 = ""
        operand2 = ""
        operation = ""
        
        pos_ini_y = 60
        pos_ini_x = 55
        dif_y = 40
        dif_x = 40

        #self.value = NumCtrl(panel, pos=(10, 5), size=(500, 20),value = "0",decimalChar = ".",fractionWidth = 0)
        self.value = wx.TextCtrl(panel, pos=(pos_ini_x, pos_ini_y - 40), size=(160, 20),value = "0", style=wx.TE_RIGHT | wx.TE_READONLY)
        # pos=(x,y)
        
        self.my_btn_sqr = wx.Button(panel, label='√', pos=(pos_ini_x, pos_ini_y), size=(40, 40))
        self.my_btn_pow2 = wx.Button(panel, label='x²', pos=(pos_ini_x + 40, pos_ini_y), size=(40, 40))
        self.my_btn_pow3 = wx.Button(panel, label='x³', pos=(pos_ini_x + 80, pos_ini_y), size=(40, 40))
        self.my_btn_xdiv = wx.Button(panel, label='1/x', pos=(pos_ini_x +120, pos_ini_y), size=(40, 40))
        
        self.my_btn_clear_all = wx.Button(panel, label='CE', pos=(pos_ini_x, pos_ini_y + 40), size=(40, 40))
        self.my_btn_clear = wx.Button(panel, label='C', pos=(pos_ini_x + 40, pos_ini_y + 40), size=(40, 40))
        self.my_btn_del = wx.Button(panel, label='DEL', pos=(pos_ini_x + 80, pos_ini_y + 40), size=(40, 40))
        self.my_btn_div = wx.Button(panel, label='÷', pos=(pos_ini_x + 120, pos_ini_y + 40), size=(40, 40))
        
        self.my_btn_n7 = wx.Button(panel, label='7', pos=(pos_ini_x, pos_ini_y + 80), size=(40, 40))
        self.my_btn_n8 = wx.Button(panel, label='8', pos=(pos_ini_x + 40, pos_ini_y + 80), size=(40, 40))
        self.my_btn_n9 = wx.Button(panel, label='9', pos=(pos_ini_x + 80, pos_ini_y + 80), size=(40, 40))
        self.my_btn_mul = wx.Button(panel, label='×', pos=(pos_ini_x +120, pos_ini_y + 80), size=(40, 40))
        
        self.my_btn_n4 = wx.Button(panel, label='4', pos=(pos_ini_x, pos_ini_y + 120), size=(40, 40))
        self.my_btn_n5 = wx.Button(panel, label='5', pos=(pos_ini_x + 40, pos_ini_y + 120), size=(40, 40))
        self.my_btn_n6 = wx.Button(panel, label='6', pos=(pos_ini_x + 80, pos_ini_y + 120), size=(40, 40))
        self.my_btn_sub = wx.Button(panel, label='-', pos=(pos_ini_x +120, pos_ini_y + 120), size=(40, 40))
        
        self.my_btn_n1 = wx.Button(panel, label='1', pos=(pos_ini_x, pos_ini_y + 160), size=(40, 40))
        self.my_btn_n2 = wx.Button(panel, label='2', pos=(pos_ini_x + 40, pos_ini_y + 160), size=(40, 40))
        self.my_btn_n3 = wx.Button(panel, label='3', pos=(pos_ini_x + 80, pos_ini_y + 160), size=(40, 40))
        self.my_btn_sum = wx.Button(panel, label='+', pos=(pos_ini_x +120, pos_ini_y + 160), size=(40, 40))
        
        self.my_btn_sign = wx.Button(panel, label='±', pos=(pos_ini_x, pos_ini_y + 200), size=(40, 40))
        self.my_btn_n0 = wx.Button(panel, label='0', pos=(pos_ini_x + 40, pos_ini_y + 200), size=(40, 40))
        self.my_btn_dot = wx.Button(panel, label='.', pos=(pos_ini_x + 80, pos_ini_y + 200), size=(40, 40))
        self.my_btn_result = wx.Button(panel, label='=', pos=(pos_ini_x +120, pos_ini_y + 200), size=(40, 40))

        # Results
        self.operation = wx.StaticText(panel, label="", pos=(pos_ini_x + 175, pos_ini_y))
        self.result = wx.StaticText(panel, label="", pos=(200, pos_ini_y + 90))
        self.result.SetForegroundColour(wx.RED)
        self.operation.SetForegroundColour(wx.RED)
        
        ## Setting Font Size Style
        #font = wx.Font(18, wx.DECORATIVE, wx.ITALIC, wx.NORMAL) -- wx.BOLD
        font = wx.Font(16, wx.DECORATIVE, wx.NORMAL, wx.BOLD)
        self.operation.SetFont(font)
        
        fontButtonOp = wx.Font(11, wx.DECORATIVE, wx.NORMAL, wx.BOLD)
        self.my_btn_sqr.SetFont(fontButtonOp)
        self.my_btn_pow2.SetFont(fontButtonOp)
        self.my_btn_pow3.SetFont(fontButtonOp)
        self.my_btn_xdiv.SetFont(fontButtonOp)
        self.my_btn_div.SetFont(fontButtonOp)
        self.my_btn_mul.SetFont(fontButtonOp)
        self.my_btn_sum.SetFont(fontButtonOp)
        self.my_btn_sub.SetFont(fontButtonOp)
        self.my_btn_sign.SetFont(fontButtonOp)
        self.my_btn_del.SetFont(fontButtonOp)
        self.my_btn_clear.SetFont(fontButtonOp)
        self.my_btn_clear_all.SetFont(fontButtonOp)
        self.my_btn_dot.SetFont(fontButtonOp)
        self.my_btn_result.SetFont(fontButtonOp)
        
        wx.StaticText(panel, label="Made by: Jose Daniel Rodríguez Sánchez", pos=(pos_ini_x, pos_ini_y + 325))
        wx.StaticText(panel, label="Build on: 2020-07-18", pos=(pos_ini_x, pos_ini_y + 345))
        wx.StaticText(panel, label="Last Update: 2020-07-18", pos=(pos_ini_x, pos_ini_y + 365))
        
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
        self.my_btn_dot.Bind(wx.EVT_BUTTON, self.OnButtonDot)
        
        self.my_btn_clear.Bind(wx.EVT_BUTTON, self.OnButtonclear)
        self.my_btn_clear_all.Bind(wx.EVT_BUTTON, self.OnButtonAC)
        
        self.my_btn_result.Bind(wx.EVT_BUTTON, self.OnButtonResult)
        self.my_btn_sum.Bind(wx.EVT_BUTTON, self.OnButtonSum)
        self.my_btn_sub.Bind(wx.EVT_BUTTON, self.OnButtonSub)
        self.my_btn_mul.Bind(wx.EVT_BUTTON, self.OnButtonMul)
        self.my_btn_div.Bind(wx.EVT_BUTTON, self.OnButtonDiv)
        self.my_btn_sqr.Bind(wx.EVT_BUTTON, self.OnButtonSqr)
        self.my_btn_pow2.Bind(wx.EVT_BUTTON, self.OnButtonPow2)
        self.my_btn_pow3.Bind(wx.EVT_BUTTON, self.OnButtonPow3)
        self.my_btn_xdiv.Bind(wx.EVT_BUTTON, self.OnButtonXdiv)
        self.my_btn_sign.Bind(wx.EVT_BUTTON, self.OnButtonSign)
    
        self.Show()
        
        current_dir = os.getcwd()
        
        #print ("Working on Dir: " + str(current_dir))
        
        # Style
        self.SetIcon(wx.Icon(current_dir + "/app_calc.ico"))
        #self.SetIcon(wx.Icon.SetWidth(16))
        #self.SetIcon(wx.Icon.SetHeight(16))
        #self.wx.Icon(desiredWidth = 150, desiredHeight = 150)
        self.my_btn_n1.SetBackgroundColour(wx.Colour(240, 240, 240))
        self.my_btn_n2.SetBackgroundColour(wx.Colour(240, 240, 240))
        self.my_btn_n3.SetBackgroundColour(wx.Colour(240, 240, 240))
        self.my_btn_n4.SetBackgroundColour(wx.Colour(240, 240, 240))
        self.my_btn_n5.SetBackgroundColour(wx.Colour(240, 240, 240))
        self.my_btn_n6.SetBackgroundColour(wx.Colour(240, 240, 240))
        self.my_btn_n7.SetBackgroundColour(wx.Colour(240, 240, 240))
        self.my_btn_n8.SetBackgroundColour(wx.Colour(240, 240, 240))
        self.my_btn_n9.SetBackgroundColour(wx.Colour(240, 240, 240))
        self.my_btn_n0.SetBackgroundColour(wx.Colour(240, 240, 240))
        self.my_btn_clear_all.SetBackgroundColour(wx.Colour(255, 0, 0))
    
        self.my_btn_clear_all.Bind(wx.EVT_ENTER_WINDOW, self.onMouseOver)
        self.my_btn_clear_all.Bind(wx.EVT_LEAVE_WINDOW, self.onMouseLeave)
        
        #wx.EVT_ENTER_WINDOW(self, self.onMouseOver)
        #wx.EVT_LEAVE_WINDOW(self, self.onMouseLeave)
        
    def onMouseOver(self, event):
        self.my_btn_clear_all.SetBackgroundColour((11, 11, 11))
        self.my_btn_clear_all.Refresh()
    
    def onMouseLeave(self, event):
        self.my_btn_clear_all.SetBackgroundColour((255, 0, 0))
        self.my_btn_clear_all.Refresh()
    
    def OnButton1(self, e):
        value = self.value.GetValue()
        if (value != 0):
            value = str(value) + "1"
            if "01" in value:
                value = value[-1:]
            #value = int(value)
            self.value.SetLabel(value)

    def OnButton2(self, e):
        value = self.value.GetValue()
        if (value != 0):
            value = str(value) + "2"
            if "02" in value:
                value = value[-1:]
            self.value.SetLabel(value)
            
    def OnButton3(self, e):
        value = self.value.GetValue()
        if (value != 0):
            value = str(value) + "3"
            if "03" in value:
                value = value[-1:]
            self.value.SetLabel(value)
        
    def OnButton4(self, e):
        value = self.value.GetValue()
        if (value != 0):
            value = str(value) + "4"
            if "04" in value:
                value = value[-1:]
            self.value.SetLabel(value)

    def OnButton5(self, e):
        value = self.value.GetValue()
        if (value != 0):
            value = str(value) + "5"
            if "05" in value:
                value = value[-1:]
            self.value.SetLabel(value)
        
    def OnButton6(self, e):
        value = self.value.GetValue()
        if (value != 0):
            value = str(value) + "6"
            if "06" in value:
                value = value[-1:]
            self.value.SetLabel(value)

    def OnButton7(self, e):
        value = self.value.GetValue()
        if (value != 0):
            value = str(value) + "7"
            if "07" in value:
                value = value[-1:]
            self.value.SetLabel(value)
        
    def OnButton8(self, e):
        value = self.value.GetValue()
        if (value != 0):
            value = str(value) + "8"
            if "08" in value:
                value = value[-1:]
            self.value.SetLabel(value)

    def OnButton9(self, e):
        value = self.value.GetValue()
        if (value != 0):
            value = str(value) + "9"
            if "09" in value:
                value = value[-1:]
            self.value.SetLabel(value)
        
    def OnButton0(self, e):
        value = self.value.GetValue()
        if (value != 0):
            value = str(value) + "0"
            if re.search("^00", value):
                value = value[-1:]
            self.value.SetLabel(value)
            
    def OnButtonDel(self, e):
        value = self.value.GetValue()
        if (value == 0 or value == "" or value =="-"):
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
                
    def OnButtonDot(self, e):
        value = self.value.GetValue()
        if ("." in str(value)):
            self.value.SetLabel(value)
        else:
            value = str(value) + "."
            self.value.SetLabel(value)
            
    def OnButtonSum(self,e):
        operand1 = self.value.GetValue()
        operation = operand1 + " + "
        self.value.SetLabel("0")
        self.operation.SetLabel(operation)
        
    def OnButtonSub(self,e):
        operand1 = self.value.GetValue()
        operation = operand1 + " - "
        self.value.SetLabel("0")
        self.operation.SetLabel(operation)
        
    def OnButtonMul(self,e):
        operand1 = self.value.GetValue()
        operation = operand1 + " × "
        self.value.SetLabel("0")
        self.operation.SetLabel(operation)

    def OnButtonDiv(self,e):
        operand1 = self.value.GetValue()
        operation = operand1 + " ÷ "
        self.value.SetLabel("0")
        self.operation.SetLabel(operation)
        
    def OnButtonSqr(self,e):
        operand1 = self.value.GetValue()
        self.value.SetLabel("0")
        operation = " √ " + operand1
        try: 
            result = op.sqr(float(operand1))
            str_result = str(result)
        except ValueError:
            operand1 = abs(float(operand1))
            result = op.sqr(float(operand1))
            str_result = str(result) + " i"
            
        int,decimal = str_result.split('.')
        
        if decimal == "0":
            str_result = str_result[:-2]
        
        operation = operation  + " = " + str_result
        self.operation.SetLabel(operation)
        #self.result.SetLabel(str_result)
        
    def OnButtonXdiv(self,e):
        operand1 = self.value.GetValue()
        self.value.SetLabel("0")
        operation = " 1/" + operand1
        try:
            result = 1 / float(operand1)
        except ZeroDivisionError:
            result = "∞"
        str_result = str(result)
        
        try:
            int,decimal = str_result.split('.')
        except ValueError:
            decimal = "Error"
            str_result = str_result
        
        if decimal == "0":
            str_result = str_result[:-2]
        
        operation = operation  + " = " + str_result
        self.operation.SetLabel(operation)
        #self.result.SetLabel(str_result)
        
    def OnButtonSign(self,e):
        operand = self.value.GetValue()
        if "-" in operand:
            operand = operand.replace("-", "")
            self.value.SetValue(operand)
        else:
            operand = "-" + operand
            self.value.SetValue(operand)
        
    def OnButtonPow2(self,e):
        operand1 = self.value.GetValue()
        self.value.SetLabel("0")
        operation = operand1 + "²"
        result = op.pot(float(operand1),2)
        str_result = str(result)
        
        int,decimal = str_result.split('.')
        
        if decimal == "0":
            str_result = str_result[:-2]
        
        operation = operation  + " = " + str_result
        self.operation.SetLabel(operation)
        #self.result.SetLabel(str_result)
        
    def OnButtonPow3(self,e):
        operand1 = self.value.GetValue()
        self.value.SetLabel("0")
        operation = operand1 + "³"
        result = op.pot(float(operand1),3)
        str_result = str(result)
        
        int,decimal = str_result.split('.')
        
        if decimal == "0":
            str_result = str_result[:-2]
        
        operation = operation  + " = " + str_result
        self.operation.SetLabel(operation)
        #self.result.SetLabel(str_result)
        
    def OnButtonResult(self,e):
        operation = self.operation.GetLabel()
        operand1 = operation[:-3]
        
        operand2 = self.value.GetValue()
        tmp = ""
        
        self.value.SetLabel("0")
        
        
        if " + " in operation:
            result = op.sum(float(operand1),float(operand2))
        if " - " in operation:
            result = op.sub(float(operand1),float(operand2))
        if " × " in operation:
            result = op.mult(float(operand1),float(operand2))
        if " ÷ " in operation:
            result = op.div(float(operand1),float(operand2))
        
        str_result = str(result)
        try:
            int,decimal = str_result.split('.')
        except ValueError:
            decimal = "Error"
            str_result = str_result
        
        if decimal == "0":
            str_result = str_result[:-2]
        
        operation = operation + operand2 + " = " + str_result
        self.operation.SetLabel(operation)
        
        
        #self.result.SetLabel(str_result)
            
    def OnButtonclear(self, e):
        value = "0"
        self.value.SetLabel(value)
        
    def OnButtonAC(self, e):
        value = "0"
        self.value.SetLabel(value)
        self.operation.SetLabel("")
            
if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame()
    app.MainLoop()
