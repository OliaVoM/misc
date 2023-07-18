"""Asyncio = модуль асинхронного программирования, который был представлен в Python
http://habr.com/ru/companies/otus/articles/509328
"""

from lib import count_word_at_url
from redis import Redis
from rq import Queue

q = Queue(connection=Redis())  # создаем очередь, именной аргумент connection для организации очереди используется Redis как список ключей и значений
job = q.enqueue(count_word_at_url, 'https://quotes.toscrape.com')  # без () как объект, потом куда gthtlftv

# ставим в очередь, передаем функции и он решает куда