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

labelH1Count = tk.Label(text="H1 Count:", fg="black", font=("Verdana",14,"underline"))

labelH1 = tk.Label(text="-", fg="black", font=("Verdana",16,"bold"))

labelH2Count = tk.Label(text="H2 Count:", fg="black", font=("Verdana",14,"underline"))

labelH2 = tk.Label(text="-", fg="black", font=("Verdana",16,"bold"))

labelH3Count = tk.Label(text="H3 Count:", fg="black", font=("Verdana",14,"underline"))

labelH3 = tk.Label(text="-", fg="black", font=("Verdana",16,"bold"))

labelH4Count = tk.Label(text="H4 Count:", fg="black", font=("Verdana",14,"underline"))

labelH4 = tk.Label(text="-", fg="black", font=("Verdana",16,"bold"))

labelImageCount = tk.Label(text="Images:", fg="black", font=("Verdana",14,"underline"))

labelImage = tk.Label(text="-", fg="black", font=("Verdana",16,"bold"))

labelLinkCount = tk.Label(text="Links:", fg="black", font=("Verdana",14,"underline"))

labelLink = tk.Label(text="-", fg="black", font=("Verdana",16,"bold"))


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

labelH1Count.place(x=10,y=100)
labelH1.place(x=10,y=120)
labelH2Count.place(x=100,y=100)
labelH2.place(x=100,y=120)
labelH3Count.place(x=200,y=100)
labelH3.place(x=200,y=120)
labelH4Count.place(x=300,y=100)
labelH4.place(x=300,y=120)




def heading_counter(url):
    if url:
        labelStatus.config(text=f"Scanning to: {entryAddress.get()}", fg="green")
    else:
        labelStatus.config(text="Status: Please enter an address", fg="red")








window.mainloop()