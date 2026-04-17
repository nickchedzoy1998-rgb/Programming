# Write your solution here!
class  NumberStats:
    def __init__(self):
        self.numbers = 0
        self.sum = 0

    def add_number(self, number:int):
        self.numbers += 1
        self.sum += number

    def count_numbers(self):
        return self.numbers
    
    def get_sum(self):
        if self.numbers > 0:
            return self.sum
        else:
            return 0
    
    def average(self):
        if self.numbers > 0:
            return self.sum / self.numbers
        else:
            return 0

stats = NumberStats()
even_numbers = NumberStats()
odd_numbers = NumberStats()

print('Type in your Numbers:\n')

while True:
    number = int(input('Enter a Number: '))

    if number == -1:
        break
    stats.add_number(number)
    if number % 2 == 0:
        even_numbers.add_number(number)
    else:
        odd_numbers.add_number(number)

print(f'Sum of Numbers: {stats.get_sum()}')
print(f'Mean of Numbers: {stats.average()}')
print(f'Sum of even numbers: {even_numbers.get_sum()}')
print(f'Sum of odd numbers: {odd_numbers.get_sum()}')