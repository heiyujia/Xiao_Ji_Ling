#GUI V1.1 all selection are only on one page
#location: desktop/Xiao_Ji_Ling_V1.1

import tkinter
import tkinter.ttk
import tkinter.font
from room import room
import os

class GUI_XiaoJiLing (object):

    def __init__(self):
        self.rooms_number = 0
        self.rooms_list = []
        self.root = tkinter.Tk()
        self.sysfont = tkinter.font.Font(self.root, size = 30)
        self.root.title('Xiao Ji Ling V1.1 by Linjie')
        self.root.geometry('1200x600')

        # split the window into differernt part
        self.main_Frm_top = tkinter.Frame(self.root, height = 360, width = 1200)
        self.main_Frm_top.pack(side = 'top')
        self.main_Frm_middle = tkinter.Frame(self.root, height = 60, width = 1200)
        self.main_Frm_middle.pack(side = 'top')
        self.main_Frm_botten = tkinter.Frame(self.root, height = 180, width = 1200)
        self.main_Frm_botten.pack(side = 'top')

        self.sub_frm_top_l = tkinter.Frame(self.main_Frm_top, height = 360, width = 400, highlightbackground="black", highlightthickness = 1)
        self.sub_frm_top_m = tkinter.Frame(self.main_Frm_top, height = 360, width = 400)
        self.sub_frm_top_r = tkinter.Frame(self.main_Frm_top, height = 360, width = 400)
        self.sub_frm_top_l.pack_propagate(False)
        self.sub_frm_top_m.pack_propagate(False)
        self.sub_frm_top_r.pack_propagate(False)
        self.sub_frm_top_l.pack(side = 'left')
        self.sub_frm_top_m.pack(side = 'left')
        self.sub_frm_top_r.pack(side = 'left')

        self.sub_frm_botten_1 = tkinter.Frame(self.main_Frm_botten, height = 180, width = 300)
        self.sub_frm_botten_2 = tkinter.Frame(self.main_Frm_botten, height = 180, width = 300)
        self.sub_frm_botten_3 = tkinter.Frame(self.main_Frm_botten, height = 180, width = 300)
        self.sub_frm_botten_4 = tkinter.Frame(self.main_Frm_botten, height = 180, width = 300, bg = 'red')
        self.sub_frm_botten_1.pack_propagate(False)
        self.sub_frm_botten_2.pack_propagate(False)
        self.sub_frm_botten_3.pack_propagate(False)
        self.sub_frm_botten_4.pack_propagate(False)
        self.sub_frm_botten_1.pack(side = 'left')
        self.sub_frm_botten_2.pack(side = 'left')
        self.sub_frm_botten_3.pack(side = 'left')
        self.sub_frm_botten_4.pack(side = 'left')
        
        # finisched the split 
        self.Big_Label = tkinter.Label(self.sub_frm_top_l, text = 'For Rooms', bg = 'light blue')
        self.Big_Label.pack(fill = tkinter.X)

        self.Label_Length = tkinter.Label(master = self.sub_frm_top_l, text = 'Length', width = 5)
        self.Label_Length.place (x = 22, y = 30)
        self.entry_length = tkinter.Entry(self.sub_frm_top_l, bd = 5, width = 4)
        self.entry_length.place (x = 20, y = 55)

        self.Label_width = tkinter.Label(master = self.sub_frm_top_l, text = 'Width', width = 5)
        self.Label_width.place (x = 172, y = 30)
        self.entry_width = tkinter.Entry(self.sub_frm_top_l, bd = 5, width = 4)
        self.entry_width.place (x = 170, y = 55)
        
        self.Label_Height = tkinter.Label(master = self.sub_frm_top_l, text = 'Height', width = 5)
        self.Label_Height.place (x = 322, y = 30)
        self.entry_height = tkinter.Entry(self.sub_frm_top_l, bd = 5, width = 4)
        self.entry_height.place (x = 320, y = 55)

        self.Label_sort = tkinter.Label(master = self.sub_frm_top_l, text = 'Sort', width = 5)
        self.Label_sort.place (x = 50, y = 100)
        self.Label_Level = tkinter.Label(master = self.sub_frm_top_l, text = 'Level', width = 5)
        self.Label_Level.place (x = 170, y = 100)
        
        self.Combobox_sort = tkinter.ttk.Combobox(master = self.sub_frm_top_l, values = ['Living Room', 
        'Sleeping Room', 'Kitchen', 'Dinning Room', 'Bathroom', 'Storeroom', 'Basement', 'Technik Room'], width = 12 )
        self.Combobox_sort.place (x = 20, y = 125)
        self.Combobox_Level = tkinter.ttk.Combobox(master = self.sub_frm_top_l, values = ['Level 1', 'Level 2', 'Level 3'], width = 6)
        self.Combobox_Level.place (x = 165, y = 125)

        self.Button_Creat_a_room = tkinter.Button(master = self.sub_frm_top_l, text = 'Creat a room', command = self.creat_a_room)
        self.Button_Creat_a_room.place (x = 280, y = 125)

        self.Listbox_rooms = tkinter.Listbox(master = self.sub_frm_top_l, width = 8, selectbackground = 'light gray', selectmode='browse')
        self.Listbox_rooms.bind('<<ListboxSelect>>', self.Show_Infos)
        self.Listbox_rooms.place (x = 20, y = 170)

        self.Listbox_Info = tkinter.Listbox(master = self.sub_frm_top_l, width = 25)
        self.Listbox_Info.place (x = 150, y = 170)

        self.root.mainloop()

    def creat_a_room(self):
        Length = float(self.entry_length.get())
        Width = float(self.entry_width.get())
        Height = float(self.entry_height.get())
        Sort = self.Combobox_sort.get()
        Level = self.Combobox_Level.get()
        self.rooms_number = self.rooms_number + 1

        A_room = room (name = 'Room_%s'%(self.rooms_number), length = Length, width = Width, hight = Height, level = Level, sort = Sort)

        self.rooms_list.append(A_room)
        self.Listbox_rooms.insert (tkinter.END, A_room.name)

        self.entry_length.delete(0, tkinter.END)
        self.entry_width.delete(0, tkinter.END)
        self.entry_height.delete(0, tkinter.END)
        self.Combobox_sort.delete(0,tkinter.END)
        self.Combobox_Level.delete(0,tkinter.END)

    def Show_Infos(self, event):
        self.Listbox_Info.delete(0,tkinter.END)
        position = self.Listbox_rooms.curselection()[0]
        print (position)
        self.rooms_list[position].calculate_the_room()
        Infos = ["Room's Name: %s"%(self.rooms_list[position].name), "Room's Length: %s"%(self.rooms_list[position].length), "Room's Width: %s"%(self.rooms_list[position].width), 
        "Room's Height: %s"%(self.rooms_list[position].hight), "Room's Level: %s"%(self.rooms_list[position].level), "Room's Sort: %s"%(self.rooms_list[position].sort), 
        "Room's Area: %s"%(self.rooms_list[position].s), "The Cable you need: %s"%(self.rooms_list[position].cable_length)]
        for item in Infos:
            self.Listbox_Info.insert(tkinter.END, item)


            


win = GUI_XiaoJiLing()