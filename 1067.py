""" 1067 - Números Ímpares | Bernardo Soares  | Fabrica de Software """

def entrada():
    x = int(input())
    return x

def resultado(x):

    for i in range(1, x+1):
        if i % 2 != 0:
            print(i)

def main():
    x = entrada()
    resultado(x)

main()