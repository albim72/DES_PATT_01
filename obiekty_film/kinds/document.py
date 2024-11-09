from film import Film

class DocumentaryFilm(Film):
    def play(self):
        print(f'Odtwarzanie filmu dokumentalnego: {self.title}')

    def get_info(self) -> str:
        return f"{self.title}, reżyseria: {self.director},produkcja: {self.year}, czas trwania [h]: {self.duration}"
