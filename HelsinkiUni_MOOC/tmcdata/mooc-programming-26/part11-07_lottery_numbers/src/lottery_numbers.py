# WRITE YOUR SOLUTION HERE:
class LotteryNumbers:
    def __init__(self, week_no: int, lotto_nos: list):
        self.week_no = week_no
        self.lotto_nos = lotto_nos

    def number_of_hits(self, numbers: list) -> float:
        return len([n for n in numbers if n in self.lotto_nos])
    
    def hits_in_place(self, numbers) -> list:
        return [n if n in self.lotto_nos else -1 for n in numbers]
    

if __name__ == '__main__':
    week5 = LotteryNumbers(5, [1,2,3,4,5,6,7])
    my_numbers = [1,4,7,11,13,19,24]

    print(week5.number_of_hits(my_numbers))

    week8 = LotteryNumbers(8, [1,2,3,10,20,30,33])
    my_numbers = [1,4,7,10,11,20,30]

    print(week8.hits_in_place(my_numbers))