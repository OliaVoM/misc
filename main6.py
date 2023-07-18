"""Asyncio = модуль асинхронного программирования, который был представлен в Python
http://habr.com/ru/companies/otus/articles/509328
"""
import signal
import sys
import json
import asyncio
import aiohttp

loop = asyncio.get_event_loop()  # событийный цикл регистрирует, обрабатывает, созд. очередь
client = aiohttp.ClientSession(loop=loop) # клиент циклится на loop = asyncio.get_event_loop(), теперь везде пишем

async def get_json(client, url):
    async with client.get(url) as response:
        assert response.status == 200  # если это так поднимается исключение 200,то ставим ожидание 200, получаем ответ и ждем
        return await response.read()

async def get_reddit_top(subreddit, client): # мы будем читать json сортировать будет его потоку ? запрос методом get % разделяет параметры
    url = 'https://www.reddit.com/r/' + subreddit + '/top.json?sort=top&t=day&limit=5'
    data1 = await get_json(client, url)
    j = json.loads(data1.decode('utf-8'))  # чтобы инфо была читабельной
    for i in j['data']['children']:
        score = i['data']['score']  # все идете через data - ключ
        title = i['data']['title']
        link = i['data']['url']
        print(str(score) + ': ' + title + ' (' + link + ')')
    print('Готово:', subreddit + '\n')

def signal_handler(signal, frame):
    loop.stop()
    client.close()
    sys.exit(0)   # системный выход с возвращением системе 0

signal.signal(signal.SIGINT, signal_handler)
"""каждую ссылку выполняет параллельно из-за префикса asyncio, загружаются одновременно не ждут друг друга
Ассинхронность действий одно не ждут другое, каждая фунция выполняется отдельно
подзадачи рассматриваются как корутины и выполняются отдельно
одна ф-ция получает json читает страницы распарсивает и печатает нам страницу"""
# asyncio.ensure_future(get_reddit_top('python', client))
asyncio.ensure_future(get_reddit_top('programming', client))
asyncio.ensure_future(get_reddit_top('compsci', client))

loop.run_forever()


