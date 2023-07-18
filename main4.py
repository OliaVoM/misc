import threading

def print_cube(num):  # вычисляет куб от заданного числа num
    print(f'Куб {num} -> {num * num * num}')


def print_square(num):  # вычисляет квадрат от заданного числа num
    print(f'Квадрат {num} -> {num ** 2}')  # num ** 2 - возведение в степень

if __name__ == '__main__':  # любой исполняемый скрипт будет main
    # создаем два потока
    thread1 = threading.Thread(target=print_square, args=(10,))  # этот м-д вызывает нашу ф-цию подразумевая,

    # что это какое-то приложение, вызывается всегда аргументами ввиде кортежа
    #  target=print_square передаем как объект, поэтому () не нужны
    thread2 = threading.Thread(target=print_cube, args=(10,))

    thread1.start()  # запуск перового потока
    thread2.start()  # запуск второго потока

    thread1.join()  # ожидание пока поток 1 завершится
    thread2.join()  # ожидание пока поток 2 завершится

    print('Процессы завершены') # процесс один потока два

