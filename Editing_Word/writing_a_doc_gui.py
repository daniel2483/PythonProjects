# pip install wxpython
#   Word Letter Editor
#   Made by: Jose Daniel Rodriguez Sanchez
#   Build on: 2020-08-01
#   Last Update: 2020-08-04


import wx
import re
import os
import writing_a_doc_module as letter
import send_email_to_gmail_account_module as email

from wx.lib.masked import NumCtrl
from PIL import Image

#from mailmerge import MailMerge
#from datetime import date
#import os

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
        #text.SetBackgroundColour(wx.Colour(255, 255, 255))
        sucursales = ['1. Óptica Nueva Imagen.', '2. Óptica Rosan Banco Nacional.', '3. Óptica Rosan Parque Central.']
        self.sucursal = wx.ComboBox(panel , value = "", pos=(pos_ini_x, pos_ini_y), size=(250, 20), choices = sucursales, style = wx.CB_DROPDOWN | wx.TE_READONLY)
        self.text_alarm1 = wx.StaticText(panel,id = 1, label="* Campo requerido", pos=(pos_ini_x + 260, pos_ini_y))
        #self.text_alarm1.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.text_alarm1.SetForegroundColour(wx.Colour(196, 56, 25))


        text = wx.StaticText(panel, label="Carta dirigida a: ", pos=(pos_ini_x - 100, pos_ini_y + 30))
        #text.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.sendto = wx.TextCtrl(panel, pos=(pos_ini_x, pos_ini_y + 30), size=(250, 20),value = "", style=wx.TE_LEFT)
        self.text_alarm2 = wx.StaticText(panel,id = 2, label="* Campo requerido", pos=(pos_ini_x + 260, pos_ini_y + 30))
        #self.text_alarm1.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.text_alarm2.SetForegroundColour(wx.Colour(196, 56, 25))
        #self.text_alarm2.Hide()

        text = wx.StaticText(panel, label="Departamento: ", pos=(pos_ini_x - 100, pos_ini_y + 60))
        #text.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.department = wx.TextCtrl(panel, pos=(pos_ini_x, pos_ini_y + 60), size=(250, 20),value = "", style=wx.TE_LEFT)

        text = wx.StaticText(panel, label="Saludo Inicial: ", pos=(pos_ini_x - 100, pos_ini_y + 90))
        #text.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.greetings = wx.TextCtrl(panel, pos=(pos_ini_x, pos_ini_y + 90), size=(250, 20),value = "", style=wx.TE_LEFT)
        #self.text_alarm3 = wx.StaticText(panel,id = 2, label="* Campo requerido", pos=(pos_ini_x + 260, pos_ini_y + 90))
        #self.text_alarm1.SetBackgroundColour(wx.Colour(255, 255, 255))
        #self.text_alarm3.SetForegroundColour(wx.Colour(196, 56, 25))
        #self.text_alarm2.Hide()

        text = wx.StaticText(panel, label="Razón de la carta: ", pos=(pos_ini_x - 100, pos_ini_y + 120))
        #text.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.reason = wx.TextCtrl(panel, pos=(pos_ini_x, pos_ini_y + 120), size=(470, 200),value = "", style=wx.TE_LEFT | wx.TE_MULTILINE)
        self.text_alarm4 = wx.StaticText(panel,id = 4, label="* Campo requerido", pos=(pos_ini_x + 480, pos_ini_y + 120))
        #self.text_alarm1.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.text_alarm4.SetForegroundColour(wx.Colour(196, 56, 25))
        #self.text_alarm2.Hide()

        text = wx.StaticText(panel, label="Nombre quien firma: ", pos=(pos_ini_x - 120, pos_ini_y + 330))
        #text.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.signature = wx.TextCtrl(panel, pos=(pos_ini_x, pos_ini_y + 330), size=(250, 20),value = "", style=wx.TE_LEFT)
        self.text_alarm5 = wx.StaticText(panel,id = 5, label="* Campo requerido", pos=(pos_ini_x + 260, pos_ini_y + 330))
        #self.text_alarm1.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.text_alarm5.SetForegroundColour(wx.Colour(196, 56, 25))
        #self.text_alarm2.Hide()

        text = wx.StaticText(panel, label="Cédula: ", pos=(pos_ini_x - 100, pos_ini_y + 360))
        #text.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.cedula1 = wx.TextCtrl(panel, id = 11, pos=(pos_ini_x, pos_ini_y + 360), size=(50, 20),value = "", style=wx.TE_LEFT)
        self.cedula1.SetMaxLength(2)
        text = wx.StaticText(panel, label="-", pos=(pos_ini_x + 58, pos_ini_y + 360))
        #text.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.cedula2 = wx.TextCtrl(panel, id = 12, pos=(pos_ini_x + 70, pos_ini_y + 360), size=(50, 20),value = "", style=wx.TE_LEFT)
        self.cedula2.SetMaxLength(4)
        text = wx.StaticText(panel, label="-", pos=(pos_ini_x + 126, pos_ini_y + 360))
        #text.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.cedula3 = wx.TextCtrl(panel, id = 13, pos=(pos_ini_x + 140, pos_ini_y + 360), size=(50, 20),value = "", style=wx.TE_LEFT)
        self.cedula3.SetMaxLength(4)

        self.text_alarm6 = wx.StaticText(panel,id = 5, label="* Campo requerido (formato 9-9999-9999)", pos=(pos_ini_x + 200, pos_ini_y + 360))
        #self.text_alarm1.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.text_alarm6.SetForegroundColour(wx.Colour(196, 56, 25))



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
        self.my_btn_save.SetBackgroundColour((13, 52, 128))
        self.my_btn_save.SetForegroundColour(wx.Colour(255, 255, 255))
        #wx.EVT_ENTER_WINDOW(self, self.onMouseOver)
        #wx.EVT_LEAVE_WINDOW(self, self.onMouseLeave)

        self.my_btn_open = wx.Button(panel, label='Abrir', pos=(pos_ini_x + 120, pos_ini_y + 450), size=(100, 40))
        #self.my_btn_open.Disable()
        self.my_btn_open.SetBackgroundColour((13, 52, 128))
        self.my_btn_open.SetForegroundColour(wx.Colour(255, 255, 255))

        self.my_btn_save_n_send = wx.Button(panel, label='Guardar y Enviar', pos=(pos_ini_x + 290, pos_ini_y + 450), size=(100, 40))
        self.my_btn_save_n_send.Disable()
        self.my_btn_save_n_send.SetBackgroundColour((13, 52, 128))
        self.my_btn_save_n_send.SetForegroundColour(wx.Colour(255, 255, 255))

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
        #text.SetBackgroundColour(wx.Colour(255, 255, 255))
        text = wx.StaticText(panel, label="Build on: 2020-08-01", pos=(pos_ini_x-90, pos_ini_y + 520))
        #text.SetBackgroundColour(wx.Colour(255, 255, 255))
        text = wx.StaticText(panel, label="Last Update: 2020-08-04", pos=(pos_ini_x-90, pos_ini_y + 540))
        #text.SetBackgroundColour(wx.Colour(255, 255, 255))



        ### Set event handlers
        # Event for combo sucursal
        self.sucursal.Bind(wx.EVT_COMBOBOX, self.OnCombo)
        # Event Block only numbers for ID
        self.cedula1.Bind(wx.EVT_KEY_UP, self.block_non_numbers)
        self.cedula2.Bind(wx.EVT_KEY_UP, self.block_non_numbers)
        self.cedula3.Bind(wx.EVT_KEY_UP, self.block_non_numbers)
        # Event for other fields
        self.sendto.Bind(wx.EVT_KEY_UP , self.checkingFields)
        self.department.Bind(wx.EVT_KEY_UP , self.checkingFields)
        self.greetings.Bind(wx.EVT_KEY_UP , self.checkingFields)
        self.reason.Bind(wx.EVT_KEY_UP , self.checkingFields)
        self.signature.Bind(wx.EVT_KEY_UP , self.checkingFields)

        # Save button
        self.my_btn_save.Bind(wx.EVT_BUTTON, self.OnButtonSave)
        # Open Button
        self.my_btn_open.Bind(wx.EVT_BUTTON, self.OnButtonOpen)
        # Save and Send Button
        self.my_btn_save_n_send.Bind(wx.EVT_BUTTON, self.OnButtonSaveNSend)





        self.Show()

        current_dir = os.getcwd()

        #print ("Working on Dir: " + str(current_dir))

        # Style
        self.SetIcon(wx.Icon(current_dir + "/images/word_logo.png"))
        #self.SetIcon(wx.Icon.SetWidth(16))
        #self.SetIcon(wx.Icon.SetHeight(16))
        #self.wx.Icon(desiredWidth = 150, desiredHeight = 150)



        imageFile = current_dir + "/images/optica_rs_3.jpg"
        logo = wx.Image(imageFile, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        imageObj = wx.StaticBitmap(self, -1, logo, (-100, -105), (logo.GetWidth(), logo.GetHeight()))
        imageObj.SetPosition((pos_ini_x + 480, pos_ini_y -10))

        #imageFile = current_dir + "/images/optica_rs.jpg"
        #bitmap = scale_bitmap(imageFile, 300, 200)
        #logo = wx.Image(imageFile, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        #logo = wx.StaticBitmap(self, -1, logo, (-50, -30), (logo.GetWidth(), logo.GetHeight()))
        #logo.SetPosition((0,0))


        #self.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBackground)

        #wx.EVT_ENTER_WINDOW(self, self.onMouseOver)
        #wx.EVT_LEAVE_WINDOW(self, self.onMouseLeave)

    def onMouseOver(self, event):
        self.my_btn_save.SetBackgroundColour((255, 255, 255))
        self.my_btn_save.SetForegroundColour(wx.Colour(0, 0, 0))
        self.my_btn_clear_all.Refresh()

    def onMouseLeave(self, event):
        self.my_btn_save.SetBackgroundColour((13, 52, 128))
        self.my_btn_save.SetForegroundColour(wx.Colour(255, 255, 255))
        self.my_btn_clear_all.Refresh()

    def OnButtonSave(self, e):
        print ("Saving File ...")
        sucursal = self.sucursal.GetValue()
        sendto = self.sendto.GetValue()
        department = self.department.GetValue()
        greetings = self.greetings.GetValue()
        reason = self.reason.GetValue()
        signature = self.signature.GetValue()
        cedula1 = self.cedula1.GetValue()
        cedula2 = self.cedula2.GetValue()
        cedula3 = self.cedula3.GetValue()

        id = cedula1 + "-" + cedula2 + "-" + cedula3

        selection = self.sucursal.GetSelection()

        current_dir = os.getcwd()
        path_file= os.path.expanduser(current_dir + "/Templates/")

        letter.saving_word_letter(selection,sendto,department,greetings,reason,signature,id,path_file)

    def OnButtonOpen(self,e):
        print ("Open File...")
        current_dir = os.getcwd()
        path_file= os.path.expanduser(current_dir + "/Templates/")
        file_to_open = "carta_final.docx"
        os.startfile(path_file + file_to_open)

    def OnButtonSaveNSend(self, e):
        print ("Saving File and Sending to Email...")
        sucursal = self.sucursal.GetValue()
        sendto = self.sendto.GetValue()
        department = self.department.GetValue()
        greetings = self.greetings.GetValue()
        reason = self.reason.GetValue()
        signature = self.signature.GetValue()
        cedula1 = self.cedula1.GetValue()
        cedula2 = self.cedula2.GetValue()
        cedula3 = self.cedula3.GetValue()

        id = cedula1 + "-" + cedula2 + "-" + cedula3

        selection = self.sucursal.GetSelection()

        current_dir = os.getcwd()
        path_file= os.path.expanduser(current_dir + "/Templates/")

        letter.saving_word_letter(selection,sendto,department,greetings,reason,signature,id,path_file)


        final_file = "carta_final.docx"
        email.sending_email("jdrs2483@gmail.com", path_file + final_file)

    def OnCombo(self, event):
        #self.label.SetLabel("selected "+ self.combo.GetValue() +" from Combobox")
        negocio = self.sucursal.GetValue()
        #print (negocio)
        self.sendto.Enable()
        self.department.Enable()
        self.greetings.Enable()
        self.reason.Enable()
        self.signature.Enable()
        self.cedula1.Enable()
        self.cedula2.Enable()
        self.cedula3.Enable()

        self.text_alarm1.Hide()

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

        sucursal = self.sucursal.GetValue()
        sendto = self.sendto.GetValue()
        #greetings = self.greetings.GetValue()
        reason = self.reason.GetValue()
        signature = self.signature.GetValue()
        cedula1 = self.cedula1.GetValue()
        cedula2 = self.cedula2.GetValue()
        cedula3 = self.cedula3.GetValue()

        # Validation Messages
        if sendto != "" and len(sendto) > 3 :   self.text_alarm2.Hide()
        else:   self.text_alarm2.Show()
        if reason != "" and len(reason) > 5 :   self.text_alarm4.Hide()
        else:   self.text_alarm4.Show()
        if signature != "" and len(signature) > 3 :   self.text_alarm5.Hide()
        else:   self.text_alarm5.Show()
        if len(cedula1) >= 1 and len(cedula2) == 4 and len(cedula3) == 4:   self.text_alarm6.Hide()
        else:   self.text_alarm6.Show()

        #print ("Key: " + str(key_code))
        #print ("Cedula: " + cedula1 + "-" + cedula2 + "-" + cedula3)
        #print ("Length: " + len(cedula1) + "-" + len(cedula2) + "-" + len(cedula3))
        #selection = self.sucursal.GetSelection()

        # Which ID field is focused
        focused = wx.Window.FindFocus()

        if focused == self.cedula1:
            #print ("Field 1 is focused...")
            if chr(key_code) in ["0","1","2","3","4","5","6","7","8","9"] or key_code in (8, 127, 314, 316):
                #print ("Is a Digit...")
                cedula1 = self.cedula1.GetValue()
            else:
                cedula1 = self.cedula1.GetValue()
                if len(cedula1) != 2:
                    self.cedula1.SetValue(cedula1[:-1])
                elif cedula1[1].isalpha():
                    self.cedula1.SetValue(cedula1[:-1])
                self.cedula1.SetInsertionPointEnd()
                #print ("Is a Letter or symbol...")
        elif focused == self.cedula2:
            #print ("Field 2 is focused...")
            if chr(key_code) in ["0","1","2","3","4","5","6","7","8","9"] or key_code in (8, 127, 314, 316):
                #print ("Is a Digit...")
                cedula2 = self.cedula2.GetValue()
            else:
                cedula2 = self.cedula2.GetValue()
                if len(cedula2) != 4:
                    self.cedula2.SetValue(cedula2[:-1])
                elif cedula2[3].isalpha():
                    self.cedula2.SetValue(cedula2[:-1])
                    self.text_alarm6.Show()
                self.cedula2.SetInsertionPointEnd()
                #print ("Is a Letter or symbol...")
        elif focused == self.cedula3:
            #print ("Field 3 is focused...")
            if chr(key_code) in ["0","1","2","3","4","5","6","7","8","9"] or key_code in (8, 127, 314, 316):
                #print ("Is a Digit...")
                cedula3 = self.cedula3.GetValue()
            else:
                cedula3 = self.cedula3.GetValue()
                if len(cedula3) != 4:
                    self.cedula3.SetValue(cedula3[:-1])
                elif cedula3[3].isalpha():
                    self.cedula3.SetValue(cedula3[:-1])
                    self.text_alarm6.Show()
                self.cedula3.SetInsertionPointEnd()
                #print ("Is a Letter or symbol...")

        #print (focused)

        if sucursal != "" and sendto != "" and reason != "" and signature != "" and len(cedula1) != 0 and len(cedula2) == 4 and len(cedula3) == 4:
            self.my_btn_save.Enable()
            #self.my_btn_open.Enable()
            self.my_btn_save_n_send.Enable()
        else:
            self.my_btn_save.Disable()
            #self.my_btn_open.Disable()
            self.my_btn_save_n_send.Disable()



        #if key_code in (8, 127, 314, 316):
        #    event.Skip()
        #    return

        # Allow ASCII numerics
        #if ord('0') <= key_code <= ord('9'):
        #    event.Skip()
        #    return

    def checkingFields(self, event):
        key_code = event.GetKeyCode()

        #print ("Key: " + str(key_code))

        sucursal = self.sucursal.GetValue()
        sendto = self.sendto.GetValue()
        #greetings = self.greetings.GetValue()
        reason = self.reason.GetValue()
        signature = self.signature.GetValue()
        cedula1 = self.cedula1.GetValue()
        cedula2 = self.cedula2.GetValue()
        cedula3 = self.cedula3.GetValue()

        #print ("Send to: " + sendto)

        # Validation Messages
        if sendto != "" and len(sendto) > 3 :   self.text_alarm2.Hide()
        else:   self.text_alarm2.Show()
        if reason != "" and len(reason) > 5 :   self.text_alarm4.Hide()
        else:   self.text_alarm4.Show()
        if signature != "" and len(signature) > 3 :   self.text_alarm5.Hide()
        else:   self.text_alarm5.Show()
        if len(cedula1) >= 1 and len(cedula2) == 4 and len(cedula3) == 4:   self.text_alarm6.Hide()
        else:   self.text_alarm6.Show()

        #key = ord(key_code)
        #print (key_code)
        #print ("Digit: " + chr(key_code))


        if sucursal != "" and sendto != ""  and reason != "" and signature != "" and len(cedula1) != 0 and len(cedula2) != 4 and len(cedula3) != 4:
            self.my_btn_save.Enable()
            #self.my_btn_open.Enable()
            self.my_btn_save_n_send.Enable()
        else:
            self.my_btn_save.Disable()
            #self.my_btn_open.Disable()
            self.my_btn_save_n_send.Disable()

        return

if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame()
    app.MainLoop()
