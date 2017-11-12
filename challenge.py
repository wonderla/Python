a = int(input("Podaj liczbe a: "))
b = int(input("Podaj liczbe b: "))
def counter(a, b):
    return a/b

try:
    print(counter(a,b))
except ZeroDivisionError:
    print("Nie można przez 0")