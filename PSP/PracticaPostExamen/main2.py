import sys
import math
from multiprocessing import Process, Array

class PrimeRange(Process):
    def __init__(self, start_num, end_num, resultArray, process_name):
        super().__init__()
        self._start_num = start_num
        self._end_num = end_num
        self._resultArray = resultArray
        self._name = process_name
    
    def run(self):
        count = 0
        
        for n in range(self._start_num, self._end_num + 1):
            if n < 2: continue # Saltamos números menores a 2
            
            esPrimo = True
            for i in range(2, int(math.sqrt(n)) + 1):
                if n % i == 0:
                    esPrimo = False
                    break
            
            if esPrimo:
                if count < len(self._resultArray):
                    self._resultArray[count] = n
                    count += 1
                    
        primos_encontrados = [x for x in self._resultArray if x != 0]
        print(f"[{self._name}] encontró: {primos_encontrados}")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Uso: python main.py 'number'")
        sys.exit(1)
    try:
        number = int(sys.argv[1])
    except ValueError:
        print("Error: Ingresa un número entero.")
        sys.exit(1)

    mitad = number // 2

    array1 = Array('i', mitad + 1)
    p1 = PrimeRange(2, mitad, array1, "Proceso 1")
    
    array2 = Array('i', number)
    p2 = PrimeRange(mitad + 1, number, array2, "Proceso 2")

    p1.start()
    p2.start()

    p1.join()
    p2.join()
    
    res1 = [x for x in array1 if x != 0]
    res2 = [x for x in array2 if x != 0]
    total = res1 + res2
    print(f"\nLista TOTAL combinada: {total}")