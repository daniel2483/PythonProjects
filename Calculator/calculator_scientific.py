# pip install wxpython
#   Calculator Scientific
#   Made by: Jose Daniel Rodriguez Sanchez
#   Build on: 2020-07-20
#   Last Update: 2020-07-22


import operations as op
import wx
import re
import os
import wx.richtext as rt
from wx.lib.masked import NumCtrl

class MyFrame(wx.Frame):
    
    def __init__(self):
        super().__init__(parent=None, title='Scientific Calculator',size=(600, 550))
        panel = wx.Panel(self)
        
        # create wx.Bitmap object  
        bmpForRootAny = wx.Bitmap('images/root.png') 
        
        operand1 = ""
        operand2 = ""
        operation = ""
        
        pos_ini_y = 170
        pos_ini_x = 95
        dif_y = 40
        dif_x = 40

        #self.value = NumCtrl(panel, pos=(5, 0), size=(500, 40),value = "",decimalChar = ".",fractionWidth = 0)
        self.value = wx.TextCtrl(panel, pos=(pos_ini_x - 40, pos_ini_y - 150), size=(200, 60),value = "", style=wx.TE_RIGHT | wx.TE_MULTILINE | wx.SUNKEN_BORDER)
        self.value.Bind(wx.EVT_CHAR, self.block_non_numbers)
        #self.value.Bind(wx.EVT_LEFT_DOWN, self.click_on_text_field) 
        
        # To have cursor always a the right position
        self.value.Bind(wx.EVT_LEFT_UP, self.click_on_text_field)
        
        # pos=(x,y)
        
        self.my_btn_pow3 = wx.Button(panel, label='x³', pos=(pos_ini_x -40, pos_ini_y -80), size=(40, 40))
        self.my_btn_cuber = wx.Button(panel, label='∛', pos=(pos_ini_x, pos_ini_y -80), size=(40, 40))
        # set bmp as bitmap for button 
        #self.my_btn_root.SetBitmap(bmpForRootAny) 
        self.my_btn_arcs = wx.Button(panel, label='arcs', pos=(pos_ini_x + 40, pos_ini_y - 80), size=(40, 40))
        self.my_btn_arcc = wx.Button(panel, label='arcc', pos=(pos_ini_x + 80, pos_ini_y -80 ), size=(40, 40))
        self.my_btn_arct = wx.Button(panel, label='arct', pos=(pos_ini_x + 120, pos_ini_y - 80), size=(40, 40))
        
        self.my_btn_pow2 = wx.Button(panel, label='x²', pos=(pos_ini_x -40, pos_ini_y -40), size=(40, 40))
        self.my_btn_powy = wx.Button(panel, label='x ʸ', pos=(pos_ini_x, pos_ini_y -40), size=(40, 40))
        self.my_btn_sin = wx.Button(panel, label='sin', pos=(pos_ini_x + 40, pos_ini_y - 40), size=(40, 40))
        self.my_btn_cos = wx.Button(panel, label='cos', pos=(pos_ini_x + 80, pos_ini_y -40 ), size=(40, 40))
        self.my_btn_tan = wx.Button(panel, label='tan', pos=(pos_ini_x + 120, pos_ini_y - 40), size=(40, 40))
        
        self.my_btn_xdiv = wx.Button(panel, label='1/x', pos=(pos_ini_x -40, pos_ini_y), size=(40, 40))
        self.my_btn_ex = wx.Button(panel, label='e^x', pos=(pos_ini_x, pos_ini_y), size=(40, 40))
        self.my_btn_ln = wx.Button(panel, label='ln', pos=(pos_ini_x + 40, pos_ini_y), size=(40, 40))
        self.my_btn_eu = wx.Button(panel, label='e', pos=(pos_ini_x + 80, pos_ini_y), size=(40, 40))
        self.my_btn_gra = wx.Button(panel, label='G', pos=(pos_ini_x + 120, pos_ini_y), size=(40, 40))
        
        self.my_btn_sqr = wx.Button(panel, label='√', pos=(pos_ini_x-40, pos_ini_y + 40), size=(40, 40))
        self.my_btn_base10 = wx.Button(panel, label='10^x', pos=(pos_ini_x, pos_ini_y + 40), size=(40, 40))
        self.my_btn_log = wx.Button(panel, label='Log', pos=(pos_ini_x + 40, pos_ini_y + 40), size=(40, 40))
        self.my_btn_res = wx.Button(panel, label='Res', pos=(pos_ini_x + 80, pos_ini_y + 40), size=(40, 40))
        self.my_btn_abs = wx.Button(panel, label='ABS', pos=(pos_ini_x +120, pos_ini_y + 40), size=(40, 40))
        
        self.my_btn_mem = wx.Button(panel, label='Mem', pos=(pos_ini_x - 40, pos_ini_y + 80), size=(40, 40))
        self.my_btn_clear_all = wx.Button(panel, label='CE', pos=(pos_ini_x, pos_ini_y + 80), size=(40, 40))
        self.my_btn_clear = wx.Button(panel, label='C', pos=(pos_ini_x + 40, pos_ini_y + 80), size=(40, 40))
        self.my_btn_del = wx.Button(panel, label='DEL', pos=(pos_ini_x + 80, pos_ini_y + 80), size=(40, 40))
        self.my_btn_div = wx.Button(panel, label='÷', pos=(pos_ini_x + 120, pos_ini_y + 80), size=(40, 40))
        
        self.my_btn_pi = wx.Button(panel, label='π', pos=(pos_ini_x - 40 , pos_ini_y + 120), size=(40, 40))
        self.my_btn_n7 = wx.Button(panel, label='7', pos=(pos_ini_x, pos_ini_y + 120), size=(40, 40))
        self.my_btn_n8 = wx.Button(panel, label='8', pos=(pos_ini_x + 40, pos_ini_y + 120), size=(40, 40))
        self.my_btn_n9 = wx.Button(panel, label='9', pos=(pos_ini_x + 80, pos_ini_y + 120), size=(40, 40))
        self.my_btn_mul = wx.Button(panel, label='×', pos=(pos_ini_x +120, pos_ini_y + 120), size=(40, 40))
        
        self.my_btn_fac = wx.Button(panel, label='n!', pos=(pos_ini_x - 40 , pos_ini_y + 160), size=(40, 40))
        self.my_btn_n4 = wx.Button(panel, label='4', pos=(pos_ini_x, pos_ini_y + 160), size=(40, 40))
        self.my_btn_n5 = wx.Button(panel, label='5', pos=(pos_ini_x + 40, pos_ini_y + 160), size=(40, 40))
        self.my_btn_n6 = wx.Button(panel, label='6', pos=(pos_ini_x + 80, pos_ini_y + 160), size=(40, 40))
        self.my_btn_sub = wx.Button(panel, label='-', pos=(pos_ini_x +120, pos_ini_y + 160), size=(40, 40))
        
        self.my_btn_sign = wx.Button(panel, label='±', pos=(pos_ini_x - 40 , pos_ini_y + 200), size=(40, 40))
        self.my_btn_n1 = wx.Button(panel, label='1', pos=(pos_ini_x, pos_ini_y + 200), size=(40, 40))
        self.my_btn_n2 = wx.Button(panel, label='2', pos=(pos_ini_x + 40, pos_ini_y + 200), size=(40, 40))
        self.my_btn_n3 = wx.Button(panel, label='3', pos=(pos_ini_x + 80, pos_ini_y + 200), size=(40, 40))
        self.my_btn_sum = wx.Button(panel, label='+', pos=(pos_ini_x +120, pos_ini_y + 200), size=(40, 40))
        
        self.my_btn_openp = wx.Button(panel, label='(', pos=(pos_ini_x - 40, pos_ini_y + 240), size=(40, 40))
        self.my_btn_closep = wx.Button(panel, label=')', pos=(pos_ini_x, pos_ini_y + 240), size=(40, 40))
        self.my_btn_n0 = wx.Button(panel, label='0', pos=(pos_ini_x + 40, pos_ini_y + 240), size=(40, 40))
        self.my_btn_dot = wx.Button(panel, label='.', pos=(pos_ini_x + 80, pos_ini_y + 240), size=(40, 40))
        self.my_btn_result = wx.Button(panel, label='=', pos=(pos_ini_x +120, pos_ini_y + 240), size=(40, 40))

        # Results
        self.operation = wx.StaticText(panel, label="", pos=(pos_ini_x + 175, pos_ini_y))
        self.result = wx.StaticText(panel, label="", pos=(200, pos_ini_y + 90))
        self.result.SetForegroundColour(wx.RED)
        self.operation.SetForegroundColour(wx.RED)
        
        ## Setting Font Size Style
        #font = wx.Font(18, wx.DECORATIVE, wx.ITALIC, wx.NORMAL) -- wx.BOLD
        font = wx.Font(16, wx.DECORATIVE, wx.NORMAL, wx.BOLD)
        self.operation.SetFont(font)
        
        ## Fonts Style
        fontButtonOpMain = wx.Font(15, wx.DECORATIVE, wx.NORMAL, wx.BOLD)
        fontButtonOp = wx.Font(11, wx.DECORATIVE, wx.NORMAL, wx.BOLD)
        self.my_btn_sqr.SetFont(fontButtonOp)
        self.my_btn_pow2.SetFont(fontButtonOp)
        self.my_btn_pow3.SetFont(fontButtonOp)
        self.my_btn_xdiv.SetFont(fontButtonOp)
        self.my_btn_div.SetFont(fontButtonOpMain)
        self.my_btn_mul.SetFont(fontButtonOpMain)
        self.my_btn_sum.SetFont(fontButtonOpMain)
        self.my_btn_sub.SetFont(fontButtonOpMain)
        self.my_btn_sign.SetFont(fontButtonOp)
        self.my_btn_del.SetFont(fontButtonOp)
        self.my_btn_clear.SetFont(fontButtonOp)
        self.my_btn_clear_all.SetFont(fontButtonOp)
        self.my_btn_dot.SetFont(fontButtonOp)
        self.my_btn_result.SetFont(fontButtonOpMain)
        self.my_btn_cuber.SetFont(wx.Font(18, wx.DECORATIVE, wx.NORMAL, wx.BOLD))
        self.my_btn_arcc.SetFont(fontButtonOp)
        self.my_btn_arcs.SetFont(fontButtonOp)
        self.my_btn_arct.SetFont(fontButtonOp)
        self.my_btn_powy.SetFont(fontButtonOp)
        self.my_btn_sin.SetFont(fontButtonOp)
        self.my_btn_cos.SetFont(fontButtonOp)
        self.my_btn_tan.SetFont(fontButtonOp)
        self.my_btn_ex.SetFont(fontButtonOp)
        self.my_btn_ln.SetFont(fontButtonOp)
        self.my_btn_eu.SetFont(fontButtonOp)
        self.my_btn_gra.SetFont(fontButtonOp)
        self.my_btn_base10.SetFont(fontButtonOp)
        self.my_btn_log.SetFont(fontButtonOp)
        self.my_btn_res.SetFont(fontButtonOp)
        self.my_btn_abs.SetFont(fontButtonOp)
        self.my_btn_mem.SetFont(fontButtonOp)
        self.my_btn_pi.SetFont(fontButtonOp)
        self.my_btn_fac.SetFont(fontButtonOp)
        self.my_btn_openp.SetFont(fontButtonOp)
        self.my_btn_closep.SetFont(fontButtonOp)
        
        
        
        wx.StaticText(panel, label="Made by: Jose Daniel Rodríguez Sánchez", pos=(pos_ini_x + 175, pos_ini_y + 200))
        wx.StaticText(panel, label="Build on: 2020-07-20", pos=(pos_ini_x + 175, pos_ini_y + 225))
        wx.StaticText(panel, label="Last Update: 2020-07-22", pos=(pos_ini_x + 175, pos_ini_y + 245))
        
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
        self.my_btn_cuber.Bind(wx.EVT_BUTTON, self.OnButtonCuber)
        self.my_btn_powy.Bind(wx.EVT_BUTTON, self.OnButtonPowy)
        
    
        self.Show()
        
        current_dir = os.getcwd()
        
        #print ("Working on Dir: " + str(current_dir))
        
        # Style
        self.SetIcon(wx.Icon(current_dir + "/images/app_calc.ico"))
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
    
    ########## Buttons Numbers ###########
    
    def OnButton1(self, e):
        value = self.value.GetValue()
        if (value != 0):
            value = str(value) + "1"
            print (value)
            if re.search("^01", value):
                value_len = len(value)
                value = value[1:value_len]
            self.value.SetLabel(value)
        self.value.SetFocus()
        self.value.SetInsertionPointEnd()

    def OnButton2(self, e):
        value = self.value.GetValue()
        if (value != 0):
            value = str(value) + "2"
            print (value)
            if re.search("^02", value):
                value_len = len(value)
                value = value[1:value_len]
            self.value.SetLabel(value)
        self.value.SetFocus()
        self.value.SetInsertionPointEnd()
            
    def OnButton3(self, e):
        value = self.value.GetValue()
        if (value != 0):
            value = str(value) + "3"
            print (value)
            if re.search("^03", value):
                value_len = len(value)
                value = value[1:value_len]
            self.value.SetLabel(value)
        self.value.SetFocus()
        self.value.SetInsertionPointEnd()
        
    def OnButton4(self, e):
        value = self.value.GetValue()
        if (value != 0):
            value = str(value) + "4"
            print (value)
            if re.search("^04", value):
                value_len = len(value)
                value = value[1:value_len]
            self.value.SetLabel(value)
        self.value.SetFocus()
        self.value.SetInsertionPointEnd()

    def OnButton5(self, e):
        value = self.value.GetValue()
        if (value != 0):
            value = str(value) + "5"
            print (value)
            if re.search("^05", value):
                value_len = len(value)
                value = value[1:value_len]
            self.value.SetLabel(value)
        self.value.SetFocus()
        self.value.SetInsertionPointEnd()
        
    def OnButton6(self, e):
        value = self.value.GetValue()
        if (value != 0):
            value = str(value) + "6"
            print (value)
            if re.search("^06", value):
                value_len = len(value)
                value = value[1:value_len]
            self.value.SetLabel(value)
        self.value.SetFocus()
        self.value.SetInsertionPointEnd()

    def OnButton7(self, e):
        value = self.value.GetValue()
        if (value != 0):
            value = str(value) + "7"
            print (value)
            if re.search("^07", value):
                value_len = len(value)
                value = value[1:value_len]
            self.value.SetLabel(value)
        self.value.SetFocus()
        self.value.SetInsertionPointEnd()
        
    def OnButton8(self, e):
        value = self.value.GetValue()
        if (value != 0):
            value = str(value) + "8"
            print (value)
            if re.search("^08", value):
                value_len = len(value)
                value = value[1:value_len]
            self.value.SetLabel(value)
        self.value.SetFocus()
        self.value.SetInsertionPointEnd()

    def OnButton9(self, e):
        value = self.value.GetValue()
        if (value != 0):
            value = str(value) + "9"
            print (value)
            if re.search("^09", value):
                value_len = len(value)
                value = value[1:value_len]
            self.value.SetLabel(value)
        self.value.SetFocus()
        self.value.SetInsertionPointEnd()
        
    def OnButton0(self, e):
        value = self.value.GetValue()
        if (value != 0):
            value = str(value) + "0"
            if re.search("^00", value):
                value = value[-1:]
            self.value.SetLabel(value)
        self.value.SetFocus()
        self.value.SetInsertionPointEnd()
    
    ########## Buttons Operations ###########
    
    def OnButtonDel(self, e):
        value = self.value.GetValue()
        if (value == 0 or value == "" or value =="-"):
            value = ""
            self.value.SetLabel(value)
        else:
            value = str(value)
            value = value[:-1]
            if (value == ""):
                value = ""
                self.value.SetLabel(value)
            else:
                self.value.SetLabel(value)
        self.value.SetFocus()
        self.value.SetInsertionPointEnd()
                
    def OnButtonDot(self, e):
        value = self.value.GetValue()
        if ("." in str(value)):
            self.value.SetLabel(value)
        else:
            value = str(value) + "."
            self.value.SetLabel(value)
        self.value.SetFocus()
        self.value.SetInsertionPointEnd()
            
    def OnButtonSum(self,e):
        operand1 = self.value.GetValue()
        operation = operand1 + " + "
        self.value.SetLabel("")
        self.operation.SetLabel(operation)
        self.value.SetFocus()
        self.value.SetInsertionPointEnd()
        
    def OnButtonSub(self,e):
        operand1 = self.value.GetValue()
        operation = operand1 + " - "
        self.value.SetLabel("")
        self.operation.SetLabel(operation)
        self.value.SetFocus()
        self.value.SetInsertionPointEnd()
        
    def OnButtonMul(self,e):
        operand1 = self.value.GetValue()
        operation = operand1 + " × "
        self.value.SetLabel("")
        self.operation.SetLabel(operation)
        self.value.SetFocus()
        self.value.SetInsertionPointEnd()

    def OnButtonDiv(self,e):
        operand1 = self.value.GetValue()
        operation = operand1 + " ÷ "
        self.value.SetLabel("")
        self.operation.SetLabel(operation)
        self.value.SetFocus()
        self.value.SetInsertionPointEnd()
        
    def OnButtonSqr(self,e):
        operand1 = self.value.GetValue()
        self.value.SetLabel("")
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
        self.value.SetFocus()
        self.value.SetInsertionPointEnd()
        
    def OnButtonXdiv(self,e):
        operand1 = self.value.GetValue()
        self.value.SetLabel("")
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
        self.value.SetFocus()
        self.value.SetInsertionPointEnd()
        
    def OnButtonSign(self,e):
        operand = self.value.GetValue()
        if "-" in operand:
            operand = operand.replace("-", "")
            self.value.SetValue(operand)
        else:
            operand = "-" + operand
            self.value.SetValue(operand)
        self.value.SetFocus()
        self.value.SetInsertionPointEnd()
        
    def OnButtonPow2(self,e):
        operand1 = self.value.GetValue()
        self.value.SetLabel("")
        operation = operand1 + "²"
        result = op.pot(float(operand1),2)
        str_result = str(result)
        
        int,decimal = str_result.split('.')
        
        if decimal == "0":
            str_result = str_result[:-2]
        
        operation = operation  + " = " + str_result
        self.operation.SetLabel(operation)
        #self.result.SetLabel(str_result)
        self.value.SetFocus()
        self.value.SetInsertionPointEnd()
        
    def OnButtonPow3(self,e):
        operand1 = self.value.GetValue()
        self.value.SetLabel("")
        operation = operand1 + "³"
        result = op.pot(float(operand1),3)
        str_result = str(result)
        
        int,decimal = str_result.split('.')
        
        if decimal == "0":
            str_result = str_result[:-2]
        
        operation = operation  + " = " + str_result
        self.operation.SetLabel(operation)
        #self.result.SetLabel(str_result)
        self.value.SetFocus()
        self.value.SetInsertionPointEnd()

    def OnButtonPowy(self,e):
        operand1 = self.value.GetValue()
        if operand1 == "":
            print ("No inicial value...")
        else:
            self.value.SetLabel(operand1 + "^")
            operation = operand1 + " ^ "
            self.value.SetLabel(operation)
            self.operation.SetLabel(operation)
            
        self.value.SetFocus()
        self.value.SetInsertionPointEnd()

    def OnButtonCuber(self,e):
        operand1 = self.value.GetValue()
        self.value.SetLabel("")
        operation = "∛" + operand1
        result = op.cube_root(float(operand1))
        str_result = str(result)
        
        try:
            int,decimal = str_result.split('.')
        except ValueError:
            decimal=""
            int = str_result
        
        if decimal == "0":
            str_result = str_result[:-2]
        
        operation = operation  + " = " + str_result
        self.operation.SetLabel(operation)
        #self.result.SetLabel(str_result)
        self.value.SetFocus()
        self.value.SetInsertionPointEnd()
        
    def OnButtonResult(self,e):
        operation = self.operation.GetLabel()
        #print (operation)
        operand1 = operation[:-3]
        
        operand2 = self.value.GetValue()
        tmp = ""
        
        self.value.SetLabel("")
        
        
        if " + " in operation:
            result = op.sum(float(operand1),float(operand2))
        if " - " in operation:
            result = op.sub(float(operand1),float(operand2))
        if " × " in operation:
            result = op.mult(float(operand1),float(operand2))
        if " ÷ " in operation:
            result = op.div(float(operand1),float(operand2))
        if " ^ " in operation:
            operand1,operand2 = operand2.split(' ^ ')
            result = op.pot(float(operand1),float(operand2))
        
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
        
        self.value.SetFocus()
        self.value.SetInsertionPointEnd()
            
    def OnButtonclear(self, e):
        value = ""
        self.value.SetLabel(value)
        self.value.SetFocus()
        self.value.SetInsertionPointEnd()
        
    def OnButtonAC(self, e):
        value = ""
        self.value.SetLabel(value)
        self.operation.SetLabel("")
        self.value.SetFocus()
        self.value.SetInsertionPointEnd()
        
    def click_on_text_field(self, event):
        self.value.SetInsertionPointEnd()
        event.Skip()
            
            
    def block_non_numbers(self, event):
        key_code = event.GetKeyCode()
        
        print ("Key: " + str(key_code))
        
        if key_code in (8, 127, 314, 316):
            event.Skip()
            return

        # Allow ASCII numerics
        if ord('0') <= key_code <= ord('9'):
            event.Skip()
            return

        if key_code == ord('-'):
            value = self.value.GetValue()
            value_len = len(value)
            print (value)
            if re.search("^-",value):
                self.value.SetValue(value[1:value_len])
                self.value.SetInsertionPointEnd() 
            else:
                self.value.SetValue("-" + value)
                self.value.SetInsertionPointEnd() 
            #event.Skip()
            return

        # Allow decimal points
        if key_code == ord('.'):
            value = self.value.GetValue()
            print (value)
            if re.search("\.", value):
                print ("Already decimal in op...")
                return
            event.Skip()
            return

        # Allow tabs, for tab navigation between TextCtrls
        #if key_code == ord('\t'):
        #    event.Skip()
        #    return

        # Block everything else
        return
if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame()
    app.MainLoop()