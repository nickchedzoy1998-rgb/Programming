# Write your solution here
import re

def is_dotw(my_string: str):
    days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']

    return my_string in days

def all_vowels(my_string: str):
    vowels = ['a', 'e', 'i', 'o', 'u']

    for char in my_string:
        if char not in vowels:
            return False

    return True

def time_of_day(my_string: str):
    pattern = r"^\d{2}:\d{2}:\d{2}$"

    if re.search(pattern, my_string) == None:
        return False

    if int(my_string[0:2]) > 23:
        return False

    if int(my_string[3:5]) > 59:
        return False

    if int(my_string[7:9]) > 59:
        return False

    return True


if __name__ == '__main__':
    print(time_of_day("12:43:01"))
    print(time_of_day("AB:01:CD"))
    print(time_of_day("17:59:59"))
    print(time_of_day("33:66:77"))