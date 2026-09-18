import unittest
import importlib 
modulo = "P06_3463_pilha_encadeada"
pilha = importlib.import_module(modulo)
modulo2 = "P06_3463_fila_encadeada"
fila = importlib.import_module(modulo2)

class TestPilha(unittest.TestCase):
    def test_lifo(self):
        p = pilha.PilhaEncadeada()
        p.push(1)
        p.push(2)
        p.push(3)
        self.assertEqual(p.pop(), 3)
        self.assertEqual(p.pop(), 2)
        self.assertEqual(p.pop(), 1)

    def test_empty(self):
        p = pilha.PilhaEncadeada()
        with self.assertRaises(IndexError): p.pop()
        with self.assertRaises(IndexError): p.topo()

    def test_len(self):
        p = pilha.PilhaEncadeada()
        self.assertEqual(len(p), 0)
        p.push(10)
        self.assertEqual(len(p), 1)
        p.push(20)
        self.assertEqual(len(p), 2)
        p.pop()
        self.assertEqual(len(p), 1)
        p.pop()
        self.assertEqual(len(p), 0)

    def test_alternation(self):
        p = pilha.PilhaEncadeada()
        p.push(10)
        p.push(20)
        self.assertEqual(p.pop(), 20)
        p.push(30)
        self.assertEqual(p.pop(), 30)
        self.assertEqual(p.pop(), 10)

    def test_types(self):
        p = pilha.PilhaEncadeada()
        p.push(10)
        p.push("abc")
        p.push(None)
        p.push(10)
        self.assertEqual(p.pop(), 10)
        self.assertIsNone(p.pop())
        self.assertEqual(p.pop(), "abc")
        self.assertEqual(p.pop(), 10)

class TestFila(unittest.TestCase):
    def test_fifo(self):
        f = fila.FilaEncadeada()
        f.enfileirar(10)
        f.enfileirar(20)
        f.enfileirar(30)
        self.assertEqual(f.desenfileirar(), 10)
        self.assertEqual(f.desenfileirar(), 20)
        self.assertEqual(f.desenfileirar(), 30)

    def test_alternation(self):
        f = fila.FilaEncadeada()
        f.enfileirar(10)
        f.enfileirar(20)
        self.assertEqual(f.desenfileirar(), 10)
        f.enfileirar(30)
        f.enfileirar(40)
        self.assertEqual(f.desenfileirar(), 20)
        self.assertEqual(f.desenfileirar(), 30)
        self.assertEqual(f.desenfileirar(), 40)

    def test_to_empty(self):
        f = fila.FilaEncadeada()
        f.enfileirar(10)
        f.enfileirar(20)
        self.assertEqual(f.desenfileirar(), 10)
        self.assertEqual(f.desenfileirar(), 20)
        self.assertTrue(f.esta_vazia())
        f.enfileirar(30)
        self.assertFalse(f.esta_vazia())
        self.assertEqual(f.desenfileirar(), 30)

    def test_empty(self):
        f = fila.FilaEncadeada()
        with self.assertRaises(IndexError): f.desenfileirar()
        with self.assertRaises(IndexError): f.frente()

    def test_len(self):
        f = fila.FilaEncadeada()
        self.assertEqual(len(f), 0)
        f.enfileirar(10)
        self.assertEqual(len(f), 1)
        f.enfileirar(20)
        self.assertEqual(len(f), 2)
        f.enfileirar(30)
        self.assertEqual(len(f), 3)
        f.desenfileirar()
        self.assertEqual(len(f), 2)
        f.desenfileirar()
        self.assertEqual(len(f), 1)
        f.desenfileirar()
        self.assertEqual(len(f), 0)

if __name__ == "__main__":
    unittest.main()