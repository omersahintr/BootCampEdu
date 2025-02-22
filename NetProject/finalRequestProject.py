import tkinter as tk
import requests as req

url = "https://www.ensonhaber.com/son-dakika-haberleri"

window = tk.Tk()
window.title("Live News Top 10")
window.minsize(width=900, height=1200)

labelAddress = tk.Label(text="Ensonhaber")