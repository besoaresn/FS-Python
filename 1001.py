def entrada():
    a = int(input())
    b = int(input())
    return a, b

def soma(a, b):
     x = ( a + b )
     return x

def main():
    a, b = entrada()
    resultado = soma(a, b)
    print(f'X = {resultado}')

main()