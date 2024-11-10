# Definicja metaklasy IterableMeta
class IterableMeta(type):
    def __new__(cls, name, bases, dct):
        # Tworzenie klasy przy użyciu metaklasy
        dct['__iter__'] = cls.__iter__
        dct['__next__'] = cls.__next__
        return super().__new__(cls, name, bases, dct)

    # Metoda __iter__ dla iterowania
    def __iter__(self):
        self._iterator = iter(self.collection)  # Tworzenie iteratora
        return self

    # Metoda __next__ dla przechodzenia do następnego elementu
    def __next__(self):
        if not hasattr(self, '_iterator'):
            raise TypeError("Iterator not initialized. Call iter() first.")
        return next(self._iterator)


# Przykład klasy używającej metaklasy IterableMeta
class IterableClass(metaclass=IterableMeta):
    def __init__(self, collection):
        if not isinstance(collection, (list, set, dict)):
            raise TypeError("Unsupported collection type. Use list, set, or dict.")
        self.collection = collection


# Testowanie
# Tworzenie instancji klasy z różnymi kolekcjami
list_instance = IterableClass([1, 2, 3])
set_instance = IterableClass({4, 5, 6})
dict_instance = IterableClass({'a': 7, 'b': 8, 'c': 9})
tuple_instance = IterableClass((45,26,2678,90))

# Test iterowania za pomocą __next__()
print("Iterating list_instance:")
list_iter = iter(list_instance)
print(next(list_iter))  # 1
print(next(list_iter))  # 2
print(next(list_iter))  # 3

print("\nIterating set_instance:")
set_iter = iter(set_instance)
print(next(set_iter))  # Element z {4, 5, 6}
print(next(set_iter))  # Element z {4, 5, 6}
print(next(set_iter))  # Element z {4, 5, 6}

print("\nIterating dict_instance:")
dict_iter = iter(dict_instance)
print(next(dict_iter))  # 'a'
print(next(dict_iter))  # 'b'
print(next(dict_iter))  # 'c'

print("\nIterating tuple_instance:")
tuple_iter = iter(tuple_instance)
print(next(tuple_iter))
print(next(tuple_iter))
print(next(tuple_iter))

# Test pętli for
print("\nUsing for loop on list_instance:")
for item in list_instance:
    print(item)

print("\nUsing for loop on set_instance:")
for item in set_instance:
    print(item)

print("\nUsing for loop on dict_instance:")
for item in dict_instance:
    print(item)
