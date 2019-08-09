import shelve

db_name = 'local.db'


def create_item(key, value, id):
    with shelve.open(db_name) as db:
        db[f'User_{id}'] = value


def get_item(id):
    with shelve.open(db_name) as db:

        try:
            result = db[f'User_{id}']
        except KeyError:
            return None

        return result


def delete_item(key):
    with shelve.open(db_name) as db:
        return db.pop(key, None)


def clear_db():
    with shelve.open(db_name) as db:
        db.clear()


create_item('Name', 'Anton')
create_item('Weather', 'Cloudy')

print(delete_item('Name'))
print(get_item('Name'), get_item('Weather'))

clear_db()
print(get_item('Name'), get_item('Weather'))
