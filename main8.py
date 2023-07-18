import time
from datetime import datetime

def dish(num, prepare, wait):
    """

    num:  номер блюда по порядку
    prepare: время на подготовку
    wait: время ожилания готовности
    """
# ниже делаем синхронно
    print(f'В {datetime.now().strftime("%H:%S")} началась подготовка к приготовлению блюда {num}. Требуемое время - {prepare} мин')
    time.sleep(prepare)  # функция задержки
    print(f'Начало приготовления блюда {num} - {datetime.now().strftime("%H:%S")}. Время ожидания блюда {num} составляет {wait} мин')
    time.sleep(wait)  # функция задержки
    print(f'В {datetime.now().strftime("%H:%S")} блюдо {num} готово')

t0 = time.time()     # засекаем время
dish(1, 2, 3)
dish(2, 5, 10)
dish(3, 3, 5)
delta = int(time.time() - t0)  # затраченное время
print(f'В {datetime.now().strftime("%H:%S")} мы закончили')  # время завершение
print(f'Затрачено времени - {delta} мин')




