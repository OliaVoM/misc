import requests


def count_word_at_url(url):  # считывает число слов по данному адрему
    """это функция для примера как вызывается async"""

    response = requests.get(url)

    print(len(response.text.split()))  # атрибут текст, сплит по пробелу получает список
    return len(response.text.split())
