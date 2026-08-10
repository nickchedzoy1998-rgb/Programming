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
        rating_string = 'no ratings'

        if self.no_ratings > 0:
            rating_string = f'{self.no_ratings} ratings, average {self.avg_score:.1f} points'
        
        return f'{self.title} ({self.seasons} seasons)\ngenres: {genre_string}\n{rating_string}'
    
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
