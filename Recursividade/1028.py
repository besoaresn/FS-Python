""" 1028 - Figurinhas | Bernardo Soares  | Fabrica de Software """

def calculo(a, b):  # Algoritmo de Euclides para calcular o máximo divisor comum (MDC)

    if b == 0:      # Base b for 0, mdc é a
        return a
    else:
        return calculo(b, a % b) # Chama a função recursivamente, passando b e o resto da divisão de a por b

def entradaValores():           # Lê o número de casos de teste e os pares de números para calcular o MDC
    n = int(input())            # Lê o número de casos de teste
    for _ in range(n):          # Para cada caso de teste, lê os dois números, calcula o MDC e imprime o resultado
        a, b = map(int, input().split())    # Lê os dois números a e b
        mdc = calculo(a, b)                 # Calcula o MDC usando a função calculo
        print(mdc)             # Printa Resultado do MDC

def main():
    entradaValores()           # Chama a função de entrada para iniciar o processo

main()