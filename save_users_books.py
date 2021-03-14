import json


def add_book_in_file(books_id, search_books_list):
    file = open('./save_books.json', 'r')
    users_books_list = json.loads(file.read())
    file.close()
    for i in range(len(search_books_list)):
        if search_books_list[i]['id'] == books_id:
            users_books_list.append(search_books_list[i])
            file = open('./save_books.json', 'w')
            file.write(json.dumps(users_books_list))
            file.close()
            break
    else:
        print("Нет такой книги!")


def delete_book_in_file(books_id):
    file = open('./save_books.json', 'r')
    users_books_list = json.loads(file.read())
    file.close()
    for i in range(len(users_books_list)):
        if users_books_list[i]['id'] == books_id:
            users_books_list.pop(i)
            file = open('./save_books.json', 'w')
            file.write(json.dumps(users_books_list))
            file.close()
            break
    else:
        print("Нет такой книги!")


def indicate_read_book_in_file(books_id):
    file = open('./save_books.json', 'r')
    users_books_list = json.loads(file.read())
    file.close()
    for i in range(len(users_books_list)):
        if users_books_list[i]['id'] == books_id:
            users_books_list[i]['has_it_been_read'] = True
            file = open('./save_books.json', 'w')
            file.write(json.dumps(users_books_list))
            file.close()
            break
    else:
        print("Нет такой книги!")


def show_books_in_file():
    file = open('./save_books.json', 'r')
    users_books_list = json.loads(file.read())
    file.close()
    for i in range(0, len(users_books_list)):
        print(
            f"id: {users_books_list[i]['id']}\n"
            f"Автор: {users_books_list[i]['author']}\n"
            f"Название книги: {users_books_list[i]['title']}\n"
            f"Описание книги: {users_books_list[i]['description']}\n"
            f"Прочитана: {users_books_list[i]['has_it_been_read']}\n\n"
        )
