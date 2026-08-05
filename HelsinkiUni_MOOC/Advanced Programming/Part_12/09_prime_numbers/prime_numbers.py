# Write your solution here
def prime_numbers():
    num = 2

    while True:
        divisor_found = False

        for divisor in range(2, num):
            if num % divisor == 0:
                divisor_found = True
                break

        if divisor_found == False:
            yield num

        num += 1


if __name__ == '__main__':
    numbers = prime_numbers()
    for i in range(8):
        print(next(numbers))