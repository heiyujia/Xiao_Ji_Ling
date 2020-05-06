import tkinter
from Building import *
from GUI_V1_1 import *
import os
from Entry_Description import *

class Surface (object):
    def __init__(self):
        self.project_number = 0
        self.project_list = []
        self.root = tkinter.Tk()
        self.root.geometry('300x300')
        self.root.title('Xiao Ji Ling V1.1 by Linjie')
        self.Main_Label = tkinter.Label(master = self.root, text = 'Project Name')
        self.Main_Label.pack()
        self.entry_project_name = tkinter.Entry(master=self.root, bd = 2, width = 10)
        self.entry_project_name.pack()
        self.Button1 = tkinter.Button(master=self.root, text = 'Creat a Project', command = self.Start_a_Project)
        self.Button1.pack()
        self.Listbox_project = tkinter.Listbox(master = self.root, width = 10)
        self.Listbox_project.place(relx = 0.1, rely= 0.3, relwidth = 0.8, relheight = 0.5)
        self.Scrollbar1 = tkinter.Scrollbar(master = self.Listbox_project, command = self.Listbox_project.yview, orient = 'vertical')
        self.Scrollbar1.pack(side = 'right', fill = tkinter.Y)
        self.Listbox_project.config(yscrollcommand = self.Scrollbar1.set)
        self.Button2 = tkinter.Button(master = self.root, text = 'Start planning', command = self.start_GUI)
        self.Button2.place(relx = 0.33, rely = 0.85)

        self.root.mainloop()

    def Start_a_Project(self):
        self.project_name = self.entry_project_name.get()
        self.path = os.getcwd() + "/Datebank/%s"%(self.project_name)
        print (self.path)
        if not os.path.exists(self.path):
            os.makedirs(self.path)

        Sub_win = Entry_description(self.path)
        self.root.wait_window(Sub_win.tk)

        #print ('end the wait')


        file = open(self.path + '/description.txt')
        context = file.read()
        file.close()

        

        P = building(name = self.project_name, description = context, path = (self.path + '/description.txt'))
        self.project_list.append(P)
        self.project_number = self.project_number + 1
        self.Listbox_project.insert(tkinter.END, self.project_name)

        self.entry_project_name.delete(0, tkinter.END)

    def start_GUI(self):
        position = self.Listbox_project.curselection()[0]
        main_win = GUI_XiaoJiLing(self.project_list[position])
        self.root.wait_window(main_win.root)



        

win = Surface()


       
