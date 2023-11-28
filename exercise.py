import unittest                                                             #Importase a biblioteca unittest para poder usar a subclase TestCase
from fibo import fibonacci                                                  #Importase o script fibo no cal se xera a cadea de Fibonacci

class Test(unittest.TestCase):                                              #Clase Test que hereda de unittest.TestCase

    def test_position(self):                                                #Método de prueba tomando self como parámetro
        list_result = fibonacci(5)                                          #Chamada ao método fibonacci co argumento 5 e gardalo na lista list_result
        self.assertEqual(list_result[4], 3)                                 #Comprobacion de que o quinto numero da secuencia de Fibonacci e 3
        print("O quinto numero da secuencia de Fibonacci e",list_result[4]) #Imprimimos por pantalla o resultado do programa

if __name__ == '__main__':                                                  #Estas duas lineas verifican que o arquivo actual e o principal na execución
    unittest.main()