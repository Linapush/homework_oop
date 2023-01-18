#Проблема синхронизации доступа к данным возникает при обращении нескольких потоков к одной и той записи.
#Задача "Читатели-Писатели" заключается в обеспечении согласованного доступа нескольких потоков к разделяемым данным
#операция записи требует эксклюзивного доступа.

from threading import Thread, Lock, Event
from time import sleep
from random import randint, choice

LETTERS_TIMEOUT = (1, 1)
INTERVAL = (4, 5)
PHRASE = [": Что-то интересное.."]
BOOK_LOCK = Lock()
letters_in_book = Event()
book = ''


class Writer(Thread):

    def __init__(self, name: str, line: str, lck_in_book: Lock):
        super().__init__()
        self.name = name
        self.line = line
        self.book_lkc = lck_in_book # (Lock - блокировка, чтобы сменить книгу)

    def run(self):
        global book, letters_in_book
        while True:
            print('Писатель {0} хочет написать в книге {1}'.format(self.name, self.line))
            with self.book_lkc:
                for letter in self.line:
                    book += letter
                    print('Писатель {0} пишет букву {1}'.format(self.name, letter))
                    letters_in_book.set()
                    letters_in_book.clear()
                    sleep(randint(*LETTERS_TIMEOUT))
                book = '' 
            print('Писателю {0} надоело, уходит спать '.format(self.name))
            sleep(randint(*INTERVAL))


class Reader(Thread):

    def __init__(self, name: str):
        super().__init__()
        self.name = name

    def run(self):
        global letters_in_book, read_string #читаем книгу построчно

        while True:
            letters_in_book.wait()
            print('Читатель {0} читает строку {1}'.format(self.name, book))


if __name__ == '__main__':
    thread_writer = [Writer(numbers, choice(PHRASE), BOOK_LOCK) for numbers in range(3)]
    thread_reader = [Reader(numbers) for numbers in range(4)]

    for reader_thr in thread_reader:
        reader_thr.start()

    for writer_thr in thread_writer:
        writer_thr.start()
