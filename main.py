"""
Задание:
1) Запросить у пользователя название книги (Оно может быть не полным) и найти по нему все книги которые есть в Google
Books.
2) Добавить в программу возможность фильтровать результат по
  * Автору (Не полное имя автора)
  * Заголовку (Не полный заголовок)
  * Описанию (Не полное описание)
  * Цене (Промежуток от и до)
Пользователя может несколько раз фильтровать один результат поиска в Google Books.
3) Добавить в программу возможность сохранять понравившиеся книги в файл.
5) Удалять книги из файла
6) Помечать как прочитанные книги
7) Отображать книги из файла
Документация по API Google books https://developers.google.com/books/docs/v1/reference/volumes
"""

import requests
import json
from save_users_books import add_book_in_file, delete_book_in_file, indicate_read_book_in_file, show_books_in_file

base_url = 'https://www.googleapis.com/books/v1/volumes?q=intitle:%s'
search_books_list = None


def get_google_books(search):
    resp = requests.get(base_url % search)
    json_resp = json.loads(resp.content)
    if 200 <= resp.status_code <= 299:
        return json_resp
    raise Exception(json_resp['error']['message'])


def book_to_dict(book):
    base_book = {
        'id': '',
        'author': '',
        'title': '',
        'description': '',
        'price': 0.0,
        'buy_link': None,
        'has_it_been_read': False
    }
    if 'id' in book:
        base_book['id'] = book['id']
    if 'volumeInfo' in book:
        if 'title' in book['volumeInfo']:
            base_book['title'] = book['volumeInfo']['title']
        if 'description' in book['volumeInfo']:
            base_book['description'] = book['volumeInfo']['description']
        if 'authors' in book['volumeInfo']:
            base_book['author'] = book['volumeInfo']['authors']
    if 'saleInfo' in book:
        if 'buyLink' in book['saleInfo']:
            base_book['buy_link'] = book['saleInfo']['buyLink']
        if 'listPrice' in book['saleInfo'] and 'amount' in book['saleInfo']['listPrice']:
            base_book['price'] = book['saleInfo']['listPrice']['amount']
    return base_book


def search_books_by_title(title):
    json_resp = get_google_books(title)
    books = [book_to_dict(x) for x in json_resp['items']]
    return books


def filter_search_books():
    while True:
        action = input(menu_filter)
        if action == "1":
            author = input("Введите автора: ")
            for i in range(0, len(search_books_list)):
                if author in search_books_list[i]["author"]:
                    print(search_books_list[i])
            continue
        elif action == "2":
            title = input("Введите заголовок: ")
            for i in range(0, len(search_books_list)):
                if title in search_books_list[i]["title"]:
                    print(search_books_list[i])
            continue
        elif action == "3":
            description = input("Введите описание: ")
            for i in range(0, len(search_books_list)):
                if description in search_books_list[i]["description"]:
                    print(search_books_list[i])
            continue
        elif action == "4":
            while True:
                try:
                    price_from = float(input("Введите цену от: "))
                except ValueError:
                    print('Нужно ввести число')
                    continue
                try:
                    price_up_to = float(input("Введите цену до: "))
                except ValueError:
                    print('Нужно ввести число')
                    continue
                for i in range(0, len(search_books_list)):
                    if price_from < search_books_list[i]["price"] < price_up_to:
                        print(search_books_list[i])
                break
        elif action == "0":
            break


if __name__ == '__main__':
    while True:
        menu = "1 - Поиск книг\n" \
               "2 - Фильтр найденных книг\n" \
               "3 - Сохранить понравившееся книги\n" \
               "4 - Удалять книгу из сохраненных\n" \
               "5 - Помечать книгу как прочитанную\n" \
               "6 - Показать сохраненные книги\n" \
               "0 - Закрыть программу\n--> "
        controls_enter = input(menu)

        if controls_enter == "1":
            books_title = input("Введите название книги: ")
            search_books_list = search_books_by_title(books_title)
            print(search_books_list)
        elif controls_enter == "2":
            menu_filter = "1 - Фильтр по автору\n" \
                          "2 - Фильтр по заголовку\n" \
                          "3 - Фильтр по описанию\n" \
                          "4 - Фильтр по цене\n" \
                          "0 - Закрыть фильтр\n--> "

            filter_search_books()
        elif controls_enter == "3":
            add_book = input("Введите id книги, которую хотите сохранить: ")
            add_book_in_file(add_book, search_books_list)
        elif controls_enter == "4":
            delete_book = input("Введите id книги, которую хотите удалить: ")
            delete_book_in_file(delete_book)
        elif controls_enter == "5":
            read_book = input("Введите id книги, которую хотите отметить как прочитанную: ")
            indicate_read_book_in_file(read_book)
        elif controls_enter == "6":
            show_books_in_file()
        elif controls_enter == "0":
            exit()
        else:
            print("Нет такого действия!")
            continue
