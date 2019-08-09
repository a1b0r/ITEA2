import shelve

db_name = 'local.db'


def create_item(key, value):
    with shelve.open(db_name) as db:
        db[key] = value

def get_item(key):
    with shelve.open(db_name) as db:

        try:
            result = db[key]
        except KeyError:
            return None

        return result


def delete_item(key):
    with shelve.open(db_name) as db:
        return db.pop(key)


create_item('Name', 'Anton')
create_item('Weather', 'Cloudy')

print(delete_item('Name'))
print(get_item('Name'), get_item('Weather'))

