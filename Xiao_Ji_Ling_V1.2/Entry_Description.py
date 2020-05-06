import tkinter
import os

class Entry_description(object):
    def __init__(self, path):
        self.tk = tkinter.Toplevel()
        self.tk.geometry('600x200')
        self.label = tkinter.Label(master=self.tk, text = 'Please entry the description of the project', width = 30)
        self.entry_content = tkinter.Entry(master=self.tk, bd = 2, width = 30)
        self.Save_button = tkinter.Button(master=self.tk, text = 'Save', command = self.quit)
        self.label.pack()
        self.entry_content.pack()
        self.Save_button.pack()

        self.path = path + '/description.txt'
        self.file = open(self.path, 'w')
        self.file.close()
        
        

    def quit(self):
        self.text = self.entry_content.get()
        self.file = open(self.path,'w')
        self.file.write(self.text + '\n')
        self.file.close()
        self.tk.destroy()