class room(object):
    def __init__ (self, name, length, width, hight, level, sort):
        self.name = name
        self.length = length
        self.width = width
        self.hight = hight
        self.level = level
        self.sort = sort
        self.cable_3x2p5 = 0
        self.s = 0
        self.rooms_sort_dict = {
            'Living Room': self.Cable_in_Living_Room, 
            'Sleeping Room': self.Cable_in_Sleeping_Room,
            'Children Rooms': self.Cable_in_Children_Room,
            'Kitchen': self.Cable_in_Kitchen,
            'Dinning Room': self.Cable_in_Dinning_Room,
            'Bathroom': self.Cable_in_Bathroom,
            'Storeroom': self.Cable_in_Storeroom,
            'Basement': self.Cable_in_Basement,
            'Technik Room': self.Cable_in_Technik_Room,
            'Flur': self.Cable_in_Flur
        }
        self.rooms_level_dict = {
            'Level 1': [0, 0],
            'Level 2': [1, 0],
            'Level 3': [1, 1]
        }
        self.creat_str = '%s has been created' %(self.name)
        self.delete_str = '%s has been deleted' %(self.name)

    def __del__ (self):
        pass

    def calculate_the_room (self):
        self.s = self.length * self.width
        self.v = self.s * self.hight
        self.wall_A = self.length * self.hight
        self.wall_B = self.width * self.hight
        self.rooms_sort_dict[self.sort]()
        

    def Cable_in_Living_Room(self):
        #self.cable_3x1p5 =
        self.cable_3x2p5 = self.length + 1.5 * self.width + 7 * self.hight
        #self.cable_5x2p5 = 
        #self.cable_5x4 = 

    def Cable_in_Sleeping_Room(self):
        #self.cable_3x1p5 =

        self.cable_3x2p5 = self.length + self.width + 7 * self.hight
        #self.cable_5x2p5 = 
        #self.cable_5x4 = 
    
    def Cable_in_Children_Room(self):
        #self.cable_3x1p5 =
        self.cable_3x2p5 = self.length + self.width + 5 * self.hight
        #self.cable_5x2p5 = 
        #self.cable_5x4 = 

    def Cable_in_Kitchen(self):
        #self.cable_3x1p5 =
        self.cable_3x2p5 = 3 * self.length + 1 * self.width + 7 * self.hight - 5
        #self.cable_5x2p5 = 
        #self.cable_5x4 = 

    def Cable_in_Dinning_Room(self):
        #self.cable_3x1p5 =
        self.cable_3x2p5 = 0.5 * self.length + self.width + self.hight
        #self.cable_5x2p5 = 
        #self.cable_5x4 = 

    def Cable_in_Bathroom(self):
        #self.cable_3x1p5 =
        self.cable_3x2p5 = 1 * self.length + 1.5 * self.width + 3 * self.hight - 1
        #self.cable_5x2p5 = 
        #self.cable_5x4 = 

    def Cable_in_Storeroom(self):
        #self.cable_3x1p5 =
        self.cable_3x2p5 = 0.5 * self.length + 0.5 * self.width + self.hight
        #self.cable_5x2p5 = 
        #self.cable_5x4 = 

    def Cable_in_Basement(self):
        #self.cable_3x1p5 =
        self.cable_3x2p5 = 0
        #self.cable_5x2p5 = 
        #self.cable_5x4 = 

    def Cable_in_Technik_Room(self):
        #self.cable_3x1p5 =
        self.cable_3x2p5 = 0
        #self.cable_5x2p5 = 
        #self.cable_5x4 = 

    def Cable_in_Flur(self):
        #self.cable_3x1p5 =
        self.cable_3x2p5 = 0.5 * self.length + 0.5 * self.width + self.hight
        #self.cable_5x2p5 = 
        #self.cable_5x4 = 
        
    