""" 1044 - Múltiplos | Bernardo Soares  | Fabrica de Software """

def lerEntrada():

    a, b = input().split()
    a = int(a)
    b = int(b)
    return a,b

def verificacao(a, b):
    return (a % b == 0 or b % a == 0)

def resultados(flag):
    if flag == 1:
        print('Sao Multiplos')
    else:
        print('Nao sao Multiplos')

def main():
    a, b = lerEntrada()
    result = verificacao(a, b)
    resultados(result)


if __name__ == "__main__":
    main()