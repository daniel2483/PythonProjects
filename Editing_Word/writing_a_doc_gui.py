# pip install wxpython
#   Word Letter Editor
#   Made by: Jose Daniel Rodriguez Sanchez
#   Build on: 2020-08-01
#   Last Update: 2020-08-03


import wx
import re
import os
from wx.lib.masked import NumCtrl
from PIL import Image

class MyFrame(wx.Frame):

    def __init__(self):
        super().__init__(parent=None, title='Word Letter Creator',size=(750, 620))
        panel = wx.Panel(self)

        self.SetBackgroundStyle(wx.BG_STYLE_CUSTOM)
        #self.frame = parent

        #self.wx.Frame.
        # pos=(x,y)

        pos_ini_y = 10
        pos_ini_x = 150

        text = wx.StaticText(panel, label="Elija Sucursal: ", pos=(pos_ini_x - 100, pos_ini_y))
        text.SetBackgroundColour(wx.Colour(255, 255, 255))
        sucursales = ['1. Óptica Nueva Imagen.', '2. Óptica Rosan Banco Nacional.', '3. Óptica Rosan Parque Central.']
        self.sucursal = wx.ComboBox(panel,id = 1 , value = "", pos=(pos_ini_x, pos_ini_y), size=(250, 20), choices = sucursales, style = wx.CB_DROPDOWN)

        text = wx.StaticText(panel, label="Carta dirigida a: ", pos=(pos_ini_x - 100, pos_ini_y + 30))
        text.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.sendto = wx.TextCtrl(panel, pos=(pos_ini_x, pos_ini_y + 30), size=(250, 20),value = "", style=wx.TE_LEFT)

        text = wx.StaticText(panel, label="Departamento: ", pos=(pos_ini_x - 100, pos_ini_y + 60))
        text.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.department = wx.TextCtrl(panel, pos=(pos_ini_x, pos_ini_y + 60), size=(250, 20),value = "", style=wx.TE_LEFT)

        text = wx.StaticText(panel, label="Saludo Inicial: ", pos=(pos_ini_x - 100, pos_ini_y + 90))
        text.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.greetings = wx.TextCtrl(panel, pos=(pos_ini_x, pos_ini_y + 90), size=(250, 20),value = "", style=wx.TE_LEFT)

        text = wx.StaticText(panel, label="Razón de la carta: ", pos=(pos_ini_x - 100, pos_ini_y + 120))
        text.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.reason = wx.TextCtrl(panel, pos=(pos_ini_x, pos_ini_y + 120), size=(520, 200),value = "", style=wx.TE_LEFT | wx.TE_MULTILINE)

        text = wx.StaticText(panel, label="Nombre quien firma: ", pos=(pos_ini_x - 120, pos_ini_y + 330))
        text.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.signature = wx.TextCtrl(panel, pos=(pos_ini_x, pos_ini_y + 330), size=(250, 20),value = "", style=wx.TE_LEFT)

        text = wx.StaticText(panel, label="Cédula: ", pos=(pos_ini_x - 100, pos_ini_y + 360))
        text.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.cedula1 = wx.TextCtrl(panel, pos=(pos_ini_x, pos_ini_y + 360), size=(50, 20),value = "", style=wx.TE_LEFT)
        self.cedula1.SetMaxLength(2)
        text = wx.StaticText(panel, label="-", pos=(pos_ini_x + 58, pos_ini_y + 360))
        text.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.cedula2 = wx.TextCtrl(panel, pos=(pos_ini_x + 70, pos_ini_y + 360), size=(50, 20),value = "", style=wx.TE_LEFT)
        self.cedula2.SetMaxLength(4)
        text = wx.StaticText(panel, label="-", pos=(pos_ini_x + 126, pos_ini_y + 360))
        text.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.cedula3 = wx.TextCtrl(panel, pos=(pos_ini_x + 140, pos_ini_y + 360), size=(50, 20),value = "", style=wx.TE_LEFT)
        self.cedula3.SetMaxLength(4)

        # First Status disable when no sucursal is selected
        self.sendto.Disable()
        self.department.Disable()
        self.greetings.Disable()
        self.reason.Disable()
        self.signature.Disable()
        self.cedula1.Disable()
        self.cedula2.Disable()
        self.cedula3.Disable()

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


        text = wx.StaticText(panel, label="Made by: Jose Daniel Rodríguez Sánchez", pos=(pos_ini_x-90, pos_ini_y + 500))
        text.SetBackgroundColour(wx.Colour(255, 255, 255))
        text = wx.StaticText(panel, label="Build on: 2020-08-01", pos=(pos_ini_x-90, pos_ini_y + 520))
        text.SetBackgroundColour(wx.Colour(255, 255, 255))
        text = wx.StaticText(panel, label="Last Update: 2020-08-03", pos=(pos_ini_x-90, pos_ini_y + 540))
        text.SetBackgroundColour(wx.Colour(255, 255, 255))



        ### Set event handlers
        # Event for combo sucursal
        self.sucursal.Bind(wx.EVT_COMBOBOX, self.OnCombo)
        # Event Block only numbers for ID
        self.cedula1.Bind(wx.EVT_CHAR, self.block_non_numbers)
        self.cedula2.Bind(wx.EVT_CHAR, self.block_non_numbers)
        self.cedula3.Bind(wx.EVT_CHAR, self.block_non_numbers)

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


        imageFile = current_dir + "/images/optica_rs.jpg"
        logo = wx.Image(imageFile, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        imageObj = wx.StaticBitmap(self, -1, logo, (-50, -30), (logo.GetWidth(), logo.GetHeight()))
        #imageObj.SetPosition((0,0))

        #imageFile = current_dir + "/images/optica_rs.jpg"
        #bitmap = scale_bitmap(imageFile, 300, 200)
        #logo = wx.Image(imageFile, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        #logo = wx.StaticBitmap(self, -1, logo, (-50, -30), (logo.GetWidth(), logo.GetHeight()))
        #logo.SetPosition((0,0))


        #self.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBackground)

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
        self.cedula1.Enable()
        self.cedula2.Enable()
        self.cedula3.Enable()

    def OnEraseBackground(self, evt):
        """
        Add a picture to the background
        """
        # yanked from ColourDB.py
        dc = evt.GetDC()

        if not dc:
            dc = wx.ClientDC(self)
            rect = self.GetUpdateRegion().GetBox()
            dc.SetClippingRect(rect)
        dc.Clear()
        bmp = wx.Bitmap("/images/optica_rs.jpg")
        dc.DrawBitmap(bmp, 0, 0)

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

if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame()
    app.MainLoop()
