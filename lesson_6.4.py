class Cars:
    name = None
    speed = None
    color = None
    is_police = False

    def __init__(self, name, speed, color, is_police = False):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police
    def go(self):
        return "The car went"
    def stop(self):
        return "The car has stopped"
    def turn(self, direction):
        return "The car turned to " + direction

class TownCar(Cars):
    family = None
    def __init__(self, name, speed, color, family = True):
        super().__init__(name, speed, color)
        self.family = family

class SportCar(Cars):
    def __init__(self, name, speed, color):
        super().__init__(name, speed, color)

class WorkCar(Cars):
    def __init__(self, name, speed, color, is_police):
        super().__init__(name, speed, color, is_police)

class PoliceCar(Cars):
    def __init__(self, name, speed, color):
        super().__init__(name, speed, color, True)

ford = TownCar('Honda', 160, 'black')
print(ford.name, ford.color, ford.speed, ford.is_police)
print(ford.go(), ford.turn('City'), ford.stop())
sport = SportCar('Honda', 180, 'red')
work1 = WorkCar('Honda', 190, 'white', True)
work2 = WorkCar('Zhiguli', 190, 'white', False)
police = PoliceCar('Honda', 180, 'red')