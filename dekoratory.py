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
