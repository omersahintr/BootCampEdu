#@Web Site Headings, Link Hrefs and Images Analysing@ #
import random
from sys import exception

from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import scrolledtext
from tkinter import messagebox
import requests as req

## Create a Window with Tkinter Library ##
window = tk.Tk()
window.title("Web Site Headings Counter & Analyzer")
window.minsize(width=900, height=1000)
###########################################

# Labels creating:
labelAddress = tk.Label(text="Site Address:", fg="black", font=("Verdana",12,"bold"))
labelStatus = tk.Label(text="Status: Ready", bg="#545a5e", font=("Verdana",18,"italic"), fg="white")
labelSourceCode = tk.Label(text="Source Code:", font=("Verdana",14,"bold"))

labelH1Count = tk.Label(text="H1", fg="black", bg="#02df5d", font=("Verdana",14,"underline"))
labelH1 = tk.Label(text="-", fg="black", font=("Verdana",16,"bold"))
labelH2Count = tk.Label(text="H2", fg="black", bg="#95df02", font=("Verdana",14,"underline"))
labelH2 = tk.Label(text="-", fg="black", font=("Verdana",16,"bold"))
labelH3Count = tk.Label(text="H3", fg="black", bg="#daf205", font=("Verdana",14,"underline"))
labelH3 = tk.Label(text="-", fg="black", font=("Verdana",16,"bold"))
labelH4Count = tk.Label(text="H4", fg="black", bg="#f2d405", font=("Verdana",14,"underline"))
labelH4 = tk.Label(text="-", fg="black", font=("Verdana",16,"bold"))

labelImageCount = tk.Label(text="Images", bg="#05f2d4", fg="black", font=("Verdana",14,"underline"))
labelImage = tk.Label(text="-", fg="black", font=("Verdana",16,"bold"))

labelLinkCount = tk.Label(text="Links", bg="#0591f2", fg="black", font=("Verdana",14,"underline"))
labelLink = tk.Label(text="-", fg="black", font=("Verdana",16,"bold"))

labelResults = tk.Label(text="RESULTS:", fg="black", font=("Verdana",16,"bold"))

# Entry Objects Creating for Window:
entryAddress = tk.Entry(font=("Verdana",12,"normal"), width=40)

# Scrolled Text Objects Creating for Windows
textResult = scrolledtext.ScrolledText(font=("courier",14),width=100, height=40)

# Button Objects Creating for Window:
sendButton = tk.Button(text="Start Scan", font=("Arial",14,"bold"), command=lambda:main_counter(entryAddress.get()))
saveFileButton = tk.Button(text="Save File", font=("Arial",14,"bold"), command=lambda:saveFileAs())

# Check Button Objects for Window:
chc_val = tk.BooleanVar(); link_val = tk.BooleanVar(); image_val = tk.BooleanVar()
checkHead = tk.Checkbutton(text="Headings", variable=chc_val)
checkLink = tk.Checkbutton(text="Linkhref", variable=link_val)
checkImage = tk.Checkbutton(text="Image", variable=image_val)


### PLACE LOCALISER ###
labelStatus.place(x=200, y=10)
labelAddress.place(x=10, y=40)
entryAddress.place(x=110, y=40); entryAddress.focus()
sendButton.place(x=450, y=36)

checkHead.place(x=10, y=75)
checkLink.place(x=100, y=75)
checkImage.place(x=180, y=75)

y1=180; y2=210; x1=10; x2=15 # static axis values
labelResults.place(x=x1,y=150)
labelH1Count.place(x=x1,y=y1)
labelH1.place(x=x2,y=y2)
labelH2Count.place(x=x1+100,y=y1)
labelH2.place(x=x2+100,y=y2)
labelH3Count.place(x=x1+200,y=y1)
labelH3.place(x=x2+200,y=y2)
labelH4Count.place(x=x1+300,y=y1)
labelH4.place(x=x2+300,y=y2)
labelImageCount.place(x=x1+400,y=y1)
labelImage.place(x=x2+400,y=y2)
labelLinkCount.place(x=x1+500,y=y1)
labelLink.place(x=x2+500,y=y2)

