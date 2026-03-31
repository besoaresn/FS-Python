def entradaDados():
    lista = input().slipt()
    for i in range(len(lista)):
        lista[i] = float(lista[i])
        return lista


def verificaPosicao(lista):
    for i in range(len(lista)):
        if i % 2 == 0:
            print("Valor na posição {}: {}".format(i, lista[i]))

def main():
    lista = entradaDados()
    verificaPosicao(lista)

if __name__ == "__main__":
  main()
