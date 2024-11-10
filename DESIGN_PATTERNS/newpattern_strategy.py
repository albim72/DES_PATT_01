from typing import Callable

# Definicja interfejsu strategii
class MathStrategy:
    def execute(self, a: float, b: float) -> float:
        raise NotImplementedError("Strategy must implement the execute method.")

# Konkretne strategie
class AddStrategy(MathStrategy):
    def execute(self, a: float, b: float) -> float:
        return a + b

class SubtractStrategy(MathStrategy):
    def execute(self, a: float, b: float) -> float:
        return a - b

class MultiplyStrategy(MathStrategy):
    def execute(self, a: float, b: float) -> float:
        return a * b

class DivideStrategy(MathStrategy):
    def execute(self, a: float, b: float) -> float:
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b

# Klasa kontekstowa, która wykorzystuje strategię
class Calculator:
    def __init__(self, strategy: MathStrategy):
        self.strategy = strategy

    def set_strategy(self, strategy: MathStrategy):
        self.strategy = strategy

    def execute_operation(self, a: float, b: float) -> float:
        return self.strategy.execute(a, b)

# Użycie
if __name__ == "__main__":
    # Wybieramy strategię dodawania
    calculator = Calculator(AddStrategy())
    result = calculator.execute_operation(10, 5)
    print(f"Result of addition: {result}")

    # Zmiana strategii na mnożenie
    calculator.set_strategy(MultiplyStrategy())
    result = calculator.execute_operation(10, 5)
    print(f"Result of multiplication: {result}")

    # Zmiana strategii na dzielenie
    calculator.set_strategy(DivideStrategy())
    result = calculator.execute_operation(10, 5)
    print(f"Result of division: {result}")
