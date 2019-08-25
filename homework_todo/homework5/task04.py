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


def clear_db():
    with shelve.open(USERS_DB) as db:
        db.clear()


def _password_validation(password1, password2):
    if password1 == password2:
        if re.match('^\w+$', password1):
            return True
        else:
            return False  # 'passwords validation failed'
    else:
        return False  # 'passwords not matched'


def _user_validation(username):
    with shelve.open(USERS_DB) as db:
        for cursor in db.items():
            if cursor[1] == username:
                return True
        return None


def _get_user_id(username):
    with shelve.open(USERS_DB) as db:
        for cursor in db.items():
            if cursor[1][0] == username:
                return cursor[0]
        return None


def _set_user(username, password):
    with shelve.open(USERS_DB) as db:
        list_id = []
        for cursor in db.items():
            list_id.append(int(cursor[0]))
        if not list_id:
            list_id.append(0)
        user_id = str(max(list_id)+1)
        db[user_id] = (username, password)


def create_user(username, password1, password2):
    if not _user_validation(username):
        if _password_validation(password1, password2):
            _set_user(username, password1)
            return User(username, password1)
    else:
        print(f'user {username} wasnt created')


class User:
    def __init__(self, username, password):
        self._username = username
        self._password = password
        self._user_id = _get_user_id(self._username)

    def __str__(self):
        return f'user : id = {self._user_id}, name = {self._username}'


clear_db
u1 = create_user('user1', 'user1', 'user1')
print(u1)