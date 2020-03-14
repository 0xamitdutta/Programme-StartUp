import os
import tkinter as tk
from tkinter import filedialog, Text

apps = []

if os.path.isfile("save.txt"):
    with open("save.txt", "r") as f:
        tempapps = f.read().split(',')
        apps = [x for x in tempapps if x.strip()]

def addApp():
    filename = filedialog.askopenfilename(initialdir="/", title="Select File", filetypes=(("executables", "*.exe"), ("all files", "*.*")))
    apps.append(filename)
    label = tk.Label(frame, text=filename, bg="gray")
    label.pack()

def runApp():
    for app in apps:
        os.startfile(app)

root = tk.Tk()
root.title("STARTUP APPS")

canvas = tk.Canvas(root, width=700, height=700, bg="#263D42")
canvas.pack()

frame = tk.Frame(root)
frame.place(relwidth=0.8, relheight=0.8, relx = 0.1, rely = 0.1)

openfile = tk.Button(root, text="Open File", bg="gray", command=addApp)
openfile.pack()

runapps = tk.Button(root, text="Run Apps", bg="gray", command=runApp)
runapps.pack()

for app in apps:
    label = tk.Label(frame, text=app)
    label.pack()

root.mainloop()

with open("save.txt", "w") as f:
    for app in apps:
        f.write(app + ',')

