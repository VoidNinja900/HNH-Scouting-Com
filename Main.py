from tkinter import *
from tkinter.ttk import *
from PIL import ImageTk, Image 
import subprocess

root = Tk()
root.title('HNHScouting')
root.iconbitmap("ImagesOfUI/KnightsLogoMinimalClear.png")
root.iconphoto(FALSE, PhotoImage(file = 'ImagesOfUI/KnightsIcon.png'))
root.configure(bg='#F1DDDF')
root.geometry("1020x1000")
root.resizable(False, False)

BGI = PhotoImage(file="ImagesOfUI/BackImageSA.png")
BGIL = Label(root, image=BGI)
BGIL.place(x=0, y=0, relwidth=1, relheight=1)


ButtonImg1 = ImageTk.PhotoImage(Image.open("ImagesOfUI/DownloadButtonSA.png"))
ButtonImg2 = ImageTk.PhotoImage(Image.open("ImagesOfUI/ExportButtonSA.png"))

def findAndDownload():
    print("StartDownload")
    Export["state"] = DISABLED
    learnFiles["state"] = DISABLED
    Process1 = subprocess.Popen(["python", "SeekAndDownloadData.py"])
    Process1.wait()
    ReEnableAll()


def exportToExcel():
    print("startExport")
    learnFiles["state"] = DISABLED
    Export["state"] = DISABLED
    Process2 = subprocess.Popen(["python", "ConvertToExcel.py"])
    Process2.wait()
    ReEnableAll()

   

def ReEnableAll():
    Export["state"] = ACTIVE
    learnFiles["state"] = ACTIVE
   


learnFiles = Button(root, text="Download From Tablet", command=findAndDownload)
learnFiles.config(image=ButtonImg1)
learnFiles.grid(row=4, column=6)

Export = Button(root, text="Export Current To Excel", command=exportToExcel)
Export.config(image=ButtonImg2)
Export.grid(row=4, column=3)

root.mainloop()