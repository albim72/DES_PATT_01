from film import Film

class FilmCollection:
    def __init__(self):
        self.films = []
        
    def add_film(self,film:Film):
        self.films.append(film)
        
    def remove_film(self,film:Film):
        self.films.remove(film)
        
    def display_all_films(self):
        for film in self.films:
            print(film.get_info())
