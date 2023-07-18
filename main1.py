from bs4 import BeautifulSoup
import lxml
import requests

url = 'https://quotes.toscrape.com/'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')  # скрипт заходит на сайт, получает код странички, причесывает

# распарсить
quotes = soup.find_all('span', class_='text')  # из супа можем вытащить цитаты
authors = soup.find_all('small', class_='author')
tags = soup.find_all('div', class_='tags')

length = len(quotes)

for index in range(length):  # будут попадать цифры от 0 до -1
    print(quotes[index].text)
    print(f'\t\t{authors[index].text}')
    t = tags[index].find_all('a', class_='tag')
    for item in t:
        print(f'\t\t\t#{item.text}')




# for q in quotes:
#     print(q.text)  # вытаскиваем текст из тега

# print(soup)
