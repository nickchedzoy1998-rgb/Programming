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
        if self.day + days < 31:
            return SimpleDate(self.day+days, self.month, self.year)
        
        else:
            days_to_end_month = 30 - self.day
            days_to_end_year = ((12 - (self.month + 1)) * 30) + days_to_end_month

            if days <= days_to_end_year:
                # 7.8.2024 Add 65
                month = self.month + 1
                days -= days_to_end_month

                if days < 30:
                    return SimpleDate(days, month, self.year)
                
                else:
                    date = days % 30
                    month = ((days - date) / 30) + self.month

                    return SimpleDate(date, month, self.year)
                
            else:
                if days < days_to_end_year + (12 * 30):
                    year = self.year + 1
                    days_rem = days - days_to_end_year
                    if days_rem < 31:
                        return SimpleDate(days_rem, 1, year)
                    
                    else:
                        year = self.year + 1
                        date = days_rem % 30
                        month =  1 + ((days_rem - date) / 30)

                        return SimpleDate(date, month, year)
                
                else:
                    year = self.year + 1
                    days_rem = days - days_to_end_year
                    date = days_rem % 30
                    month = (((days_rem - date) / 30) % 12)
                    year = year + ((((days_rem - date) / 30)-month) / 12)

                    return SimpleDate(date, month, year)



        


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