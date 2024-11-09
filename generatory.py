#przykład 1
def liczby():
    wynik = []
    for i in range(33):
        wynik.append(i)
    return wynik

print(liczby())

def genliczby():
    for i in range(33):
        yield i

print(genliczby())
print(list(genliczby()))
for p in genliczby():
    print(p)

#przykład2

def wznowienia(n,k):
    print("wstrzymanie działania 0")
    yield 4535
    print("wznowienie działania 1")

    print("wstrzymanie działania 1")
    yield n+k
    print("wznowienie działania 2")

    n = 8*k-4
    print("wstrzymanie działania 2")
    yield n-k
    print("wznowienie działania 3")

    print("wstrzymanie działania 3")
    yield n*k
    print("wznowienie działania 4")

    print("wstrzymanie działania 4")
    yield n/k
    print("wznowienie działania 5")

print(wznowienia(7,3))
print(list(wznowienia(7,3)))

for i in wznowienia(8,4):
    print("_"*50)
    print(type(i))
    print(f"Zwrócono wartość: {i}")

print("*"*60)

k = wznowienia(9,5)
print(next(k))
print(next(k))
print(next(k))



