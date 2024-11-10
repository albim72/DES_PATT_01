from typing import List
from abc import ABC, abstractmethod

# Klasa reprezentująca wyrażenie w języku operacji matematycznych
class Expression(ABC):
    @abstractmethod
    def interpret(self) -> float:
        pass

# Klasa reprezentująca liczbę
class Number(Expression):
    def __init__(self, value: float):
        self.value = value

    def interpret(self) -> float:
        return self.value

# Klasa reprezentująca dodawanie
class Add(Expression):
    def __init__(self, left: Expression, right: Expression):
        self.left = left
        self.right = right

    def interpret(self) -> float:
        return self.left.interpret() + self.right.interpret()

# Klasa reprezentująca odejmowanie
class Subtract(Expression):
    def __init__(self, left: Expression, right: Expression):
        self.left = left
        self.right = right

    def interpret(self) -> float:
        return self.left.interpret() - self.right.interpret()

# Klasa reprezentująca mnożenie
class Multiply(Expression):
    def __init__(self, left: Expression, right: Expression):
        self.left = left
        self.right = right

    def interpret(self) -> float:
        return self.left.interpret() * self.right.interpret()

# Klasa reprezentująca dzielenie
class Divide(Expression):
    def __init__(self, left: Expression, right: Expression):
        self.left = left
        self.right = right

    def interpret(self) -> float:
        return self.left.interpret() / self.right.interpret()

# Interpreter dla wyrażeń w notacji RPN
class RPNInterpreter:
    def __init__(self):
        self.stack: List[Expression] = []

    def parse_token(self, token: str):
        if token in {"+", "-", "*", "/"}:
            # Pobierz dwa ostatnie elementy ze stosu
            right = self.stack.pop()
            left = self.stack.pop()

            # Stwórz odpowiedni obiekt operacji i dodaj go na stos
            if token == "+":
                self.stack.append(Add(left, right))
            elif token == "-":
                self.stack.append(Subtract(left, right))
            elif token == "*":
                self.stack.append(Multiply(left, right))
            elif token == "/":
                self.stack.append(Divide(left, right))
        else:
            # Jeśli token jest liczbą, zamień ją na obiekt Number i dodaj na stos
            self.stack.append(Number(float(token)))

    def interpret(self, expression: str) -> float:
        tokens = expression.split()
        for token in tokens:
            self.parse_token(token)
        # Po przetworzeniu wszystkich tokenów wynik interpretacji jest na szczycie stosu
        return self.stack.pop().interpret()

# Przykład użycia interpretera
if __name__ == "__main__":
    interpreter = RPNInterpreter()
    
    expression = "3 5 + 2 * 10 /"  # Przykładowe wyrażenie RPN: (3 + 5) * 2 / 10
    result = interpreter.interpret(expression)
    print(f"Wynik wyrażenia '{expression}': {result}")
