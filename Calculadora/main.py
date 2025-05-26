# main.py

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error: división por cero"
    return a / b

if __name__ == "__main__":
    print("Suma:", suma(5, 3))
    print("Resta:", resta(5, 3))
    print("Multiplicación:", multiplicacion(5, 3))
    print("División:", division(5, 0))
hola