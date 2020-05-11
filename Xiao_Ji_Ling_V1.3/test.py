from tkinter import *

root = Tk()

w = Label(root, text="Right-click to display menu", width=40, height=20)
w.pack()

def Next_1():
    print ('you click right')

# create a menu
popup = Menu(root, tearoff=0)
popup.add_command(label="Next", command = Next_1) # , command=next) etc...
popup.add_command(label="Previous")
popup.add_separator()
popup.add_command(label="Home")



def do_popup(event):
    # display the popup menu
    try:
        popup.tk_popup(event.x_root, event.y_root, 0)
    finally:
        # make sure to release the grab (Tk 8.0a1 only)
        popup.grab_release()

w.bind("<Button-2>", do_popup)

b = Button(root, text="Quit", command=root.destroy)
b.pack()

mainloop()