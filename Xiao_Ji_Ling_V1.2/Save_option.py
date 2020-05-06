import tkinter
import os

class Save_option(object):
    def __init__(self, info):
        self.sv = tkinter.Toplevel()
        self.sv.geometry('400x200')
        self.sv_label = tkinter.Label(self.sv, text = "Do you want to save your planning?", width = 30)
        #self.sv_label.pack()
        self.sv_label.place(relx = 0.5, rely = 0.1, anchor = tkinter.CENTER)
        x = lambda a: a
        self.sv_save_button = tkinter.Button(self.sv, text = 'Save', command = x(1))
        self.sv_cancel_button = tkinter.Button(self.sv, text = 'Quit', command = x(0))
        self.sv_save_button.place(relx = 0.3, rely = 0.6, anchor = tkinter.CENTER)
        self.sv_cancel_button.place(relx = 0.7, rely = 0.6, anchor = tkinter.CENTER)
        if x == 1:
            f = open(info.store_path, 'w')
            f.write("Buliding Name: %s \nRooms Number: %s    Flats Number: %s   Floor Number: %s \nTotal Cable: %s      Total Area: %s"
            %(info.building_name, info.rooms_number, info.flats_number, info.floors_number, info.building_cable_length, info.building_area))
            f.close()
            tkinter.messagebox.showinfo('Info', 'The file has been saved in ' + info.store_path)
            self.sv.destroy()
        elif x == 0:
            tkinter.messagebox.showinfo('Info', 'The file has not been saved')
            self.sv.destroy()
