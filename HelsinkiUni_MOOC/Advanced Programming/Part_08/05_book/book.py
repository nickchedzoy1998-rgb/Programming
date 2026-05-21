# Write your solution here:
class Book:
    def __init__(self, name: str, author: str, genre: str, year: int):
        self.name = name
        self.author = author
        self.genre = genre
        self.year = year

    def show_details(self):
        print(f'The genre of the book {self.name} is {self.genre}, written by {self.author} and released in {self.year}.')

if __name__ == '__main__':
    python = Book("Fluent Python", "Luciano Ramalho", "programming", 2015)
    everest = Book("High Adventure", "Edmund Hillary", "autobiography", 1956)

    python.show_details()
    everest.show_details()