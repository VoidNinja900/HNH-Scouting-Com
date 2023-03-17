from tkinter import *
from tkinter.ttk import *
from PIL import ImageTk, Image 
import subprocess

root = Tk()
root.title('HNHScouting')
root.iconbitmap("ImagesOfUI/KnightsLogoMinimalClear.png")
root.iconphoto(FALSE, PhotoImage(file = 'ImagesOfUI/KnightsIcon.png'))
root.configure(bg='#F1DDDF')

ButtonImg1 = ImageTk.PhotoImage(Image.open("ImagesOfUI/DownloadButtonSA.png"))
ButtonImg2 = ImageTk.PhotoImage(Image.open("ImagesOfUI/ExportButtonSA.png"))

def findAndDownload():
    print("StartDownload")
    Export["state"] = DISABLED
    learnFiles["state"] = DISABLED
    subprocess.run(["python", "SeekAndDownloadData.py"])

def exportToExcel():
    print("startExport")
    learnFiles["state"] = DISABLED
    Export["state"] = DISABLED
    subprocess.run(["python", "ConvertToExcel.py"])


learnFiles = Button(root, text="Download From Tablet", command=findAndDownload)
learnFiles.config(image=ButtonImg1)
learnFiles.pack()

Export = Button(root, text="Export Current To Excel", command=exportToExcel)
Export.config(image=ButtonImg2)
Export.pack()


root.mainloop()