import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image

root= tk.Tk()
root.title("PNG To JPG By HHK")
canvas1 = tk.Canvas(root, width=300, height=250, bg='lightsteelblue2', relief='raised')
canvas1.pack()



label1 = tk.Label(root, text='
 Tool', bg='lightsteelblue2')
label1.config(font=('helvetica', 20))
canvas1.create_window(150, 50, window=label1)


def getJPG():
    global im1

    import_file_path = filedialog.askopenfilename()
    im1 = Image.open(import_file_path)


browseButton_PNG = tk.Button(text="      Import   PNG   File     ", command=getPNG, bg='royalblue', fg='white',
                             font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 120, window=browseButton_PNG)


def convertToJPG():
    global im1

    export_file_path = filedialog.asksaveasfilename(defaultextension='.jpg')
    im1.save(export_file_path)


saveAsButton_JPG = tk.Button(text=' Convert  PNG To JPG ', command=convertToJPG, bg='royalblue', fg='white',
                             font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 180, window=saveAsButton_JPG)

root.mainloop()