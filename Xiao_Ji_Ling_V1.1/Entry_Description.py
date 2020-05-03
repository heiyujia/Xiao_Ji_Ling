import tkinter
import os

class Entry_description(object):
    def __init__(self, path):
        self.tk = tkinter.Tk()
        self.tk.geometry('200x200')
        self.label = tkinter.Label(master=self.tk, text = 'Please entry the description of the project', width = 5)
        self.entry_content = tkinter.Entry(master=self.tk, bd = 2)
        self.Save_button = tkinter.Button(master=self.tk, text = 'Save', command = self.quit)
        self.label.pack()
        self.entry_content.pack()
        self.Save_button.pack()

        self.path = path + '/description.txt'
        self.file = open(self.path, 'w')
        self.file.close()
        
        self.tk.mainloop()

    def quit(self):
        self.text = self.entry_content.get()
        self.file = open(self.path,'w')
        self.file.write(self.text)
        self.file.close()
        self.tk.destroy()