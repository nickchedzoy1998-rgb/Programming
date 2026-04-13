import time

class Stopwatch:
    def __init__(self):
        self.seconds = 0
        self.minutes = 0

    def tick(self):
        if self.seconds < 59:
            self.seconds += 1
        else:
            self.seconds = 0
            self.minutes += 1
    
    def __str__(self):
        return(f'{self.minutes:02}:{self.seconds:02}')


class Clock:
    def __init__(self):
        self.hour = 0
        self.minute = 0
        self.second = 0

    def tick(self):
        if self.second < 59:
            self.second += 1
        else:
            self.second = 0
            if self.minute < 59:
                self.minute += 1
            else:
                self.minute = 0
                if self.hour < 23:
                    self.hour += 1
                else:
                    self.hour = 0

    def set(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

   
    def __str__(self):
        return(f'{self.hour:02}:{self.minute:02}:{self.second:02}')

clock = Clock()
clock.set(14,52,38)
while True:
    clock.tick()
    print(clock)
    time.sleep(1)