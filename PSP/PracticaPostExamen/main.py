'''
terminal: python main.py 'number'

for n in range(2, raiz cuadrada de 10 + 1)

number / n

calcular todos los primos del numero ingresado con sys
'''

import sys
import math
from multiprocessing import Process, Array

class PrimeFactorization(Process):
    def __init__(self, startNum, endNum, resultArray, process_name):
        super().__init__()
        self._startNum = startNum
        self._endNum = endNum
        self._resultArray = resultArray
        self._process_name = process_name

    def run(self):
        'number = self._number'
        count = 0

        for n in range(self._startNum, self._endNum + 1):
            if n < 2: continue

            esPrimo = True
            for i in range(2, int(math.sqrt(n)) + 1):
                if n % i == 0:
                    esPrimo = False
                    break

            if esPrimo:
                if count < len(self._resultArray):
                    self._resultArray[count] = n
                    count += 1
                    
        primosEncontrados = [x for x in self._resultArray if x != 0]
        print(f"[{self._process_name}] encontró: {primosEncontrados}")

        '''
        for n in range(2, number + 1):
            esPrimo = True

            for i in range(2, int(math.sqrt(n)) + 1):
                if n % i == 0:
                    esPrimo = False
                    break
            if esPrimo:
                if count < len(self._resultArray):
                    self._resultArray[count] = n
                    count += 1

        number = self._number
        primos = []
        
        for n in range(2, int(math.sqrt(number)) + 1):
            while number % n == 0:
                primos.append(n)
                number //= n
        if number > 1:
            primos.append(number)

        for i, primo in enumerate(primos):
            if i < len(self._resultArray):
                self._resultArray[i] = primo
'''
if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python main.py 'number'")
        sys.exit(1)
    try:
        number = int(sys.argv[1])
    except ValueError:
        print("Error: Ingresa un número entero.")
        sys.exit(1)

    resultArray = Array('i', number)

    mitad = number // 2
    
    mitad1 = Array('i', mitad + 1)
    p1 = PrimeFactorization(2, mitad, mitad1, "Proceso 1")
    
    mitad2= Array('i', number)
    p2 = PrimeFactorization(mitad + 1, number, mitad2, "Proceso 2")

    p1.start()
    p2.start()

    p1.join()
    p2.join()
    
    '''
    p = PrimeFactorization(number, resultArray)
    p.start()
    p.join()
    '''

    'final_result = [x for x in resultArray if x != 0]'
    
    res1 = [x for x in mitad1 if x != 0]
    res2 = [x for x in mitad2 if x != 0]