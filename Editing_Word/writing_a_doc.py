import win32com.client

# This line actually creates a Word object in memory. You should be
# able to see winword.exe in Taskmanager at this point.
word = win32com.client.Dispatch("Word.Application")

# Word is started in the background. This line brings makes its main
# (empty) window visible.
word.visible = 1

# This instruction creates a new Word document ! Yes, it *is* that easy.
doc = word.Documents.Add()

# This function writes an initial text to the document.
doc.Range().Text = "Hello, world"
