from multiprocessing import Lock, Process
from time import sleep
from random import randint

# timeout - задает время, в течение которого поток будет находиться 
# в заблокированном состоянии при попытке захватить уже занятый Lock-объект. 

class Philosopher(Process):

    wait_forks = 3
    time_to_eat = 1
    THINKING_TIME = (1, 3)
    RUN = True

    def __init__(self, num, right_fork: Lock, left_fork: Lock):
        super().__init__()
        self.num = num
        self.right_fork = right_fork
        self.left_fork = left_fork
    
    def eating(self):
        r_f = self.right_fork
        l_f = self.left_fork
        free_r_fork = r_f.acquire(timeout=Philosopher.wait_forks)
        free_l_fork = l_f.acquire(timeout=Philosopher.wait_forks)

        if free_r_fork:
            print(f'Философ № {self.name} взял правую палочку')

        if free_l_fork:
            print(f'Философ № {self.name} взял левую палочку') 
        else:    
            self.right_fork.release()

        if free_r_fork and free_l_fork:
            print(f'Философ № {self.name} ест')
            sleep(Philosopher.time_to_eat)
            print(f'Философ № {self.name} поел')
            self.right_fork.release()
            self.left_fork.release()
        else:
            print(f'Философ № {self.name} продолжает думать')

    def run(self):
        while self.RUN:
            print(f'Философ № {self.name} думает')
            sleep(randint(*Philosopher.THINKING_TIME))
            print(f'Философ № {self.name} проголодался')
            self.eating()

if __name__ == "__main__":
    philosophers_amount = 5
    forks = [Lock() for _ in range(philosophers_amount)]
    #создаем вилки
    #передаем вилки
    philosophers = [Philosopher (str(num), forks[num % 5], forks[(num - 1) % 5]) for num in range(philosophers_amount)]
    for philosopher in philosophers:
        philosopher.start()
