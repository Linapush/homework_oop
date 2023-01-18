# Мьютекс можно представить в виде переменной, которая может находиться в двух состояниях: в заблокированном и в незаблокированном. При входе в свою критическую секцию поток вызывает функцию перевода мьютекса в заблокированное состояние, при этом поток блокируется до освобождения мьютекса, если другой поток уже владеет им.
# Конструктор очереди FIFO . maxsize — это целое число, которое устанавливает верхний предел количества элементов, которые могут быть помещены в очеред
# Блокировка взаимного исключения (мьютекс) для процессов через класс multiprocessing.Lock 
# Событие управляет флагом, который может быть установлен в значение true с помощью set()метода и сброшен в значение false с помощью clear()метода. Метод wait()блокируется до тех пор, пока флаг не станет истинным. Флаг изначально ложный.
# wait - блокировать до тех пор, пока внутренний флаг не станет истинным. 
# При вызове с блокирующим аргументом, установленным на True(по умолчанию), блокируем до тех пор, пока блокировка не будет разблокирована, затем установим его в заблокированное и вернем True.
# Когда замок заблокирован, сбросьте его до разблокированного и вернитесь
# timeout - задает время, в течение которого поток будет находиться в заблокированном состоянии при попытке захватить уже занятый Lock-объект. 
# Метод lock блокирует вызывающий поток до тех пор, пока этот поток не получит права владения мьютексом
# Блокировка — механизм синхронизации, позволяющий обеспечить исключительный доступ к разделяемому ресурсу между несколькими потоками.
# Переменная условия позволяет одному или нескольким потокам ждать, пока они не будут уведомлены другим потоком.

from multiprocessing import Process, Queue, Event, Lock
from random import randint
from time import sleep

class Client:
    def __init__(self, name):        
        self.name = name

class Barber:    
    TIMEOUT = 20
    WORK_INT = (6, 8)

    def __init__(self):
        self.__client_came = Event()
        
    def barber_sleep(self):
        print('Клиенты еще не пришли. Можно и поспать')        
        sleep_result = self.__client_came.wait(timeout=Barber.TIMEOUT)
        return sleep_result

    def barber_call(self):
        self.__client_came.set() 
           
    def barber_cut(self, client: Client):        
        sleep(randint(*Barber.WORK_INT))
        print('Парикмахер стрижёт клиента {}'.format(client.name))

    def barber_greet(self, client: Client):
        print('Парикмахер приветствует клиента {}'.format(client.name))        
        self.__client_came.clear()
        self.barber_cut(client)        
        print('Клиент {} пострижен. Ура!'.format(client.name))
        print('Клиент {} ушёл из салона'.format(client.name))

class Salon:
    def __init__(self, q_size: int, mutex: Lock):        
        self.q_size = q_size
        self.mutex = mutex        
        self.__queue = Queue(maxsize=q_size)
        self.__worker = Barber()        
        self.__process = Process(target=self.salon_work)

    def salon_open(self):        
        print('Салон открылся')
        self.__process.start()

    def salon_work(self):
        while True:            
            self.mutex.acquire()
            if self.__queue.empty():                
                self.mutex.release()
                sleep_result = self.__worker.barber_sleep()                
                if not sleep_result:
                    self.salon_close()                    
                    break
            else:                
                self.mutex.release()
                client = self.__queue.get()                
                self.__worker.barber_greet(client)

    def door_enter(self, client: Client):        
        with mutex: 
            print('Клиент {} пришёл в салон'.format(client.name))            
            if self.__queue.full():
                print('Клиент {} увидел полную очередь и ушёл из салона'. format(client.name))            
            else:
                values = client.name                
                print('Клиент {} хочет модную стрижку. Ожидает в приёмной'.format(*values))
                self.__queue.put(client)                
                self.__worker.barber_call()

    def salon_close(self):
        print('Парикмахер проснулся. Клиентов давно нет. Салон закрылся')

QUEUE_IN_SALON = 2
CLIENT_ENTER_INTERVAL = (3, 4)
if __name__ == '__main__':
    mutex = Lock() #доступ одному клиенту
    clients: list = [Client(str(i)) for i in range(1, 10)] 
    salon = Salon(QUEUE_IN_SALON, mutex) #очередь в салоне
    salon.salon_open() 
    for client in clients:        
        sleep(randint(*CLIENT_ENTER_INTERVAL)) #время ожидания
        salon.door_enter(client)
