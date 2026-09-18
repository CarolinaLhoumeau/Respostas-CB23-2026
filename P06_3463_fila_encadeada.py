import importlib

modulo = "P06_3463_pilha_encadeada"
pilha = importlib.import_module(modulo)


class FilaEncadeada:
    def __init__(self):
        self._tamanho = 0
        self.back = pilha.PilhaEncadeada()
        self.front = pilha.PilhaEncadeada()

    def _transferir(self):
        while not self.back.esta_vazia():
            self.front.push(self.back.pop())

    def enfileirar(self, item):
        self.back.push(item)
        self._tamanho += 1

    def desenfileirar(self):
        if self.esta_vazia():
            raise IndexError("A fila está vazia.")

        if self.front.esta_vazia():
            self._transferir()

        self._tamanho -= 1
        return self.front.pop()

    def frente(self):
        if self.esta_vazia():
            raise IndexError("A fila está vazia.")

        if self.front.esta_vazia():
            self._transferir()

        return self.front.topo()

    def esta_vazia(self):
        return self._tamanho == 0

    def __len__(self):
        return self._tamanho

    def __repr__(self):
        if self.esta_vazia():
            return "[]"

        if self.front.esta_vazia():
            self._transferir()

        elementos = []
        temporaria = pilha.PilhaEncadeada()

        while not self.front.esta_vazia():
            elemento = self.front.pop()
            elementos.append(elemento)
            temporaria.push(elemento)

        while not temporaria.esta_vazia():
            self.front.push(temporaria.pop())

        elementos_formatados = []
        for elemento in elementos:
            elementos_formatados.append(
                '"' + elemento + '"' if isinstance(elemento, str) else str(elemento)
            )

        return "[" + ", ".join(elementos_formatados) + "]"


if __name__ == "__main__":
    fila = FilaEncadeada()
    print(fila)
