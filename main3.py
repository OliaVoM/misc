from multiprocessing import Process

def print_func(continent='Asia'):  # функция эмулирует операцию, если бы мы из консоли запускали
    # отдельные процессы с аргументами, ОС запускает каждый процесс отдельно: ф-ция отдельное приложение, с отдельными параметрами
    # каждой было выделена отдельный поток
    # недостаток - всю обязанность возложили на ОС
    print(f'Это - {continent}.')
if __name__ == '__main__':

    names = ['America', 'Europe', 'Africa']
    procs = []  # процессы пустой список
    proc = Process(target=print_func)  # вызов процесс с аргументом по умолчанию
    procs.append(proc)  # добавить
    proc.start()

    for name in names: # в цикле пербираем все и инциируем
        proc = Process(target=print_func, args=(name,))  # (name,) - кортеж
        procs.append(proc)  # для каждого append и запускаем
        proc.start()

    for proc in procs: # все процессы объеденены и запущены параллельно
        proc.join()
