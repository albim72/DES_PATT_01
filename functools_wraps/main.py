from funcwraps import dekorator
from cache import fibonacci
from obliczenie import podwojenie

def main():
    print("przykład użycia dekoratora z @wraps! ")

    @dekorator
    def wrapsprzyklad():
        return "prosta funkcja"

    print(wrapsprzyklad())

    print("przykład użycia lru_cache!")

    print(fibonacci(10))

    print("przykład użycia  ** partial **")
    print(podwojenie(5))


if __name__ == '__main__':
    main()
