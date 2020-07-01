class Road:
    __length = None
    __width = None
    weigth = None
    thickness = None
    def __init__(self, length, width):
        self.length = length
        self.width = width
        print('Make road_to_ocean_beach')

    def intake(self):
        self.weigth = 30
        self.thickness = 0.08
        intake = self.length * self.width * self.weigth * self.thickness / 1000
        print(f'Need {intake} tons for the building')

road_to_ocean_beach = Road(20108, 9)
road_to_ocean_beach.intake()