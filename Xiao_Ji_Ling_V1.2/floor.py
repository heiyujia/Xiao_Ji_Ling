class floor(object):
    def __init__(self):
        self.name = None
        self.flats_number = 0
        self.including_flats_Infos = []
        self.floor_area = 0
        self.floor_cable_length = 0


    def add_flats(self, Info):

        self.including_flats_Infos.append(Info)

    def calculate_the_floor(self):
        for item in self.including_flats_Infos:
            self.floor_cable_length = self.floor_cable_length + float(item.flat_cable_length)
            self.floor_area = self.floor_area + float(item.flat_area)
        self.flats_number = len(self.including_flats_Infos)


    