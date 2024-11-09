from collection import FilmCollection
from kinds.action import ActionFilm
from kinds.comedy import ComedyFilm
from kinds.document import DocumentaryFilm


collection = FilmCollection()
film1 = ActionFilm("Mad Max: Fury Road", "George Miller",2015,2)
film2 = ComedyFilm("the Grand Budapest Hotel","Wes Anderson",2014,1.75,
                   "Wes Anderson's Universe",1)
film3 = DocumentaryFilm("The Social Dilemma","Jeff Orlowsky",2020,1.7)

film1.add_award("Oscar za najlepszy montaż")
film1.add_award("Oscar za najlepszy dźwiek")

collection.add_film(film1)
collection.add_film(film2)
collection.add_film(film3)

collection.display_all_films()

film1.play()
film2.play()
