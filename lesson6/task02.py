# Создать свою структуру данных Словарь, которая поддерживает методы, get, items, keys, values.
# Так же перегрузить операцию сложения для словарей, которая возвращает новый расширенный объект.

# Указанные методы описываем самостоятельно, без использования стандартных.

import shelve


class ShelveDictionary:

    def __init__(self, db_name):
        self._db_name = db_name
        with shelve.open(db_name) as db:
            pass

    @property
    def item(self, key):
        with shelve.open(self._db_name) as db:
            for item_key, item_value in db.items():
                if item_key == key:
                    return item_value

    @item.setter
    def item(self, key, value):
        with shelve.open(self._db_name) as db:
            db[key] = (value)

    @item.deleter
    def item(self, key):
        with shelve.open(self._db_name) as db:
            del db[key]


dict1 = StopIteration('task02_db01.db')

dict1.item = ('key01', 'value01')
dict1.item = 'key01'
