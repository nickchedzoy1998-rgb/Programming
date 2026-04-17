class Book:
    def __init__(self, name: str, author: str, genre: str, year: int):
        self.name = name
        self.author = author
        self.genre = genre 
        self.year = year

    ##STUB:# This enables easy printing of a Book object
    def __repr__(self):
        return f"{self.name} ({self.author}), {self.year} - genre: {self.genre}"


# -----------------------------
# Write your solution here
# -----------------------------
def books_of_genre(books: list, genre: str):
    matching_books = []

    for book in books:
        if book.genre == genre:
            matching_books.append(book)

    if matching_books:
        print(f'Books in the {genre} genre:')
        for match in matching_books:
            print(match.__repr__())
    else:
        print(f'There are no books in the {genre} genre')