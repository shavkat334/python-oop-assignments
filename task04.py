class movie:

    def __init__(self, title, genre, duration, rating):
        self.title = title
        self.genre = genre
        self.duration = duration
        self.rating = rating

    def show_info(self) -> None:
        print(f'movie(movie_name="{self.title}")')

m01 = movie('titanic', 'comedy', 200, 10.0)

m01.show_info()
