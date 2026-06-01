# WRITE YOUR SOLUTION HERE:
import os
import string

def most_common_words(filename: str, lower_limit: int) -> dict:

    script_dir = os.path.dirname(__file__)
    absolute_path = os.path.join(script_dir, filename)

    with open(absolute_path, 'r') as file:
        content = file.read()
        clean_content = "".join([char for char in content if char not in string.punctuation])
        words = clean_content.split()
    
    return {w: words.count(w) for w in words if words.count(w)>= lower_limit}


if __name__ == '__main__':
    print(most_common_words('comprehensions.txt', 3))