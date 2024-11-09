from film import Film
from award import AwardWinning

class ActionFilm(Film,AwardWinning):
    def __init__(self, title: str, director: str, year: int, duration: float):
        Film.__init__(self,title, director, year, duration)
        AwardWinning.__init__(self)

    def play(self):
        print(f"odtwarzanie filmu akcji: {self.title}")

    def get_info(self) -> str:
        info = f"{self.title}, reżyseria: {self.director},produkcja: {self.year}, czas trwania [h]: {self.duration}"
        if self.awards:
            info += f" | Nagrody: {','.join(self.awards)}"
        return info
