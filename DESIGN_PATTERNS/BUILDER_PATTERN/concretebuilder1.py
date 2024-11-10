from builder import Builder
from prod1 import Product1

class ConcreteBuilder(Builder):
    def reset(self):
        self._product = Product1()
        
    def __init__(self) -> None:
        self.reset()

    @property
    def product(self) -> Product1:
        product = self._product
        self.reset()
        return product

    def produce_part_a(self):
        self._product.add("PartA1")

    def produce_part_b(self):
        self._product.add("PartB1")

    def produce_part_c(self):
        self._product.add("PartC1")
        
    
