class room:
    def __init__ (self, name, length, width, hight, level, sort):
        self.name = name
        self.length = length
        self.width = width
        self.hight = hight
        self.level = level
        self.sort = sort
        self.cable_length = 0
        self.s = 0

    def __del__ (self):
        print ('a room has been deleted')

    def calculate_the_room (self, factor_a =1 , factor_b = 1, factor_c = 1):
        self.s = self.length * self.width
        self.v = self.s * self.hight
        self.wall_A = self.length * self.hight
        self.wall_B = self.width * self.hight
        if self.level == 'Level 1':
            self.cable_length = factor_a * self.length + factor_b * self.width + factor_c * self.hight
        elif self.level == 'Level 2':
            self.cable_length = factor_a * self.length + factor_b * self.width + factor_c * self.hight
        elif self.level == 'Level 3':
            self.cable_length = factor_a * self.length + factor_b * self.width + factor_c * self.hight
        
    