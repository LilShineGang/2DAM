from multiprocessing import Process, current_process, Value
from time import sleep
from random import randint

shared_total: int = 0

class Adder(Process):

    def __init__(self, n1:int, n2:int, shared_total: Value):
        super().__init__()

        self._n1 = n1
        self._n2 = n2
        self._shared_total: Value = shared_total
        self._lock = lock
        
    def run(self):
        with lock:
            self.shared_total.value += self._n1 + self._n2
        print(f"suma: {current_process().pid}: {self._n1} + {self._n2} = {self._n1 + self._n2}")
        print(f"hasta ahora: {self.shared_total.value}")
        print()
        
if __name__ == "__main__":
    
    lock = Lock()
    shared_total = Value("i", 0)
    processes = [ Adder(randint(1, 10), randint(1, 10), shared_total, lock) for _ in range(5) ]

    for p in processes:
        p.start()

    for p in processes:
        p.join()

    print(f"Proceso padre, con PID={current_process().pid} terminado")
    print(f"Total: {shared_total.value}")
