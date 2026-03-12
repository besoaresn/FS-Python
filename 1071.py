""" 1071 - Soma de impares consecutivos| Bernardo Soares  | Fabrica de Software """

def entrada():
    x = int(input())
    y = int(input())
    return x, y

def calculo(x, y):
    a = min(x, y)
    b = max(x, y)
    soma = 0
    for i in range(a + 1, b):
        if i % 2 != 0:
            soma += i
    print(soma)

def main():
    x, y = entrada()
    calculo(x, y)


main()
