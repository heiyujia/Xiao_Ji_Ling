class flat(object):
    def __init__(self, name = None):
        self.name = name
        self.rooms_number = 0
        self.including_rooms_Infos = []
        self.flat_area = 0
        self.flat_cable_3x2p5 = 0
        self.creat_str = '%s has been created' %(self.name)

    def __del__ (self):
        self.delete_str = '%s has been deleted' %(self.name)


    def add_rooms(self, Info):

        self.including_rooms_Infos.append(Info)

    def calculate_the_flat(self):
        self.flat_cable_3x2p5 = 0
        self.flat_area = 0
        for item in self.including_rooms_Infos:
            self.flat_cable_3x2p5 = self.flat_cable_3x2p5 + float(item.cable_3x2p5)
            self.flat_area = self.flat_area + float(item.s)
        self.rooms_number = len(self.including_rooms_Infos)


    