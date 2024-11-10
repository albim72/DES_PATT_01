import unittest


# Wzorzec Singleton
class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance


# Wzorzec Factory Method
class Product:
    def __str__(self):
        return "This is a product."


class ConcreteProductA(Product):
    def __str__(self):
        return "This is product A."


class ConcreteProductB(Product):
    def __str__(self):
        return "This is product B."


class ProductFactory:
    def create_product(self, product_type: str) -> Product:
        if product_type == 'A':
            return ConcreteProductA()
        elif product_type == 'B':
            return ConcreteProductB()
        else:
            raise ValueError("Unknown product type")


# Testowanie klas
class TestPatterns(unittest.TestCase):

    def test_singleton(self):
        # Testujemy, czy Singleton zawsze zwraca tę samą instancję
        singleton1 = Singleton()
        singleton2 = Singleton()
        self.assertIs(singleton1, singleton2, "Singleton should return the same instance.")

    def test_factory_method(self):
        factory = ProductFactory()

        # Tworzymy produkt A i B
        product_a = factory.create_product('A')
        product_b = factory.create_product('B')

        # Sprawdzamy, czy produkty są poprawne
        self.assertIsInstance(product_a, ConcreteProductA, "Product A should be of type ConcreteProductA.")
        self.assertIsInstance(product_b, ConcreteProductB, "Product B should be of type ConcreteProductB.")

        # Sprawdzamy, czy stringi produktów są prawidłowe
        self.assertEqual(str(product_a), "This is product A.")
        self.assertEqual(str(product_b), "This is product B.")


if __name__ == "__main__":
    unittest.main()
