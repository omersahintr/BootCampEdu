import tkinter as tk
import requests as req

url_static = "https://github.com/omersahintr/BootCampEdu/"

## Create a Window with Tkinter Library ##
window = tk.Tk()
window.title("Web Site Headings Counter & Analyzer")
window.minsize(width=900, height=1000)
###########################################

# Labels creating:
labelAddress = tk.Label(text="Site Address:")
labelAddress.config(fg="black", font=("Verdana",12,"bold"))

labelStatus = tk.Label(text="Status: Ready",  font=("Verdana",18,"bold"))
labelStatus.config(fg="green")




# Entery Objects Creating for Window
enteryAddress = tk.Entry(font=("Verdana",12,"normal"), width=40)



# Button Objects Creating for Window
sendButton = tk.Button(text="Start Scan", font=("Arial",14,"bold"), command=lambda:heading_counter(enteryAddress.get()))


### PLACE LOCALISER ###
#labelStatus.grid(row=1,column=0)
labelStatus.place(x=400, y=10)
labelAddress.place(x=10, y=40)
enteryAddress.place(x=110, y=40); enteryAddress.focus()
sendButton.place(x=450, y=36)




def heading_counter(url):
    labelStatus.config(text=enteryAddress.get())








window.mainloop()