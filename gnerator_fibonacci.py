def fibonacci_prime_generator(limit=None):
    """
    Generator liczb Fibonacciego, które są liczbami pierwszymi.
    
    :param limit: Opcjonalny limit ilości generowanych liczb.
    :type limit: int or None
    :yield: Kolejna liczba Fibonacciego będąca liczbą pierwszą.
    :rtype: int
    """
    a, b = 0, 1  # Początkowe wartości dla ciągu Fibonacciego
    count = 0    # Licznik generowanych liczb

    def is_prime(n):
        """Sprawdza, czy liczba n jest liczbą pierwszą."""
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    while True:
        a, b = b, a + b  # Następna liczba Fibonacciego
        if is_prime(a):
            yield a  # Zwróć liczbę, jeśli jest liczbą pierwszą
            count += 1
            if limit is not None and count >= limit:
                break  # Przerwij, jeśli osiągnięto limit


# Przykład użycia generatora
generator = fibonacci_prime_generator(limit=5)  # Limitujemy do 5 liczb pierwszych z ciągu Fibonacciego

for prime in generator:
    print(prime)
