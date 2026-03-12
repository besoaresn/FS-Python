""" 1006 - Média 2 | Bernardo Soares  | Fabrica de Software """

def entradaDados():
    A = float(input())
    B = float(input())
    C = float(input())
    return A, B, C

def media(A, B, C):
    media = (A * 2 + B * 3 + C * 5) / 10
    return media

def main():
    A, B, C = entradaDados()
    mediaAluno = media(A, B, C)
    print(f'MEDIA = {mediaAluno:.1f}')

main()