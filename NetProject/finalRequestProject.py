import tkinter as tk
import requests as req

url_static = "https://github.com/omersahintr/BootCampEdu/"

## Create a Window with Tkinter Library ##
window = tk.Tk()
window.title("Web Site Headings Counter & Analyzer")
window.minsize(width=900, height=1000)
###########################################

# Labels creating:
labelAddress = tk.Label(text="Site Address:", fg="black", font=("Verdana",12,"bold"))

labelStatus = tk.Label(text="Status: Ready",  font=("Verdana",18,"bold"), fg="green")

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


# Entry Objects Creating for Window
entryAddress = tk.Entry(font=("Verdana",12,"normal"), width=40)



# Button Objects Creating for Window
sendButton = tk.Button(text="Start Scan", font=("Arial",14,"bold"), command=lambda:heading_counter(entryAddress.get()))


### PLACE LOCALISER ###
#labelStatus.grid(row=1,column=0)
labelStatus.place(x=200, y=10)
labelAddress.place(x=10, y=40)
entryAddress.place(x=110, y=40); entryAddress.focus()
sendButton.place(x=450, y=36)

y1=140; y2=165; x1=10; x2=15
labelResults.place(x=x1,y=100)
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



def heading_counter(url):
    if url:
        labelStatus.config(text=f"Scanning to: {entryAddress.get()}", fg="green")
    else:
        labelStatus.config(text="Status: Please enter an address", fg="red")








window.mainloop()