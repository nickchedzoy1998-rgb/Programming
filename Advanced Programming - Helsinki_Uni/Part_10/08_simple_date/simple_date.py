# WRITE YOUR SOLUTION HERE:

class SimpleDate:
    def __init__(self, day: float, month: float, year: float):
        self.day = day
        self.month = month
        self.year = year

    def __str__(self):
        return f'{self.day:.0f}.{self.month:.0f}.{self.year:.0f}'

    def __lt__(self, other):
        if self.year < other.year:
            return True
        
        elif self.year == other.year:
            if self.month < other.month:
                return True
            
            elif self.month == other.month:
                if self.day < other.day:
                    return True
                
        return False
    
    def __gt__(self, other):
        if self.year > other.year:
            return True
        
        elif self.year == other.year:
            if self.month > other.month:
                return True
            
            elif self.month == other.month:
                if self.day > other.day:
                    return True
                
        return False

    def __eq__(self, other):
        return self.year == other.year and self.month == other.month and self.day == other.day
    

    def __ne__(self, other):
        return self.year != other.year or self.month != other.month or self.day != other.day
    

    def __add__(self, days):
        new_day = self.day + days
        new_month = self.month
        new_year = self.year
        
        while new_day > 30:
            new_day -= 30
            new_month += 1
        
        while new_month > 12:
            new_month -= 12
            new_year += 1
        
        return SimpleDate(new_day, new_month, new_year)
    
    def __sub__(self, other):
        tv1 = self.year * 360 + self.month * 30 + self.day
        tv2 = other.year * 360 + other.month * 30 + other.day
        return abs(tv1 - tv2)



        


if __name__ == '__main__':
    d1 = SimpleDate(4, 10, 2020)
    d2 = SimpleDate(28, 12, 1985)
    d3 = SimpleDate(28, 12, 1985)

    print(d1 == d2)
    print(d1 != d2)
    print(d1 == d3)
    print(d1 < d2)
    print(d1 > d2)

    d3 = d1 + 3
    d4 = d2 + 400

    print(d1)
    print(d2)
    print(d3)
    print(d4)