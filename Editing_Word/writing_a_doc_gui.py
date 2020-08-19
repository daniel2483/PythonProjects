# pip install wxpython
#   Word Letter Editor
#   Made by: Jose Daniel Rodriguez Sanchez
#   Build on: 2020-08-01
#   Last Update: 2020-08-19


import wx
import re
import os
import writing_a_doc_module as letter
import send_email_to_gmail_account_module as email
import wx.grid as grid


# from wx.lib.masked import NumCtrl
# from PIL import Image


# from mailmerge import MailMerge
# from datetime import date
# import os

class dialogBox(wx.Dialog):
    def __init__(self, parent, title):
        super(dialogBox, self).__init__(parent, title=title, size=(410, 200))
        panel = wx.Panel(self)

        font = wx.Font(10, wx.DECORATIVE, wx.NORMAL, wx.NORMAL)

        self.label_0 = wx.StaticText(panel, id=1, label="Email de lista:", pos=(10, 20))
        email_list = ['alerosan@gmail.com', 'jdrs2483@gmail.com', 'jdrs2483@yahoo.com']
        self.email_list = wx.ComboBox(panel, value="", pos=(110, 20), size=(150, 25), choices=email_list,
                                      style=wx.CB_DROPDOWN | wx.TE_READONLY)

        # self.label_1 = wx.StaticText(panel,id = 3, label="Solamente direcciones gmail..." , pos = (50,20))
        self.label_1 = wx.StaticText(panel, id=1, label="Email: ", pos=(10, 50))
        self.email = wx.TextCtrl(panel, id=2, size=(150, 25), pos=(110, 50))
        self.text_alarm1 = wx.StaticText(panel, id=1, label="* Campo requerido", pos=(275, 50))
        self.text_alarm1.SetForegroundColour(wx.Colour(196, 56, 25))

        # self.btn = wx.Button(panel, wx.ID_OK, label = "ok", size = (50,20), pos = (75,50))

        # self.Bind ( wx.EVT_CLOSE, self.on_close )
        # self.SetSizerAndFit ( self.CreateButtonSizer ( wx.OK|wx.CANCEL ) )

        self.label_0.SetFont(font)
        self.email_list.SetFont(font)
        self.label_1.SetFont(font)
        self.email.SetFont(font)
        self.text_alarm1.SetFont(font)

        self.my_btn_ok = wx.Button(panel, label='OK', pos=(75, 90), size=(100, 40))
        # self.my_btn_open.Disable()
        self.my_btn_ok.SetBackgroundColour((13, 52, 128))
        self.my_btn_ok.SetForegroundColour(wx.Colour(255, 255, 255))

        self.my_btn_ok.Bind(wx.EVT_BUTTON, self.OnButtonOK)
        self.my_btn_ok.Disable()

        self.email.Bind(wx.EVT_KEY_UP, self.checkingEmail)

        self.email_list.Bind(wx.EVT_COMBOBOX, self.OnComboEmail)

    # def on_close ( self, event ):
    # print ("hello from on_close!")
    # self.Destroy()

    def OnButtonOK(self, event):
        current_dir = os.getcwd()
        path_file = os.path.expanduser(current_dir + "/Templates/")

        email_list = self.email.GetValue()

        final_file = "carta_final.docx"

        print("Sending Email to " + email_list)

        email.sending_email(email_list, path_file + final_file)

        # Destroy Dialog Box
        self.Destroy()

    def checkingEmail(self, event):
        # key_code = event.GetKeyCode()

        email = self.email.GetValue()

        # Validation Email
        # regex = '^[a-z0-9.]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        regex = '^[a-z0-9.]+[\._]?[a-z0-9]+[@]\w+[.][a-z0-9.]{2,}$'

        if re.search(regex, email):
            # print("Valid Email")
            self.my_btn_ok.Enable()
            self.text_alarm1.Hide()
        else:
            # print("Invalid Email")
            self.my_btn_ok.Disable()
            self.text_alarm1.Show()

        return

    def OnComboEmail(self, event):
        # self.label.SetLabel("selected "+ self.combo.GetValue() +" from Combobox")
        email = self.email_list.GetValue()
        # print (email)
        self.email.SetValue(email)
        self.text_alarm1.Hide()
        self.my_btn_ok.Enable()