labelSourceCode.place(x=x1,y=y1+70)
textResult.place(x=x1, y=y1+100)
saveFileButton.place(x=x1,y=y1+700)

## SAVE DATA TO TEXT FILE FUNCTION ##
def saveFileAs():
    try:
        fileName = "request"+str(random.randint(1,3000))+".txt"
        file = open(fileName,"x")
        file.write(textResult.get("1.0","end"))
        file.close()
        messagebox.showinfo(title="File Saved", message="Data was saved to ./"+fileName)
    except Exception as e:
        messagebox.showerror(title="File Saved", message=str(e))

## MAIN COUNTER AND ANALYZER FUNCTION ##
def main_counter(url):
    try:
        textResult.delete("1.0", "end")
        if url and (chc_val or link_val or image_val):
            connectUrl = req.get(url)
            soupWebText = BeautifulSoup(connectUrl.text, "html.parser")

            if chc_val.get() == 1:
                textResult.insert(tk.INSERT, chars=(f"----------- HEADINGS: -----------\n"))
                h1_1 = 0
                for h1s in soupWebText.find_all("h1"):
                    if h1s.text != None:
                        h1_1+= 1
                        textResult.insert(tk.INSERT, chars=(f"{h1_1} - H1 - {h1s.text}\n"))
                labelH1.config(text=h1_1)
                h2_1 = 0
                for h2s in soupWebText.find_all("h2"):
                    if h2s.text != None:
                        h2_1 += 1
                        textResult.insert(tk.INSERT, chars=(f"  {h2_1} - H2 - {h2s.text}\n"))
                labelH2.config(text=h2_1)
                h3_1 = 0
                for h3s in soupWebText.find_all("h3"):
                    if h3s.text != None:
                        h3_1 += 1
                        textResult.insert(tk.INSERT, chars=(f"    {h3_1} - H3 - {h3s.text}\n"))
                labelH3.config(text=h3_1)
                h4_1 = 0
                for h4s in soupWebText.find_all("h4"):
                    if h4s.text != None:
                        h4_1 += 1
                        textResult.insert(tk.INSERT, chars=(f"      {h4_1} - H4 - {h4s.text}\n"))
                labelH4.config(text=h4_1)
            else:
                labelH1.config(text="-"); labelH2.config(text="-")
                labelH3.config(text="-"); labelH4.config(text="-")

            if link_val.get() == 1:
                textResult.insert(tk.INSERT, chars=(f"\n\n\n\n----------- URL LINKS: -----------\n"))
                lnk_1 = 0
                for links in soupWebText.find_all("a"):
                    foundLinks = links.get("href")
                    if links.text != None:
                        lnk_1 += 1
                        textResult.insert(tk.INSERT, chars=(f"{lnk_1}- {links.text}:\n {foundLinks}\n"))
                labelLink.config(text=lnk_1)
            else:
                labelLink.config(text="-")

            if image_val.get():
                textResult.insert(tk.INSERT, chars=(f"\n\n\n\n----------- IMAGES: -----------\n"))
                img_1 = 0
                for imgs in soupWebText.find_all("img"):
                    foundImages = imgs.get("src")
                    if imgs.text != None:
                        img_1 += 1
                        textResult.insert(tk.INSERT, chars=(f"{img_1}- {foundImages}\n"))
                labelImage.config(text=img_1)
            else:
                labelImage.config(text="-")
            labelStatus.config(text="Status: Finish Scan", fg="#02df5d")
        else:
            labelStatus.config(text="Status: Please enter an address or select", fg="red")
    except Exception as e:
        messagebox.showerror("Connecting Error","Error code: " + str(e))

window.mainloop()