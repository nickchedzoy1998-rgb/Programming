# WRITE YOUR SOLUTION HERE:

class Car:
    def __init__(self):
        self.odometer = 0
        self.tank = 0

    def fill_up(self):
        self.tank = 60

    def drive(self, km:int):
        km_left_to_drive = km

        while self.tank >= 1 and km_left_to_drive >= 1:
            self.odometer += 1
            self.tank -=1
            km_left_to_drive -=1
        
    def __str__(self):
        return f'{self.__class__.__name__}: odometer reading at {self.odometer} km, petrol remaining {self.tank} litres'
    

if __name__ == '__main__':
    car = Car()
    print(car)
    car.fill_up()
    print(car)
    car.drive(20)
    print(car)
    car.drive(50)
    print(car)
    car.drive(10)
    print(car)
    car.fill_up()
    car.fill_up()
    print(car)