class MyFrame(wx.Frame):

    def __init__(self):
        super().__init__(parent=None, title='App Cartas Rosan', size=(800, 620))
        panel = wx.Panel(self)

        self.SetBackgroundStyle(wx.BG_STYLE_CUSTOM)
        self.SetBackgroundColour('WHITE')
        # self.frame = parent

        font = wx.Font(10, wx.DECORATIVE, wx.NORMAL, wx.NORMAL)

        # self.wx.Frame.
        # pos=(x,y)

        pos_ini_y = 10
        pos_ini_x = 150

        self.text1 = wx.StaticText(panel, label="Elija Sucursal: ", pos=(pos_ini_x - 120, pos_ini_y))
        # text.SetBackgroundColour(wx.Colour(255, 255, 255))
        sucursales = ['1. Óptica Nueva Imagen.', '2. Óptica Rosan Banco Nacional.', '3. Óptica Rosan Parque Central.']
        self.sucursal = wx.ComboBox(panel, value="", pos=(pos_ini_x, pos_ini_y), size=(250, 25), choices=sucursales,
                                    style=wx.CB_DROPDOWN | wx.TE_READONLY)
        self.text_alarm1 = wx.StaticText(panel, id=1, label="* Campo requerido", pos=(pos_ini_x + 260, pos_ini_y))
        # self.text_alarm1.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.text_alarm1.SetForegroundColour(wx.Colour(196, 56, 25))

        self.text2 = wx.StaticText(panel, label="Carta dirigida a: ", pos=(pos_ini_x - 120, pos_ini_y + 30))
        # text.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.sendto = wx.TextCtrl(panel, pos=(pos_ini_x, pos_ini_y + 30), size=(250, 25), value="", style=wx.TE_LEFT)
        self.text_alarm2 = wx.StaticText(panel, id=2, label="* Campo requerido", pos=(pos_ini_x + 260, pos_ini_y + 30))
        # self.text_alarm1.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.text_alarm2.SetForegroundColour(wx.Colour(196, 56, 25))
        # self.text_alarm2.Hide()

        self.text3 = wx.StaticText(panel, label="Departamento: ", pos=(pos_ini_x - 120, pos_ini_y + 60))
        # text.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.department = wx.TextCtrl(panel, pos=(pos_ini_x, pos_ini_y + 60), size=(250, 25), value="",
                                      style=wx.TE_LEFT)

        self.text4 = wx.StaticText(panel, label="Saludo Inicial: ", pos=(pos_ini_x - 120, pos_ini_y + 90))
        # text.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.greetings = wx.TextCtrl(panel, pos=(pos_ini_x, pos_ini_y + 90), size=(250, 25), value="", style=wx.TE_LEFT)
        # self.text_alarm3 = wx.StaticText(panel,id = 2, label="* Campo requerido", pos=(pos_ini_x + 260, pos_ini_y + 90))
        # self.text_alarm1.SetBackgroundColour(wx.Colour(255, 255, 255))
        # self.text_alarm3.SetForegroundColour(wx.Colour(196, 56, 25))
        # self.text_alarm2.Hide()

        self.text5 = wx.StaticText(panel, label="Razón de la carta: ", pos=(pos_ini_x - 120, pos_ini_y + 120))
        # text.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.reason = wx.TextCtrl(panel, pos=(pos_ini_x, pos_ini_y + 120), size=(470, 140), value="",
                                  style=wx.TE_LEFT | wx.TE_MULTILINE)
        self.text_alarm4 = wx.StaticText(panel, id=4, label="* Campo requerido", pos=(pos_ini_x + 480, pos_ini_y + 120))
        # self.text_alarm1.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.text_alarm4.SetForegroundColour(wx.Colour(196, 56, 25))
        # self.text_alarm2.Hide()

        ################# Formulario para recetas ########################

        self.text_combo_mediciones = wx.StaticText(panel, label="Agregar Receta: ",
                                                   pos=(pos_ini_x - 120, pos_ini_y + 270))
        opciones = ['Si', 'No']
        self.mediciones = wx.ComboBox(panel, value="No", pos=(pos_ini_x, pos_ini_y + 270), size=(40, 25),
                                      choices=opciones, style=wx.CB_DROPDOWN | wx.TE_READONLY)
        self.mediciones.Disable()

        # self.GridPanel = wx.Panel(self)
        self.mygrid = grid.Grid(panel, pos=(pos_ini_x + 50, pos_ini_y + 270))
        self.mygrid.CreateGrid(2, 4)
        # self.mygrid.SetSize(220, 3000)

        (w, h) = self.mygrid.GetBestSize()
        print(str(w) + "   " + str(h))

        # sizer = wx.BoxSizer(wx.HORIZONTAL)
        # sizer.Add(self.mygrid, -1, wx.EXPAND)
        # self.SetSizer(sizer)

        # change a couple column labels
        # mygrid.SetColLabelValue(0, "").
        self.mygrid.SetColLabelValue(0, "     Esfera     ")
        self.mygrid.SetColLabelValue(1, "    Cilindro    ")
        self.mygrid.SetColLabelValue(2, "      Eje       ")
        self.mygrid.SetColLabelValue(3, "      A.V.      ")

        # Change Row labels
        # mygrid.SetRowLabelValue(0, "")
        self.mygrid.SetRowLabelValue(0, "Ojo I.")
        self.mygrid.SetRowLabelValue(1, "Ojo D.")

        self.mygrid.AutoSize()
        self.mygrid.SetColSize(0, 100)
        self.mygrid.SetColSize(1, 100)
        self.mygrid.SetColSize(2, 100)
        self.mygrid.SetColSize(3, 100)

        self.mygrid.SetRowSize(0, 25)
        self.mygrid.SetRowSize(1, 25)

        self.mygrid.AutoSize()
        self.mygrid.DisableDragGridSize()

        self.mygrid.Disable()

        # self.mygrid.EnableScrolling(False, False)
        ################# Fin formulario para recetas ####################

        self.text_cedula_combo = wx.StaticText(panel, id=22, label="Lista de Cédulas",
                                               pos=(pos_ini_x - 120, pos_ini_y + 360))
        ids = ['Alejandro Rodríguez Sánchez | 2-0626-0889 | 066-530',
               'Gladys Rodríguez Sánchez | 9-9999-9999 | 999-999',
               'Fabio Rodríguez González | 6-0106-1307 | 999-999',
               'Fabiola Rodríguez Sánchez | 2-0698-0165 | 066-799',
               'Daniel Rodríguez Sánchez | 1-1172-0707 | 999-999']
        self.ids = wx.ComboBox(panel, value="", pos=(pos_ini_x, pos_ini_y + 360), size=(270, 25), choices=ids,
                               style=wx.CB_DROPDOWN | wx.TE_READONLY)

        self.text6 = wx.StaticText(panel, label="Nombre quien firma: ", pos=(pos_ini_x - 120, pos_ini_y + 390))
        # text.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.signature = wx.TextCtrl(panel, pos=(pos_ini_x, pos_ini_y + 390), size=(250, 25), value="",
                                     style=wx.TE_LEFT)
        self.text_alarm5 = wx.StaticText(panel, id=5, label="* Campo requerido", pos=(pos_ini_x + 260, pos_ini_y + 390))
        # self.text_alarm1.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.text_alarm5.SetForegroundColour(wx.Colour(196, 56, 25))
        # self.text_alarm2.Hide()

        self.text7 = wx.StaticText(panel, label="Cédula: ", pos=(pos_ini_x - 120, pos_ini_y + 420))
        # text.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.cedula1 = wx.TextCtrl(panel, id=11, pos=(pos_ini_x, pos_ini_y + 420), size=(50, 25), value="",
                                   style=wx.TE_LEFT)
        self.cedula1.SetMaxLength(2)
        self.text8 = wx.StaticText(panel, label="-", pos=(pos_ini_x + 58, pos_ini_y + 420))
        # text.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.cedula2 = wx.TextCtrl(panel, id=12, pos=(pos_ini_x + 70, pos_ini_y + 420), size=(50, 25), value="",
                                   style=wx.TE_LEFT)
        self.cedula2.SetMaxLength(4)
        self.text9 = wx.StaticText(panel, label="-", pos=(pos_ini_x + 126, pos_ini_y + 420))
        # text.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.cedula3 = wx.TextCtrl(panel, id=13, pos=(pos_ini_x + 140, pos_ini_y + 420), size=(50, 25), value="",
                                   style=wx.TE_LEFT)
        self.cedula3.SetMaxLength(4)

        self.text_alarm6 = wx.StaticText(panel, id=5, label="* Campo requerido (formato 9-9999-9999)",
                                         pos=(pos_ini_x + 200, pos_ini_y + 420))
        # self.text_alarm1.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.text_alarm6.SetForegroundColour(wx.Colour(196, 56, 25))

        # First Status disable when no sucursal is selected
        self.sendto.Disable()
        self.department.Disable()
        self.greetings.Disable()
        self.reason.Disable()
        self.signature.Disable()
        self.ids.Disable()
        self.cedula1.Disable()
        self.cedula2.Disable()
        self.cedula3.Disable()

        self.my_btn_save = wx.Button(panel, label='Guardar', pos=(pos_ini_x - 50, pos_ini_y + 450), size=(100, 40))
        self.my_btn_save.Disable()
        self.my_btn_save.SetBackgroundColour((13, 52, 128))
        self.my_btn_save.SetForegroundColour(wx.Colour(255, 255, 255))
        # wx.EVT_ENTER_WINDOW(self, self.onMouseOver)
        # wx.EVT_LEAVE_WINDOW(self, self.onMouseLeave)

        self.my_btn_open = wx.Button(panel, label='Abrir', pos=(pos_ini_x + 120, pos_ini_y + 450), size=(100, 40))
        # self.my_btn_open.Disable()
        self.my_btn_open.SetBackgroundColour((13, 52, 128))
        self.my_btn_open.SetForegroundColour(wx.Colour(255, 255, 255))

        self.my_btn_save_n_send = wx.Button(panel, label='Guardar y Enviar', pos=(pos_ini_x + 290, pos_ini_y + 450),
                                            size=(100, 40))
        self.my_btn_save_n_send.Disable()
        self.my_btn_save_n_send.SetBackgroundColour((13, 52, 128))
        self.my_btn_save_n_send.SetForegroundColour(wx.Colour(255, 255, 255))

        self.my_btn_send = wx.Button(panel, label='Enviar', pos=(pos_ini_x + 460, pos_ini_y + 450), size=(100, 40))
        # self.my_btn_save_n_send.Disable()
        self.my_btn_send.SetBackgroundColour((13, 52, 128))
        self.my_btn_send.SetForegroundColour(wx.Colour(255, 255, 255))

        # Font style and size
        self.text1.SetFont(font)
        self.sucursal.SetFont(font)
        self.text_alarm1.SetFont(font)

        self.text2.SetFont(font)
        self.sendto.SetFont(font)
        self.text_alarm2.SetFont(font)

        self.text3.SetFont(font)
        self.department.SetFont(font)

        self.greetings.SetFont(font)

        self.text4.SetFont(font)
        self.text_alarm4.SetFont(font)
        self.reason.SetFont(font)
        self.text5.SetFont(font)

        self.text_alarm5.SetFont(font)
        self.signature.SetFont(font)
        self.text6.SetFont(font)

        self.text_combo_mediciones.SetFont(font)
        self.mediciones.SetFont(font)
        self.mygrid.SetFont(font)

        self.text_cedula_combo.SetFont(font)
        self.ids.SetFont(font)

        self.text7.SetFont(font)
        self.text8.SetFont(font)
        self.text9.SetFont(font)
        self.cedula1.SetFont(font)
        self.cedula2.SetFont(font)
        self.cedula3.SetFont(font)
        self.text_alarm6.SetFont(font)

        # self.label_1.SetFont(font)
        # self.email.SetFont(font)
        # self.text_alarm1.SetFont(font)
        # Results
        # self.operation = wx.StaticText(panel, label="", pos=(pos_ini_x + 175, pos_ini_y))
        # self.result = wx.StaticText(panel, label="", pos=(200, pos_ini_y + 90))
        # self.result.SetForegroundColour(wx.RED)
        # self.operation.SetForegroundColour(wx.RED)

        ## Setting Font Size Style
        # font = wx.Font(18, wx.DECORATIVE, wx.ITALIC, wx.NORMAL) -- wx.BOLD
        # font = wx.Font(16, wx.DECORATIVE, wx.NORMAL, wx.BOLD)
        # self.operation.SetFont(font)

        # fontButton = wx.Font(11, wx.DECORATIVE, wx.NORMAL, wx.BOLD)

        text = wx.StaticText(panel, label="Made by: Jose Daniel Rodríguez Sánchez",
                             pos=(pos_ini_x - 90, pos_ini_y + 500))
        fontCredits = wx.Font(8, wx.DECORATIVE, wx.ITALIC, wx.BOLD)
        text.SetFont(fontCredits)
        # text.SetBackgroundColour(wx.Colour(255, 255, 255))
        text = wx.StaticText(panel, label="Build on: 2020-08-01", pos=(pos_ini_x - 90, pos_ini_y + 520))
        text.SetFont(fontCredits)
        # text.SetBackgroundColour(wx.Colour(255, 255, 255))
        text = wx.StaticText(panel, label="Last Update: 2020-08-19", pos=(pos_ini_x - 90, pos_ini_y + 540))
        text.SetFont(fontCredits)
        # text.SetBackgroundColour(wx.Colour(255, 255, 255))

        ### Set event handlers
        # Event for combo sucursal
        self.sucursal.Bind(wx.EVT_COMBOBOX, self.OnCombo)
        # Event Block only numbers for ID
        self.cedula1.Bind(wx.EVT_KEY_UP, self.block_non_numbers)
        self.cedula2.Bind(wx.EVT_KEY_UP, self.block_non_numbers)
        self.cedula3.Bind(wx.EVT_KEY_UP, self.block_non_numbers)
        # Event for other fields
        self.sendto.Bind(wx.EVT_KEY_UP, self.checkingFields)
        self.department.Bind(wx.EVT_KEY_UP, self.checkingFields)
        self.greetings.Bind(wx.EVT_KEY_UP, self.checkingFields)
        self.reason.Bind(wx.EVT_KEY_UP, self.checkingFields)
        self.signature.Bind(wx.EVT_KEY_UP, self.checkingFields)

        # Event for Yes/No Combo
        self.mediciones.Bind(wx.EVT_COMBOBOX, self.OnComboMed)

        # Event for Ids Combo
        self.ids.Bind(wx.EVT_COMBOBOX, self.OnComboIds)

        # Save button
        self.my_btn_save.Bind(wx.EVT_BUTTON, self.OnButtonSave)
        # Open Button
        self.my_btn_open.Bind(wx.EVT_BUTTON, self.OnButtonOpen)
        # Save and Send Button
        self.my_btn_save_n_send.Bind(wx.EVT_BUTTON, self.OnButtonSaveNSend)
        # Only Send Last letter created
        self.my_btn_send.Bind(wx.EVT_BUTTON, self.OnButtonSendLastLetter)

        self.Show()

        current_dir = os.getcwd()

        # print ("Working on Dir: " + str(current_dir))

        # Style
        self.SetIcon(wx.Icon(current_dir + "/images/word_logo.png"))
        # self.SetIcon(wx.Icon.SetWidth(16))
        # self.SetIcon(wx.Icon.SetHeight(16))
        # self.wx.Icon(desiredWidth = 150, desiredHeight = 150)

        imageFile = current_dir + "/images/optica_ni_2.jpg"
        logo = wx.Image(imageFile, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        imageObj = wx.StaticBitmap(self, -1, logo, (-100, -105), (logo.GetWidth(), logo.GetHeight()))
        imageObj.SetPosition((pos_ini_x + 379, pos_ini_y - 10))

        imageFile = current_dir + "/images/optica_rs_3.jpg"
        logo = wx.Image(imageFile, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        imageObj = wx.StaticBitmap(self, -1, logo, (-100, -105), (logo.GetWidth(), logo.GetHeight()))
        imageObj.SetPosition((pos_ini_x + 510, pos_ini_y - 10))

        # imageFile = current_dir + "/images/optica_rs.jpg"
        # bitmap = scale_bitmap(imageFile, 300, 200)
        # logo = wx.Image(imageFile, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        # logo = wx.StaticBitmap(self, -1, logo, (-50, -30), (logo.GetWidth(), logo.GetHeight()))
        # logo.SetPosition((0,0))

        # wx.EVT_ENTER_WINDOW(self, self.onMouseOver)
        # wx.EVT_LEAVE_WINDOW(self, self.onMouseLeave)

    # def onMouseOver(self, event):
    # self.my_btn_save.SetBackgroundColour((255, 255, 255))
    # self.my_btn_save.SetForegroundColour(wx.Colour(0, 0, 0))
    # self.my_btn_clear_all.Refresh()

    # def onMouseLeave(self, event):
    # self.my_btn_save.SetBackgroundColour((13, 52, 128))
    # self.my_btn_save.SetForegroundColour(wx.Colour(255, 255, 255))
    # self.my_btn_clear_all.Refresh()

    def OnButtonSave(self, e):
        print("Saving File ...")
        sendto = self.sendto.GetValue()
        department = self.department.GetValue()
        greetings = self.greetings.GetValue()
        reason = self.reason.GetValue()
        signature = self.signature.GetValue()
        cedula1 = self.cedula1.GetValue()
        cedula2 = self.cedula2.GetValue()
        cedula3 = self.cedula3.GetValue()

        id = cedula1 + "-" + cedula2 + "-" + cedula3

        sphere_l = self.mygrid.GetCellValue(0, 0)
        sphere_r = self.mygrid.GetCellValue(1, 0)
        cylinder_l = self.mygrid.GetCellValue(0, 1)
        cylinder_r = self.mygrid.GetCellValue(1, 1)
        axis_l = self.mygrid.GetCellValue(0, 2)
        axis_r = self.mygrid.GetCellValue(1, 2)
        av_l = self.mygrid.GetCellValue(0, 3)
        av_r = self.mygrid.GetCellValue(1, 3)

        selection = self.sucursal.GetSelection()

        current_dir = os.getcwd()
        path_file = os.path.expanduser(current_dir + "/Templates/")

        mediciones_flag = self.mediciones.GetValue()
        try:
            if mediciones_flag == "Si":
                letter.saving_word_letter_mediciones(selection, sendto, department, greetings, reason, signature,
                                                     id, sphere_l, sphere_r, cylinder_l, cylinder_r,
                                                     axis_l, axis_r, av_l, av_r, path_file)
            if mediciones_flag == "No":
                letter.saving_word_letter(selection, sendto, department, greetings, reason, signature,
                                          id, path_file)
            wx.MessageBox('Archivo Guardado', 'Información', wx.OK | wx.ICON_INFORMATION)
        except PermissionError:
            wx.MessageBox('El documento se encuentra abierto y No se ha Guardado', 'Error de permisos',
                          wx.OK | wx.ICON_ERROR)

    def OnButtonOpen(self, e):
        # print("Open File...")
        current_dir = os.getcwd()
        path_file = os.path.expanduser(current_dir + "/Templates/")
        file_to_open = "carta_final.docx"
        # os.close(path_file + file_to_open)
        os.startfile(path_file + file_to_open)

    def OnButtonSaveNSend(self, e):
        print("Saving File and Sending to Email...")

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

        sphere_l = self.mygrid.GetCellValue(0, 0)
        sphere_r = self.mygrid.GetCellValue(1, 0)
        cylinder_l = self.mygrid.GetCellValue(0, 1)
        cylinder_r = self.mygrid.GetCellValue(1, 1)
        axis_l = self.mygrid.GetCellValue(0, 2)
        axis_r = self.mygrid.GetCellValue(1, 2)
        av_l = self.mygrid.GetCellValue(0, 3)
        av_r = self.mygrid.GetCellValue(1, 3)

        selection = self.sucursal.GetSelection()

        current_dir = os.getcwd()
        path_file = os.path.expanduser(current_dir + "/Templates/")

        mediciones_flag = self.mediciones.GetValue()

        try:
            if mediciones_flag == "Si":
                letter.saving_word_letter_mediciones(selection, sendto, department, greetings, reason, signature,
                                                     id, sphere_l, sphere_r, cylinder_l, cylinder_r,
                                                     axis_l, axis_r, av_l, av_r, path_file)
            if mediciones_flag == "No":
                letter.saving_word_letter(selection, sendto, department, greetings, reason, signature,
                                          id, path_file)

            wx.MessageBox('Archivo Guardado', 'Información', wx.OK | wx.ICON_INFORMATION)

            a = dialogBox(self, "Dialog").ShowModal()
        except PermissionError:
            wx.MessageBox('El documento se encuentra abierto y No se ha Guardado', 'Error de permisos',
                          wx.OK | wx.ICON_ERROR)

        # final_file = "carta_final.docx"

    def OnButtonSendLastLetter(self, e):
        # print("Sending last letter to Email...")

        a = dialogBox(self, "Dialog").ShowModal()

        # final_file = "carta_final.docx"
        # email.sending_email("jdrs2483@gmail.com", path_file + final_file)

    def OnCombo(self, event):
        # self.label.SetLabel("selected "+ self.combo.GetValue() +" from Combobox")
        negocio = self.sucursal.GetValue()
        # print (negocio)
        self.sendto.Enable()
        self.department.Enable()
        self.greetings.Enable()
        self.reason.Enable()
        self.signature.Enable()
        self.mediciones.Enable()
        self.ids.Enable()
        self.cedula1.Enable()
        self.cedula2.Enable()
        self.cedula3.Enable()

        self.text_alarm1.Hide()

    def block_non_numbers(self, event):
        key_code = event.GetKeyCode()

        sucursal = self.sucursal.GetValue()
        sendto = self.sendto.GetValue()
        # greetings = self.greetings.GetValue()
        reason = self.reason.GetValue()
        signature = self.signature.GetValue()
        cedula1 = self.cedula1.GetValue()
        cedula2 = self.cedula2.GetValue()
        cedula3 = self.cedula3.GetValue()

        # Validation Messages
        if sendto != "" and len(sendto) > 3:
            self.text_alarm2.Hide()
        else:
            self.text_alarm2.Show()
        if reason != "" and len(reason) > 5:
            self.text_alarm4.Hide()
        else:
            self.text_alarm4.Show()
        if signature != "" and len(signature) > 3:
            self.text_alarm5.Hide()
        else:
            self.text_alarm5.Show()
        if len(cedula1) >= 1 and len(cedula2) == 4 and len(cedula3) == 4:
            self.text_alarm6.Hide()
        else:
            self.text_alarm6.Show()

        # print ("Key: " + str(key_code))
        # print ("Cedula: " + cedula1 + "-" + cedula2 + "-" + cedula3)
        # print ("Length: " + len(cedula1) + "-" + len(cedula2) + "-" + len(cedula3))
        # selection = self.sucursal.GetSelection()

        # Which ID field is focused
        focused = wx.Window.FindFocus()

        if focused == self.cedula1:
            # print ("Field 1 is focused...")
            if chr(key_code) in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"] or key_code in (8, 127, 314, 316):
                # print ("Is a Digit...")
                cedula1 = self.cedula1.GetValue()
            else:
                cedula1 = self.cedula1.GetValue()
                if len(cedula1) != 2:
                    self.cedula1.SetValue(cedula1[:-1])
                elif cedula1[1].isalpha():
                    self.cedula1.SetValue(cedula1[:-1])
                self.cedula1.SetInsertionPointEnd()
                # print ("Is a Letter or symbol...")
        elif focused == self.cedula2:
            # print ("Field 2 is focused...")
            if chr(key_code) in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"] or key_code in (8, 127, 314, 316):
                # print ("Is a Digit...")
                cedula2 = self.cedula2.GetValue()
            else:
                cedula2 = self.cedula2.GetValue()
                if len(cedula2) != 4:
                    self.cedula2.SetValue(cedula2[:-1])
                elif cedula2[3].isalpha():
                    self.cedula2.SetValue(cedula2[:-1])
                    self.text_alarm6.Show()
                self.cedula2.SetInsertionPointEnd()
                # print ("Is a Letter or symbol...")
        elif focused == self.cedula3:
            # print ("Field 3 is focused...")
            if chr(key_code) in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"] or key_code in (8, 127, 314, 316):
                # print ("Is a Digit...")
                cedula3 = self.cedula3.GetValue()
            else:
                cedula3 = self.cedula3.GetValue()
                if len(cedula3) != 4:
                    self.cedula3.SetValue(cedula3[:-1])
                elif cedula3[3].isalpha():
                    self.cedula3.SetValue(cedula3[:-1])
                    self.text_alarm6.Show()
                self.cedula3.SetInsertionPointEnd()
                # print ("Is a Letter or symbol...")

        # print (focused)

        if sucursal != "" and sendto != "" and reason != "" and signature != "" and len(cedula1) != 0 and len(
                cedula2) == 4 and len(cedula3) == 4:
            self.my_btn_save.Enable()
            # self.my_btn_open.Enable()
            self.my_btn_save_n_send.Enable()
        else:
            self.my_btn_save.Disable()
            # self.my_btn_open.Disable()
            self.my_btn_save_n_send.Disable()

        # if key_code in (8, 127, 314, 316):
        #    event.Skip()
        #    return

        # Allow ASCII numerics
        # if ord('0') <= key_code <= ord('9'):
        #    event.Skip()
        #    return

    def checkingFields(self, event):
        key_code = event.GetKeyCode()

        # print ("Key: " + str(key_code))

        sucursal = self.sucursal.GetValue()
        sendto = self.sendto.GetValue()
        # greetings = self.greetings.GetValue()
        reason = self.reason.GetValue()
        signature = self.signature.GetValue()
        cedula1 = self.cedula1.GetValue()
        cedula2 = self.cedula2.GetValue()
        cedula3 = self.cedula3.GetValue()

        # print ("Send to: " + sendto)

        # Validation Messages
        if sendto != "" and len(sendto) > 3:
            self.text_alarm2.Hide()
        else:
            self.text_alarm2.Show()
        if reason != "" and len(reason) > 5:
            self.text_alarm4.Hide()
        else:
            self.text_alarm4.Show()
        if signature != "" and len(signature) > 3:
            self.text_alarm5.Hide()
        else:
            self.text_alarm5.Show()
        if len(cedula1) >= 1 and len(cedula2) == 4 and len(cedula3) == 4:
            self.text_alarm6.Hide()
        else:
            self.text_alarm6.Show()

        # key = ord(key_code)
        # print (key_code)
        # print ("Digit: " + chr(key_code))

        if sucursal != "" and sendto != "" and reason != "" and signature != "" and len(cedula1) > 0 and len(
                cedula2) == 4 and len(cedula3) == 4:
            self.my_btn_save.Enable()
            # self.my_btn_open.Enable()
            self.my_btn_save_n_send.Enable()
        else:
            self.my_btn_save.Disable()
            # self.my_btn_open.Disable()
            self.my_btn_save_n_send.Disable()

        return

    def ShowMessage(self):
        wx.MessageBox('Archivo Guardado', 'Info', wx.OK | wx.ICON_INFORMATION)

    def OnComboIds(self, event):
        id = self.ids.GetValue()
        name, ced = id.split(' | ')
        print("Changing ID..." + ced)

        self.signature.SetValue(name)
        self.text_alarm5.Hide()

        cedula1, cedula2, cedula3 = ced.split('-')

        self.cedula1.SetValue(cedula1)
        self.cedula2.SetValue(cedula2)
        self.cedula3.SetValue(cedula3)

        self.text_alarm6.Hide()

        # Validating fields
        sucursal = self.sucursal.GetValue()
        sendto = self.sendto.GetValue()
        # greetings = self.greetings.GetValue()
        reason = self.reason.GetValue()
        signature = self.signature.GetValue()
        cedula1 = self.cedula1.GetValue()
        cedula2 = self.cedula2.GetValue()
        cedula3 = self.cedula3.GetValue()

        if sucursal != "" and sendto != "" and reason != "" and signature != "" and len(cedula1) > 0 and len(
                cedula2) == 4 and len(cedula3) == 4:
            self.my_btn_save.Enable()
            # self.my_btn_open.Enable()
            self.my_btn_save_n_send.Enable()
        else:
            self.my_btn_save.Disable()
            # self.my_btn_open.Disable()
            self.my_btn_save_n_send.Disable()

    def OnComboMed(self, event):
        print("Combo is Working....")
        question = self.mediciones.GetValue()

        if question == "Si":
            self.mygrid.Enable()
        else:
            self.mygrid.Disable()


if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame()
    app.MainLoop()
