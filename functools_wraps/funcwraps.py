from functools import wraps

def dekorator(funkcja):
    @wraps(funkcja)
    def wrapper(*args,**kwargs):
        print("informacja:abc")
        wynik = funkcja(*args,**kwargs)
        print("zakończenie!")
        return wynik
    return wrapper
