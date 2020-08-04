# pip install wxpython
#   Word Letter Editor
#   Made by: Jose Daniel Rodriguez Sanchez
#   Build on: 2020-08-01
#   Last Update: 2020-08-03


import wx
import re
import os
from wx.lib.masked import NumCtrl

class MyFrame(wx.Frame):

    def __init__(self):
        super().__init__(parent=None, title='Word Letter Creator',size=(750, 620))
        panel = wx.Panel(self)

        #self.wx.Frame.
        # pos=(x,y)

        pos_ini_y = 10
        pos_ini_x = 150

        wx.StaticText(panel, label="Elija Sucursal: ", pos=(pos_ini_x - 100, pos_ini_y))
        sucursales = ['1. Óptica Nueva Imagen.', '2. Óptica Rosan Banco Nacional.', '3. Óptica Rosan Parque Central.']
        self.sucursal = wx.ComboBox(panel,id = 1 , value = "", pos=(pos_ini_x, pos_ini_y), size=(250, 20), choices = sucursales, style = wx.CB_DROPDOWN)

        wx.StaticText(panel, label="Carta dirigida a: ", pos=(pos_ini_x - 100, pos_ini_y + 30))
        self.sendto = wx.TextCtrl(panel, pos=(pos_ini_x, pos_ini_y + 30), size=(250, 20),value = "", style=wx.TE_LEFT)

        wx.StaticText(panel, label="Departamento: ", pos=(pos_ini_x - 100, pos_ini_y + 60))
        self.department = wx.TextCtrl(panel, pos=(pos_ini_x, pos_ini_y + 60), size=(250, 20),value = "", style=wx.TE_LEFT)

        wx.StaticText(panel, label="Saludo Inicial: ", pos=(pos_ini_x - 100, pos_ini_y + 90))
        self.greetings = wx.TextCtrl(panel, pos=(pos_ini_x, pos_ini_y + 90), size=(250, 20),value = "", style=wx.TE_LEFT)

        wx.StaticText(panel, label="Razón de la carta: ", pos=(pos_ini_x - 100, pos_ini_y + 120))
        self.reason = wx.TextCtrl(panel, pos=(pos_ini_x, pos_ini_y + 120), size=(520, 200),value = "", style=wx.TE_LEFT | wx.TE_MULTILINE)

        wx.StaticText(panel, label="Nombre quien firma: ", pos=(pos_ini_x - 120, pos_ini_y + 330))
        self.signature = wx.TextCtrl(panel, pos=(pos_ini_x, pos_ini_y + 330), size=(250, 20),value = "", style=wx.TE_LEFT)

        # First Status disable when no sucursal is selected
        self.sendto.Disable()
        self.department.Disable()
        self.greetings.Disable()
        self.reason.Disable()
        self.signature.Disable()


        self.my_btn_save = wx.Button(panel, label='Guardar', pos=(pos_ini_x-50, pos_ini_y + 450), size=(100, 40))
        self.my_btn_save.Disable()

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


        wx.StaticText(panel, label="Made by: Jose Daniel Rodríguez Sánchez", pos=(pos_ini_x, pos_ini_y + 500))
        wx.StaticText(panel, label="Build on: 2020-08-01", pos=(pos_ini_x, pos_ini_y + 520))
        wx.StaticText(panel, label="Last Update: 2020-08-03", pos=(pos_ini_x, pos_ini_y + 540))

        ### Set event handlers
        # Event for combo sucursal
        self.sucursal.Bind(wx.EVT_COMBOBOX, self.OnCombo)

        # Save button
        self.my_btn_save.Bind(wx.EVT_BUTTON, self.OnButtonSave)


        self.Show()

        current_dir = os.getcwd()

        #print ("Working on Dir: " + str(current_dir))

        # Style
        self.SetIcon(wx.Icon(current_dir + "/images/word_logo.png"))
        #self.SetIcon(wx.Icon.SetWidth(16))
        #self.SetIcon(wx.Icon.SetHeight(16))
        #self.wx.Icon(desiredWidth = 150, desiredHeight = 150)
        self.my_btn_save.SetBackgroundColour(wx.Colour(240, 240, 240))

        #wx.EVT_ENTER_WINDOW(self, self.onMouseOver)
        #wx.EVT_LEAVE_WINDOW(self, self.onMouseLeave)

    def onMouseOver(self, event):
        self.my_btn_clear_all.SetBackgroundColour((11, 11, 11))
        self.my_btn_clear_all.Refresh()

    def onMouseLeave(self, event):
        self.my_btn_clear_all.SetBackgroundColour((255, 0, 0))
        self.my_btn_clear_all.Refresh()

    def OnButtonSave(self, e):
        print ("Saving File ...")

    def OnCombo(self, event):
        #self.label.SetLabel("selected "+ self.combo.GetValue() +" from Combobox")
        negocio = self.sucursal.GetValue()
        #print (negocio)
        self.my_btn_save.Enable()
        self.sendto.Enable()
        self.department.Enable()
        self.greetings.Enable()
        self.reason.Enable()
        self.signature.Enable()

if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame()
    app.MainLoop()
