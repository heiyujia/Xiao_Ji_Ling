import tkinter
import tkinter.ttk
import tkinter.font
import tkinter.messagebox
from room import room
from floor import *
import os
from flat import *
from Building import *
#from Save_option import *


class GUI_XiaoJiLing (object):

    def __init__(self, building):
        self.building = building
        self.rooms_number = 0
        self.rooms_list = []
        self.root = tkinter.Toplevel()
        self.sysfont = tkinter.font.Font(self.root, size = 30)
        self.root.title('Xiao Ji Ling V1.3 by Linjie')
        self.root.geometry('1200x600')
        self.root.bind('<Button-1>', self.update_the_Building_Info)

        # split the window into differernt part
        self.main_Frm_top = tkinter.Frame(self.root, height = 360, width = 1200)
        self.main_Frm_top.pack(side = 'top')
        self.main_Frm_middle = tkinter.Frame(self.root, height = 60, width = 1200,highlightbackground="black", highlightthickness = 1)
        self.main_Frm_middle.pack(side = 'top')
        self.main_Frm_botten = tkinter.Frame(self.root, height = 180, width = 1200,highlightbackground="black", highlightthickness = 1)
        self.main_Frm_botten.pack(side = 'top')

        self.sub_frm_top_l = tkinter.Frame(self.main_Frm_top, height = 360, width = 400, highlightbackground="black", highlightthickness = 1)
        self.sub_frm_top_m = tkinter.Frame(self.main_Frm_top, height = 360, width = 400, highlightbackground="black", highlightthickness = 1)
        self.sub_frm_top_r = tkinter.Frame(self.main_Frm_top, height = 360, width = 400, highlightbackground="black", highlightthickness = 1)
        self.sub_frm_top_l.pack_propagate(False)
        self.sub_frm_top_m.pack_propagate(False)
        self.sub_frm_top_r.pack_propagate(False)
        self.sub_frm_top_l.pack(side = 'left')
        self.sub_frm_top_m.pack(side = 'left')
        self.sub_frm_top_r.pack(side = 'left')

        self.sub_frm_botten_1 = tkinter.Frame(self.main_Frm_botten, height = 180, width = 300)
        self.sub_frm_botten_2 = tkinter.Frame(self.main_Frm_botten, height = 180, width = 300)
        self.sub_frm_botten_3 = tkinter.Frame(self.main_Frm_botten, height = 180, width = 300)
        self.sub_frm_botten_4 = tkinter.Frame(self.main_Frm_botten, height = 180, width = 300)
        self.sub_frm_botten_1.pack_propagate(False)
        self.sub_frm_botten_2.pack_propagate(False)
        self.sub_frm_botten_3.pack_propagate(False)
        self.sub_frm_botten_4.pack_propagate(False)
        self.sub_frm_botten_1.pack(side = 'left')
        self.sub_frm_botten_2.pack(side = 'left')
        self.sub_frm_botten_3.pack(side = 'left')
        self.sub_frm_botten_4.pack(side = 'left')
        
        # finisched the split 

        # Part1: left top for Room--------------------------------------------------------------------------
        self.Big_Label_rooms = tkinter.Label(self.sub_frm_top_l, text = 'For Rooms', bg = 'light blue')
        self.Big_Label_rooms.pack(fill = tkinter.X)

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
        'Sleeping Room', 'Children Rooms','Kitchen', 'Dinning Room', 'Bathroom', 'Storeroom', 'Flur', 'Basement', 'Technik Room'], width = 12 )
        self.Combobox_sort.place (x = 20, y = 125)
        self.Combobox_sort.current(0)
        self.Combobox_Level = tkinter.ttk.Combobox(master = self.sub_frm_top_l, values = ['Level 1', 'Level 2', 'Level 3'], width = 6)
        self.Combobox_Level.place (x = 165, y = 125)
        self.Combobox_Level.current(0)

        self.Button_Creat_a_room = tkinter.Button(master = self.sub_frm_top_l, text = 'Creat a room', command = self.creat_a_room)
        self.Button_Creat_a_room.place (x = 280, y = 125)

        self.Listbox_rooms = tkinter.Listbox(master = self.sub_frm_top_l, width = 8, selectbackground = 'light gray', selectmode='SINGLE')
        self.Listbox_rooms.bind('<<ListboxSelect>>', self.Show_Infos)
        self.Listbox_rooms.place (x = 20, y = 170)

        self.Menu_rooms = tkinter.Menu(master=self.Listbox_rooms, tearoff = 0)
        self.Menu_rooms.add_command (label = 'Copy the room', command = self.copy_room)
        self.Menu_rooms.add_command (label = 'Delete the room', command = self.delete_room)

        self.Listbox_rooms.bind("<Button-2>", self.popup)

        self.Listbox_Info = tkinter.Listbox(master = self.sub_frm_top_l, width = 25)
        self.Listbox_Info.place (x = 150, y = 170)

        # Part2: Top middle for flat ----------------------------------------------------------------
        self.rooms_list_for_flat = []
        self.flats_list = []
        self.flats_number = 0

        self.Big_Label_flats = tkinter.Label(master = self.sub_frm_top_m, text = 'For Flats', bg = 'light green')
        self.Big_Label_flats.pack(fill = tkinter.X)

        self.Listbox_rooms_for_flat = tkinter.Listbox(master = self.sub_frm_top_m, width = 8, selectmode = tkinter.MULTIPLE, selectbackground = 'light gray', exportselection = 0)
        self.Listbox_rooms_for_flat.place (x = 20, y = 30)

        self.Listbox_flats = tkinter.Listbox(master = self.sub_frm_top_m, width = 8, selectbackground = 'light gray', exportselection = 0)
        self.Listbox_flats.bind('<<ListboxSelect>>', self.Show_flat_Infos)
        self.Listbox_flats.place (x = 200, y = 30)

        self.Button_Creat_a_flat = tkinter.Button(master = self.sub_frm_top_m, text = 'Creat a flat', command = self.creat_a_flat)
        self.Button_Creat_a_flat.place (x = 300, y = 100)

        self.Button_add_rooms_to_flat = tkinter.Button(master = self.sub_frm_top_m, text = 'added to', command = self.add_rooms_to_flat)
        self.Button_add_rooms_to_flat.place (x = 110, y = 100)

        self.Listbox_flats_Info1 = tkinter.Listbox(master = self.sub_frm_top_m)
        self.Listbox_flats_Info1.place (x = 20, y = 223, relwidth = 0.4 ,relheight=0.35)
        self.Listbox_flats_Info2 = tkinter.Listbox(master = self.sub_frm_top_m)
        self.Listbox_flats_Info2.place (x = 178, y = 223, relwidth = 0.5 ,relheight=0.35)
        self.Scrollbar_Listbox_flats_Info2 = tkinter.Scrollbar(master = self.Listbox_flats_Info2, command = self.Listbox_flats_Info2.yview, orient = 'vertical')
        self.Scrollbar_Listbox_flats_Info2.pack( side = 'right', fill = tkinter.Y)
        #self.Scrollbar_Listbox_flats_Info2.place(x = 165, y = 0)
        self.Listbox_flats_Info2.config(yscrollcommand = self.Scrollbar_Listbox_flats_Info2.set)

        # Part3: Top right for 
        self.flats_list_for_floor = []
        self.floors_list = []
        self.floors_number = 0

        self.Big_Label_floor = tkinter.Label(master = self.sub_frm_top_r, text = 'For Floor', bg = 'pink')
        self.Big_Label_floor.pack(fill = tkinter.X)

        self.Listbox_flats_for_floor = tkinter.Listbox(master = self.sub_frm_top_r, width = 8, selectmode = tkinter.MULTIPLE, selectbackground = 'light gray', exportselection = 0)
        self.Listbox_flats_for_floor.place (x = 20, y = 30)

        self.Listbox_floors = tkinter.Listbox(master = self.sub_frm_top_r, width = 8, selectbackground = 'light gray', exportselection = 0)
        self.Listbox_floors.bind('<<ListboxSelect>>', self.Show_floor_Infos)
        self.Listbox_floors.place (x = 200, y = 30)

        self.Button_Creat_a_floor = tkinter.Button(master = self.sub_frm_top_r, text = 'Creat a floor', command = self.creat_a_floor)
        self.Button_Creat_a_floor.place (x = 300, y = 100)

        self.Button_add_flats_to_floor = tkinter.Button(master = self.sub_frm_top_r, text = 'added to', command = self.add_flats_to_floor)
        self.Button_add_flats_to_floor.place (x = 110, y = 100)

        self.Listbox_floors_Info1 = tkinter.Listbox(master = self.sub_frm_top_r)
        self.Listbox_floors_Info1.place (x = 20, y = 223, relwidth = 0.4 ,relheight=0.35)
        self.Listbox_floors_Info2 = tkinter.Listbox(master = self.sub_frm_top_r)
        self.Listbox_floors_Info2.place (x = 178, y = 223, relwidth = 0.5 ,relheight=0.35)
        self.Scrollbar_Listbox_floors_Info2 = tkinter.Scrollbar(master = self.Listbox_floors_Info2, command = self.Listbox_floors_Info2.yview, orient = 'vertical')
        self.Scrollbar_Listbox_floors_Info2.pack( side = 'right', fill = tkinter.Y)
        
        self.Listbox_floors_Info2.config(yscrollcommand = self.Scrollbar_Listbox_floors_Info2.set)

        #part4 : middle for Building and Building description
        self.building_lable = tkinter.Label(master=self.main_Frm_middle, text = self.building.building_name)
        self.building_lable.pack(side = 'left')
        #self.building_lable2 = tkinter.Label(master=self.main_Frm_middle, text = self.building.building_description)
        #self.building_lable2.pack(side = 'left')
        
        #part5: Botten for Building info
        self.Infobox = tkinter.Listbox(master = self.sub_frm_botten_1)
        self.Infobox.place(relwidth = 0.9, relheight = 1)
        self.Infobox_scrollbar = tkinter.Scrollbar(master = self.Infobox, command = self.Infobox.yview, orient = 'vertical')
        self.Infobox_scrollbar.pack( side = 'right', fill = tkinter.Y)
        #self.Scrollbar_Listbox_flats_Info2.place(x = 165, y = 0)
        self.Infobox.config(yscrollcommand = self.Infobox_scrollbar.set)

        self.Infobox.insert(tkinter.END, self.building.creat_str)

        self.Info1 = tkinter.StringVar()
        self.Info2 = tkinter.StringVar()
        self.Info3 = tkinter.StringVar()
        self.Info4 = tkinter.StringVar()
        self.Info5 = tkinter.StringVar()
        self.Info6 = tkinter.StringVar()

        self.Info1.set('Rooms number: 0')
        self.Info2.set('Flats number: 0')
        self.Info3.set('Floors number: 0')
        self.Info4.set('Total Cable: 0')
        self.Info5.set('Total area: 0')
        self.Info6.set("Description:\n%s"%(self.building.building_description))

        self.building_info_label1 = tkinter.Label(master=self.sub_frm_botten_2, textvariable = self.Info1)
        self.building_info_label1.pack()
        self.building_info_label2 = tkinter.Label(master=self.sub_frm_botten_2, textvariable = self.Info2)
        self.building_info_label2.pack()
        self.building_info_label3 = tkinter.Label(master=self.sub_frm_botten_2, textvariable = self.Info3)
        self.building_info_label3.pack()
        self.building_info_label4 = tkinter.Label(master=self.sub_frm_botten_2, textvariable = self.Info4)
        self.building_info_label4.pack()
        self.building_info_label5 = tkinter.Label(master=self.sub_frm_botten_2, textvariable = self.Info5)
        self.building_info_label5.pack()
        self.building_info_label6 = tkinter.Label(master=self.sub_frm_botten_3, textvariable = self.Info6, width = 10, height = 20)
        self.building_info_label6.pack(side = tkinter.TOP)

        self.finish_Button = tkinter.Button(master=self.sub_frm_botten_4, text = 'End the Planning', command = self.Save_option)
        self.finish_Button.pack()
        
        #self.root.mainloop()

    # function definition
    # Part1: left top for Room--------------------------------------------------------------------------
    def creat_a_room(self):
        try:
            Length = float(self.entry_length.get())
            Width = float(self.entry_width.get()) 
            Height = float(self.entry_height.get())
        except:
            tkinter.messagebox.showinfo('Warning', 'The Entry of Length, Width and Height\n must be Number and can not be Empty')
            self.Infobox.insert(tkinter.END, "Warning: The Entry of Length, Width")
            self.Infobox.insert(tkinter.END, "and Height must be Number and can")
            self.Infobox.insert(tkinter.END, "not be Empty")
            self.entry_length.delete(0, tkinter.END)
            self.entry_width.delete(0, tkinter.END)
            self.entry_height.delete(0, tkinter.END)
            self.Combobox_sort.delete(0,tkinter.END)
            self.Combobox_Level.delete(0,tkinter.END)
            self.Combobox_sort.current(0)
            self.Combobox_Level.current(0)
            return
        
        Sort = self.Combobox_sort.get()
        Level = self.Combobox_Level.get()

        self.rooms_number = self.rooms_number + 1
        A_room = room (name = 'Room_%s'%(self.rooms_number), length = Length, width = Width, hight = Height, level = Level, sort = Sort)
        self.rooms_list.append(A_room)
        self.rooms_list_for_flat.append(A_room)
        self.Listbox_rooms.insert (tkinter.END, A_room.name)
        self.Listbox_rooms_for_flat.insert (tkinter.END, A_room.name)

        self.entry_length.delete(0, tkinter.END)
        self.entry_width.delete(0, tkinter.END)
        self.entry_height.delete(0, tkinter.END)
        self.Combobox_sort.delete(0,tkinter.END)
        self.Combobox_Level.delete(0,tkinter.END)
        self.Combobox_sort.current(0)
        self.Combobox_Level.current(0)

        self.Infobox.insert(tkinter.END, A_room.creat_str)

    def Show_Infos(self, event):
        self.Listbox_Info.delete(0,tkinter.END)
        position = self.Listbox_rooms.curselection()[0]
        self.rooms_list[position].calculate_the_room()
        Infos = ["Room's Name: %s"%(self.rooms_list[position].name), "Room's Length: %s"%(self.rooms_list[position].length), "Room's Width: %s"%(self.rooms_list[position].width), 
        "Room's Height: %s"%(self.rooms_list[position].hight), "Room's Level: %s"%(self.rooms_list[position].level), "Room's Sort: %s"%(self.rooms_list[position].sort), 
        "Room's Area: %s"%(self.rooms_list[position].s), "NYM-J 3x2.5: %s"%(self.rooms_list[position].cable_3x2p5)]
        for item in Infos:
            self.Listbox_Info.insert(tkinter.END, item)

    def popup(self, event):
        self.Menu_rooms.post(event.x_root, event.y_root)

    def copy_room(self):
        self.Infobox.insert(tkinter.END, "The room has been copied")

    def delete_room(self):
        self.Infobox.insert(tkinter.END, "The room has been deleted")

    # Part2: Top middle for Flat--------------------------------------------------------------------------
    def creat_a_flat(self):
        #A_flat = flat()
        self.flats_number = self.flats_number + 1
        A_flat = flat(name = 'Flat_%s'%(self.flats_number))
        #A_flat.name = 'Flat_%s'%(self.flats_number)
        self.flats_list.append(A_flat)
        self.flats_list_for_floor.append(A_flat)
        self.Listbox_flats.insert(tkinter.END, A_flat.name)
        self.Listbox_flats_for_floor.insert (tkinter.END, A_flat.name)

        self.Infobox.insert(tkinter.END, A_flat.creat_str)

    def add_rooms_to_flat(self):
        get_position_rooms = self.Listbox_rooms_for_flat.curselection()
        get_position_flat = self.Listbox_flats.curselection()[0]

        Templist = []

        for i in get_position_rooms:
            Templist.append(self.rooms_list_for_flat[i])

        #delete the selected elements
        a = range(len(self.rooms_list_for_flat))
        index_a = set(a)
        index_b = set(get_position_rooms)
        index_c = index_a - index_b
        self.rooms_list_for_flat = [self.rooms_list_for_flat[i] for i in index_c]


        self.Listbox_rooms_for_flat.delete(0,tkinter.END)

        for item in self.rooms_list_for_flat:
            self.Listbox_rooms_for_flat.insert (tkinter.END, item.name)

        for item in Templist:
            item.calculate_the_room()
            self.flats_list[get_position_flat].add_rooms (Info = item)

        #self.flats_list[get_position_flat].calculate_the_flat()
    
    
    def Show_flat_Infos(self, event):
        
        self.Listbox_flats_Info1.delete(0, tkinter.END)
        self.Listbox_flats_Info2.delete(0,tkinter.END)
        get_position_flat = self.Listbox_flats.curselection()[0]
        self.flats_list[get_position_flat].calculate_the_flat()
        
        Infos_flat1 = ['Rooms Number: %s'%(self.flats_list[get_position_flat].rooms_number), 'Flat area: %s'%(self.flats_list[get_position_flat].flat_area), 'NYM-J 3x2.5: %s'%(self.flats_list[get_position_flat].flat_cable_3x2p5)]
        for Item in Infos_flat1:
            self.Listbox_flats_Info1.insert(tkinter.END, Item)

        Actuell_rooms = [item for item in self.flats_list[get_position_flat].including_rooms_Infos]
        Infos_flat2 = ['Including Rooms:']
        for item in Actuell_rooms:
            Infos_flat2.append('Name: %s'%(item.name))
            Infos_flat2.append('Sort: %s'%(item.sort))
            Infos_flat2.append('Area: %s'%(item.s))
            Infos_flat2.append('Cable: %s'%(item.cable_3x2p5))

        for item in Infos_flat2:
            self.Listbox_flats_Info2.insert(tkinter.END, item)

    # Part3: Top right for floor
    def creat_a_floor(self):
        #A_floor = floor()
        self.floors_number = self.floors_number + 1
        A_floor = floor(name = 'Floor_%s'%(self.floors_number))
        #A_floor.name = 'Floor_%s'%(self.floors_number)
        self.floors_list.append(A_floor)
        self.Listbox_floors.insert(tkinter.END, A_floor.name)

        self.Infobox.insert(tkinter.END, A_floor.creat_str)

    def add_flats_to_floor(self):
        get_position_flats = self.Listbox_flats_for_floor.curselection()
        get_position_floor = self.Listbox_floors.curselection()[0]

        Templist = []

        for i in get_position_flats:
            Templist.append(self.flats_list_for_floor[i])

        #delete the selected elements
        a = range(len(self.flats_list_for_floor))
        index_a = set(a)
        index_b = set(get_position_flats)
        index_c = index_a - index_b
        self.flats_list_for_floor = [self.flats_list_for_floor[i] for i in index_c]


        self.Listbox_flats_for_floor.delete(0,tkinter.END)

        for item in self.flats_list_for_floor:
            self.Listbox_flats_for_floor.insert (tkinter.END, item.name)

        for item in Templist:
            #item.calculate_the_flat()
            self.floors_list[get_position_floor].add_flats (Info = item)

        #self.floors_list[get_position_floor].calculate_the_floor()


    def Show_floor_Infos(self, event):
        
        self.Listbox_floors_Info1.delete(0, tkinter.END)
        self.Listbox_floors_Info2.delete(0,tkinter.END)
        get_position_floor = self.Listbox_floors.curselection()[0]
        self.floors_list[get_position_floor].calculate_the_floor()
        
        Infos_floor1 = ['Flats Number: %s'%(self.floors_list[get_position_floor].flats_number), 'Floor Area: %s'%(self.floors_list[get_position_floor].floor_area), 'NYM-J 3x2.5: %s'%(self.floors_list[get_position_floor].floor_cable_3x2p5)]
        for Item in Infos_floor1:
            self.Listbox_floors_Info1.insert(tkinter.END, Item)

        Actuell_floors = [item for item in self.floors_list[get_position_floor].including_flats_Infos]
        Infos_floor2 = ['Including flats:']
        for item in Actuell_floors:
            Infos_floor2.append('Name: %s'%(item.name))
            Infos_floor2.append('Rooms Number: %s'%(item.rooms_number))
            Infos_floor2.append('Flat area: %s'%(item.flat_area))
            Infos_floor2.append('Flat cable: %s'%(item.flat_cable_3x2p5))

        for item in Infos_floor2:
            self.Listbox_floors_Info2.insert(tkinter.END, item)

    def update_the_Building_Info(self,event):
        self.building.rooms_number = self.rooms_number
        self.building.flats_number = self.flats_number
        self.building.floors_number = self.floors_number
        self.building.building_cable_3x2p5  = 0
        self.building.building_area = 0
        for item in self.floors_list:
            self.building.building_cable_3x2p5 = self.building.building_cable_3x2p5 + item.floor_cable_3x2p5
            self.building.building_area = self.building.building_area + item.floor_area

        self.Info1.set('Rooms number: '+str(self.building.rooms_number))
        self.Info2.set('Flats number: '+str(self.building.flats_number))
        self.Info3.set('Floors number: '+str(self.building.floors_number))
        self.Info4.set('Total NYM-J 3x2.5: '+str(self.building.building_cable_3x2p5))
        self.Info5.set('Total area: '+str(self.building.building_area))

    def Save_option(self):
        sv = tkinter.messagebox.askquestion(title='Quit the Plannung', message = 'Do you want to save the planning?')
        if sv == 'yes':
            f = open(self.building.store_path, 'w')
            f.write('Description: ' + self.building.building_description + '\n' + "Buliding Name: %s \nRooms Number: %s    Flats Number: %s   Floor Number: %s \nTotal NYM-J 3x2.5: %s      Total Area: %s"
            %(self.building.building_name, self.building.rooms_number, self.building.flats_number, self.building.floors_number, self.building.building_cable_3x2p5, self.building.building_area))
            f.close()
            tkinter.messagebox.showinfo('Info', 'The file has been saved in ' + self.building.store_path)
            self.root.destroy()
        else:
            tkinter.messagebox.showinfo('Info', 'The file has not been saved')
            self.root.destroy()






        

