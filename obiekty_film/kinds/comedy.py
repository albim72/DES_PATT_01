from film import Film
from series import SeriesPart

class ComedyFilm(Film,SeriesPart):
    def __init__(self, title: str, director: str, year: int, duration: float, series_name:str, part_number:int):
        Film.__init__(self,title, director, year, duration)
        SeriesPart.__init__(self,series_name,part_number)

    def play(self):
        print(f"odtwarzanie komedii: {self.title}")

    def get_info(self) -> str:
        info = f"{self.title}, reżyseria: {self.director},produkcja: {self.year}, czas trwania [h]: {self.duration}"
        series_info = self.get_series_info()
        info += f" | {series_info}"
        return info
