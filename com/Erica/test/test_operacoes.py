from unittest import TestCase
from com.Erica.operacoes import Operacoes

class TestOperacoes(TestCase):

    def setUp(self):
        self.operacoes = Operacoes()

    def test_mult(self):
        self.assertEqual(self.operacoes.multiplicacao(5,5),25,"return 25")
    
        print(5*5)