from tkinter import *
from tkinter.ttk import *
from PIL import ImageTk, Image 

root = Tk()
root.title('HNHScouting')
root.iconbitmap("ImagesOfUI/KnightsLogoMinimalClear.png")
root.iconphoto(FALSE, PhotoImage(file = 'ImagesOfUI/KnightsIcon.png'))
root.configure(bg='#F1DDDF')

ButtonImg1 = ImageTk.PhotoImage(Image.open("ImagesOfUI/ExportButtonSA.png"))
ButtonImg2 = ImageTk.PhotoImage(Image.open("ImagesOfUI/DownloadButtonSA.png"))

def findAndDownload():
    print("StartDownload")
    learnFiles["state"] = DISABLED

def exportToExcel():
    print("startExport")
    Export["state"] = DISABLED



learnFiles = Button(root, text="Download From Tablet", command=findAndDownload)
learnFiles.config(image=ButtonImg1)
learnFiles.pack()

Export = Button(root, text="Export Current To Excel", command=exportToExcel)
Export.config(image=ButtonImg2)
Export.pack()


root.mainloop()