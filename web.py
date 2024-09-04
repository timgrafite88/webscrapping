import requests
from bs4 import BeautifulSoup
from pprint import pprint

# список ключевых слов
KEYWORDS = ['дизайн', 'фото', 'web', 'python']

URL = 'https://habr.com/ru/articles/'

# Получаем содержимое страницы
response = requests.get(URL)
soup = BeautifulSoup(response.text, 'html.parser')

# Находим все статьи на странице
articles = soup.find_all('article')

# Список для хранения подходящих статей
matching_articles = []

# Проходим по всем статьям
for article in articles:
    # Извлекаем заголовок, ссылку и дату публикации

    # заголовок статьи
    title = article.find('a', class_="tm-title__link").find('span').text

    # ссылка на статью
    small_link = article.find('a', class_="tm-title__link")['href']
    link = f'https://habr.com{small_link}'

    # дата и время публикации
    date_time = article.find('a', class_="tm-article-datetime-published").find('time')['title']

    if any(keyword.lower() in title.lower() for keyword in KEYWORDS):
            matching_articles.append(f"{date_time} – {title} – {link}")

# Выводим подходящие статьи
for article in matching_articles:
    print(article)