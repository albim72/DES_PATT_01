import time

#przykład 1
def startstop(funkcja):
    def wrapper(*args):
        print("_"*60)
        print("startowanie procesu...")
        funkcja(*args)
        print("kończenie procesu...")
    return wrapper

def zawijanie(w_co):
    print(f"zawijanie czekoladek w {w_co}")

zw = startstop(zawijanie)
print(zw)
zw("sreberka")

@startstop
def dmuchanie(czego):
    print(f"dmuchanie {czego} na torcie urodzinowym!")

def info():
    print("abc")

dmuchanie("świeczek")

info()

#przykład 2
def pomiarczasu(funkcja):
    def wrapper():
        starttime = time.time()
        funkcja()
        endtime = time.time()
        wynik = endtime - starttime
        print(f"czas wykonania funkcji: {wynik} s")
    return wrapper

def usypiacz(funkcja):
    def wrapper():
        time.sleep(3)
        return funkcja()
    return wrapper

@pomiarczasu
@usypiacz
def biglista():
    sum([i**5 for i in range(10_000_000)])
biglista()

#przykład 3

def debug(funkcja):
    def wrapper(*args):
        print(f"wołana funkcja: {funkcja.__name__}")
        funkcja(*args)
    return wrapper


@debug
def komunikat(n,k):
    print(f"komunikat nr {n} -> {k}")

komunikat(34,"informacja na temat p90")

#przykład 4 - dekorator sprawdzający typy argumentów

def sprawdz_typy(typy):
    def dekorator(funkcja):
        def wrapper(*args,**kwargs):
            for (arg,typ) in zip(args,typy):
                if not isinstance(arg,typ):
                    raise TypeError(f"Argument {arg} nie jest typu: {typ}")
            return funkcja(*args,**kwargs)
        return wrapper
    return dekorator

@sprawdz_typy((int,int))
def mnozenie(a,b):
    return a*b

try:
    print(mnozenie(6,8))
    print(mnozenie(6,"osiem"))
except TypeError as tp:
    print(tp)

#przykład 5 - dekorato służący do memizacji wyników

def memoizacja(funkcja):
    cache = {}

    def wrapper(*args):
        if args in cache:
            print(f"Zwracanie wyniku z cache dla argumentow: {args}")
            print(f"funkcja: {funkcja.__name__}({args}->{funkcja(*args)})")
            return cache[args]
        else:
            wynik=funkcja(*args)
            cache[args] = wynik
            return wynik
    return wrapper


@memoizacja
def fibonacci(n):
    if n<=1:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)

print(fibonacci(10))
