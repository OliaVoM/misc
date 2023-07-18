import os
import time
from datetime import datetime
import asyncio

async def dish(num, prepare, wait):
    """

    num:  номер блюда по порядку
    prepare: время на подготовку
    wait: время ожидания готовности
    """
# ниже делаем синхронно
    print(f'В {datetime.now().strftime("%H:%S")} началась подготовка к приготовлению блюда {num}. Требуемое время - {prepare} мин')
    time.sleep(prepare)  # функция задержки
    print(f'Начало приготовления блюда {num} - {datetime.now().strftime("%H:%S")}. Время ожидания блюда {num} составляет {wait} мин')
    await asyncio.sleep(wait)  # функция задержки
    print(f'В {datetime.now().strftime("%H:%S")} блюдо {num} готово')

async def main():
    tasks = [
        asyncio.create_task(dish(1, 2, 3)),
        asyncio.create_task(dish(2, 5, 10)),
        asyncio.create_task(dish(3, 3, 5)),
    ]
    await asyncio.gather(*tasks)

if __name__ == '__main__':
    t0 = time.time()
    if os.name == 'nt':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())
    delta = int(time.time() - t0)  # затраченное время
    print(f'В {datetime.now().strftime("%H:%S")} мы закончили')  # время завершение
    print(f'Затрачено времени - {delta} мин')