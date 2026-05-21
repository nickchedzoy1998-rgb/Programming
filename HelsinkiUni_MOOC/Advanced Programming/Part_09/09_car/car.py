# WRITE YOUR SOLUTION HERE:

class Car:
    def __init__(self):
        self.__odometer = 0
        self.__tank = 0

    def fill_up(self):
        self.__tank = 60

    def drive(self, km:int):
        km_left_to_drive = km

        while self.__tank >= 1 and km_left_to_drive >= 1:
            self.__odometer += 1
            self.__tank -=1
            km_left_to_drive -=1
        
    def __str__(self):
        return f'{self.__class__.__name__}: odometer reading at {self.__odometer} km, petrol remaining {self.__tank} litres'
    

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