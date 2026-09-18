class Node:
    def __init__(self, item):
        self.proximo = None
        self.valor = item

    def __repr__(self):
        return str(self.valor)


def str_melhor(item):
    saida = str()
    if isinstance(item, str):
        saida += '"'
        saida += item
        saida += '"'
    else:
        saida = str(item)
    return saida


class PilhaEncadeada:
    def __init__(self):
        self._topo = None
        self._tamanho = 0

    def push(self, item):
        novo = Node(item)
        novo.proximo = self._topo
        self._topo = novo
        self._tamanho += 1

    def pop(self):
        if self._tamanho == 0:
            raise IndexError("A pilha está vazia.")

        saida = self._topo.valor
        self._topo = self._topo.proximo
        self._tamanho -= 1
        return saida

    def topo(self):
        if self._tamanho == 0:
            raise IndexError("A pilha está vazia.")
        return self._topo.valor

    def esta_vazia(self):
        return self._tamanho == 0

    def __len__(self):
        return self._tamanho

    def __repr__(self):
        elementos = []
        atual = self._topo

        while atual is not None:
            elementos.append(str_melhor(atual.valor))
            atual = atual.proximo

        return "[" + ", ".join(elementos) + "]"


if __name__ == "__main__":
    pilha = PilhaEncadeada()
    print(pilha)
