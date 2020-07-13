import win32com.client

# This line actually creates a Word object in memory. You should be
# able to see winword.exe in Taskmanager at this point.
word = win32com.client.Dispatch("Word.Application")

# Word is started in the background. This line brings makes its main
# (empty) window visible.
word.visible = 1

# This instruction creates a new Word document ! Yes, it *is* that easy.
doc = word.Documents.Add()

doc.PageSetup.Orientation = 1 # Make some Setup to the Document:
doc.PageSetup.LeftMargin = 200
doc.PageSetup.TopMargin = 20
doc.PageSetup.BottomMargin = 20
doc.PageSetup.RightMargin = 20
doc.Content.Font.Size = 40
doc.Content.Paragraphs.TabStops.Add (100)
doc.Content.Text = "Hello, I am a text!"
doc.Content.MoveEnd

# This function writes an initial text to the document.
#doc.Range().Text = "Hello, world"
