""" 1555 - Funções | Bernardo Soares  | Fabrica de Software """

def entrada():
    n = int(input())
    casos = []
    for _ in range(n):
        x, y = map(int, input().split())
        casos.append((x, y))

    return casos

def funcoes(x, y):
    r = (3 * x) * (3 * x) + y * y
    b = 2 * (x * x) + (5 * y) * (5 * y)
    c = -100 * x + y * y * y
    return (r, b, c)

def verGanhador(r, b, c):
    if r > b and r > c:
        print("Rafael ganhou")
    elif b > r and b > c:
        print("Beto ganhou")
    else:
        print("Carlos ganhou")

def main():
    casos = entrada()

    for x, y in casos:
        r, b, c = funcoes(x, y)
        verGanhador(r, b, c)

main()