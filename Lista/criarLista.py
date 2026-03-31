class No:
    def __init__(self, valor):
        self.valor = valor
        self.prox = None

    def mostrar_no(self):
        print(self.valor)

class listaEncadeada:
    def __init__(self):
        self.primeiro = None

    def lista_vazia(self):
        return self.primeiro is None

    def mostrar_lista(self):
        if  self.lista_vazia():
            print("Lista vazia")
            return None
        atual = self.primeiro
        while atual is not None:
            atual.mostrar_no()
            atual = atual.prox

    def inserir_inicio(self, valor):
        novo = No(valor)
        novo.prox = self.primeiro
        self.primeiro = novo

    def inserir_fim(self, valor):
        novo = No(valor)
        if self.lista_vazia():
            return

        atual = self.primeiro
        while atual.prox is not None:
            atual = atual.prox
        atual.prox = novo

    def excluir(self, valor):








lista = listaEncadeada()

lista.inserir_inicio(1)
lista.inserir_inicio(2)
lista.inserir_inicio(3)

lista.mostrar_lista()