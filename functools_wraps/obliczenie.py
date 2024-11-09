from functools import partial

def mnozenie(a,b):
    return a*b

podwojenie = partial(mnozenie,2)
