from director import  Director
from concretebuilder1 import ConcreteBuilder

director = Director()
builder = ConcreteBuilder()

director.builder = builder

print(f"\nProdukt minimalny")
director.build_minimal_version()
builder.product.list_parts()

print(f"\nProdukt pełny")
director.build_full_version()
builder.product.list_parts()

#wersja użytkownika
print("\nwłasna wersja produktu [AC]")
builder.produce_part_a()
builder.produce_part_c()
builder.product.list_parts()

