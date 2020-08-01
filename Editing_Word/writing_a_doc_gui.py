# pip install wxpython
#   Word Letter Editor
#   Made by: Jose Daniel Rodriguez Sanchez
#   Build on: 2020-08-01
#   Last Update: 2020-08-01


import wx
import re
import os
from wx.lib.masked import NumCtrl

class MyFrame(wx.Frame):

    def __init__(self):
        super().__init__(parent=None, title='Word Letter Creator',size=(550, 500))
        panel = wx.Panel(self)

        #self.wx.Frame.


        pos_ini_y = 10
        pos_ini_x = 150

        wx.StaticText(panel, label="Elija Sucursal: ", pos=(pos_ini_x - 100, pos_ini_y))

        sucursales = ['1. Óptica Nueva Imagen.', '2. Óptica Rosan Banco Nacional.', '3. Óptica Rosan Parque Central.']
        self.sucursal = wx.ComboBox(panel,id = 1 , value = "1. Óptica Nueva Imagen.", pos=(pos_ini_x, pos_ini_y), size=(250, 20), choices = sucursales, style = wx.CB_DROPDOWN)

        #self.value = NumCtrl(panel, pos=(10, 5), size=(500, 20),value = "0",decimalChar = ".",fractionWidth = 0)
        self.value = wx.TextCtrl(panel, pos=(pos_ini_x, pos_ini_y + 30), size=(160, 20),value = "", style=wx.TE_LEFT)
        # pos=(x,y)


        self.my_btn_n1 = wx.Button(panel, label='Guardar', pos=(pos_ini_x-50, pos_ini_y + 200), size=(100, 40))

        # Results
        self.operation = wx.StaticText(panel, label="", pos=(pos_ini_x + 175, pos_ini_y))
        self.result = wx.StaticText(panel, label="", pos=(200, pos_ini_y + 90))
        self.result.SetForegroundColour(wx.RED)
        self.operation.SetForegroundColour(wx.RED)

        ## Setting Font Size Style
        #font = wx.Font(18, wx.DECORATIVE, wx.ITALIC, wx.NORMAL) -- wx.BOLD
        font = wx.Font(16, wx.DECORATIVE, wx.NORMAL, wx.BOLD)
        self.operation.SetFont(font)

        fontButton = wx.Font(11, wx.DECORATIVE, wx.NORMAL, wx.BOLD)


        wx.StaticText(panel, label="Made by: Jose Daniel Rodríguez Sánchez", pos=(pos_ini_x, pos_ini_y + 325))
        wx.StaticText(panel, label="Build on: 2020-08-01", pos=(pos_ini_x, pos_ini_y + 345))
        wx.StaticText(panel, label="Last Update: 2020-08-01", pos=(pos_ini_x, pos_ini_y + 365))

        # Set event handlers
        # Numbers
        self.my_btn_n1.Bind(wx.EVT_BUTTON, self.OnButton1)


        self.Show()

        current_dir = os.getcwd()

        #print ("Working on Dir: " + str(current_dir))

        # Style
        self.SetIcon(wx.Icon(current_dir + "/images/word_logo.png"))
        #self.SetIcon(wx.Icon.SetWidth(16))
        #self.SetIcon(wx.Icon.SetHeight(16))
        #self.wx.Icon(desiredWidth = 150, desiredHeight = 150)
        self.my_btn_n1.SetBackgroundColour(wx.Colour(240, 240, 240))

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
            print (value)
            if re.search("^01", value):
                value_len = len(value)
                value = value[1:value_len]
            #value = int(value)
            self.value.SetLabel(value)


if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame()
    app.MainLoop()
