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
