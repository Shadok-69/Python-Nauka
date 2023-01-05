# PASJA INFORMATYKI REKURENCJA

# Ćwiczenie 1

def fun(n):
    # przypadek podstawowy - konkretna wartość jest zwracana
    if n==0:
        return 3
    # przypadek rekurencyjny - funkcja wywołuje samą siebie, aż
    # do napotkania przypadku podstawowego
    else: 
        return fun(n-1)+2
 
print(f'Usage: funkcja rekurencyjna: {fun(3)}')

# Cwiczenie 2 - potęgowanie

def potegowanie(w, p):
    if p == 0:
        return 1
    else:
        return w * potegowanie(w, p-1)
    
print(f'Usage: funkcja rekurencyjna potegowanie: {potegowanie(3, 4)}')

# Cwiczenie 3 - Wyznaczenie n-tego elementu ciagu fibonacciego

def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

print(f'Usage: funkcja rekurencyjna-wartość elementu ciagu fibonacci: {fib(4)}')

# Cwiczenie 4 - Silnia

def silnia(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * silnia(n-1)
    
print(f'Usage: funkcja rekurencyjna silnia :{silnia(4)}')