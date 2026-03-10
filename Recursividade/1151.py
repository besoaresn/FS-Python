""" 1151 - Fibonacci Fácil | Bernardo Soares  | Fabrica de Software """

def fib(n):                 # Função para calcular os primeiros n números da sequência de Fibonacci
    a, b = 0, 1             # Inicializa os dois primeiros números da sequência de Fibonacci
    lista = []              # Lista para armazenar os números da sequência de Fibonacci
    for  _ in range(n):     # Loop para calcular os primeiros n números da sequência de Fibonacci
        lista.append(str(a)) # Adiciona o número atual da sequência de Fibonacci à lista, convertendo-o para string
        a, b = b, a + b     # Atualiza os valores de a e b para os próximos números da sequência de Fibonacci (a recebe o valor de b, e b recebe a soma de a e b)
    print(' '.join(lista))  # Imprime os números da sequência de Fibonacci separados por espaço, unindo os elementos da lista com um espaço entre eles

def entrada():              # Função para ler a entrada do usuário, que é o número de termos da sequência de Fibonacci a ser calculada
    n = int(input())        # Lê o número de termos da sequência de Fibonacci a ser calculada
    fib(n)                  # Chama a função fib para calcular e imprimir os primeiros n números da sequência de Fibonacci

def main():                 # Função principal que inicia o programa
    entrada()               # Chama a função de entrada para iniciar o processo

main()