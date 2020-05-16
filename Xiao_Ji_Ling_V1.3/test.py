from tkinter import *

root = Tk()

L = Listbox(root)
text = ['1','2','3','4']
for i in text:
    L.insert(END, i)

L.pack()

for item in L:
    print(item)

root.mainloop()