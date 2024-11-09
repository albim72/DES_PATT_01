class ContextManager:
    def __init__(self):
        print("inicjacja metody __init__()")

    def __enter__(self):
        print("inicjacja metody __enter__()")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("inicjacja metody __exit__()")

with ContextManager() as manager:
    print("działania wewnątrz instrukcji with...")
