# Создать подобие социальной сети. Описать классы, которые должны выполнять соответствующие функции
# (Предлагаю насследовать класс авторизации от класса регистрации).
# Добавить проверку на валидность пароля (содержание символов и цифр), проверка на уникальность логина пользователя.
# Человек заходит, и имеет возможность зарегистрироваться (ввод логин, пароль, потдверждение пароля),
# далее входит в свою учетную запись. Добавить возможность выхода из учетной записи, и вход в новый аккаунт.
# Создать класс User, котоырй должен разделять роли обычного пользователя и администратора.
# При входе под обычным пользователем мы можем добавить новый пост, с определённым содержимим,
# так же пост должен содержать дату публикации.
# Под учётной записью администратора мы можем увидеть всех пользователей нашей системы, дату их регистрации, и их посты.

import shelve
import re


USERS_DB = 'users.db'


def password_validation(password1, password2):
    if password1 == password2:
        if not re.match('^\w+$', password1):
            return 'passwords validation failed'
    else:
        return 'passwords not matched'


def user_validation(username):
    with shelve.open(USERS_DB) as db:
        for cursor in db.items():
            if cursor[1] == username:
                return True
        return None


def get_user_id(username):
    with shelve.open(USERS_DB) as db:
        for cursor in db.items():
            if cursor[1] == username:
                return cursor[0]
        return None


def set_user(username, password1):
    with shelve.open(USERS_DB) as db:
        list_id = []
        for cursor in db.items():
            list_id.append(cursor[0])
        print(max(list_id, default=0)+1)
        db[max(list_id, default=0)+1] = list(username, password1)


def create_user(username, password1, password2):
    if user_validation(username):
        if password_validation(password1, password2):
            set_user(username, password1)
    else:
        print(f'user {username} wasnt created')


class User:
    def __init__(self, username, password):
        self._username = username
        self._password = password
        self._user_id = get_user_id(self._username)

    def __str__(self):
        return f'user : id = {self._user_id}, name = {self._username}'


u1 = User(username='user1', password='user1')
print(u1)