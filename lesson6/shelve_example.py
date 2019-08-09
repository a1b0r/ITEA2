import shelve

db_name = 'local.db'

with shelve.open(db_name) as db:
    db['Country'] = ('Ukraine', 'USA', 'UK')

    for c in db.items():
        print(c)

    for c in db.keys():
        print(c)

    for c in db.values():
        print(c)
