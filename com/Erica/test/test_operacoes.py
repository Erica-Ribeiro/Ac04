from unittest import TestCase
from com.Erica.operacoes import Multiplicacao

class TestOperacoes(TestCase):

	def setUp(self):
		self.operacoes = Multiplicacao()
	
	def test_mult(self):
		self.assertEqual(self.operacoes.mult([2,2]), 4, "Resultado deve ser 4")