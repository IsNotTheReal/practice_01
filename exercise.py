import unittest
from fibo import fibonacci  #Importase o script fibo no cal se xera a cadea de Fibonacci

class Test(unittest.TestCase):

    def test_position(self):
        list_result = fibonacci(5)
        self.assertEqual(list_result[4], 3)  #Comprobacion de que o quinto numero da secuencia de Fibonacci e 3
        print("O quinto numero da secuencia de Fibonacci e",list_result[4])

if __name__ == '__main__':
    unittest.main()