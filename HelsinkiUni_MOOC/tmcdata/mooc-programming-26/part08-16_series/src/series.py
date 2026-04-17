# Write your solution here:

class Series():
    def __init__(self, title, seasons, genres):
        self.title = title
        self.seasons = seasons
        self.genres = genres
        self.no_ratings = 0
        self.avg_score = 0
        self.total_score = 0
    
    def __str__(self):
        genre_string = ", ".join(self.genres)
        rating_string = 'No Ratings'

        if self.no_ratings > 0:
            rating_string = f'{self.no_ratings} Ratings, Average {self.avg_score:.1f} points'
        
        return f'{self.title} ({self.seasons} seasons)\nGenres: {genre_string}\n{rating_string}'
    
    def rate(self, rating:int):
        if rating < 0 or rating > 5:
            raise ValueError('Rating must be between 0 and 5')
        else:
            self.no_ratings += 1
            self.total_score += rating
            self.avg_score = (float(self.total_score / self.no_ratings))
        


def minimum_grade(rating: float, series_list: list):
    matches = []
    for series in series_list:
        if series.avg_score >= rating:
            matches.append(series)
    return matches
        
def includes_genre(genre: str, series_list: list):
    matches = []
    for series in series_list:
        if genre in series.genres:
            matches.append(series)
    return matches

while True:
    s1 = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
    s1.rate(5)

    s2 = Series("South Park", 24, ["Animation", "Comedy"])
    s2.rate(3)

    s3 = Series("Friends", 10, ["Romance", "Comedy"])
    s3.rate(2)

    series_list = [s1, s2, s3]

    print("a minimum grade of 4.5:")
    for series in minimum_grade(4.5, series_list):
        print(series.title)

    print("genre Comedy:")
    for series in includes_genre("Comedy", series_list):
        print(series.title)
    break
        
# if __name__ == '__main__':
#     s1 = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
#     s1.rate(5)

#     s2 = Series("South Park", 24, ["Animation", "Comedy"])
#     s2.rate(3)

#     s3 = Series("Friends", 10, ["Romance", "Comedy"])
#     s3.rate(2)

#     series_list = [s1, s2, s3]

#     print(series_list)