from mongoengine import *
connect("lesson_9")


class User(Document):
    login = StringField(max_length=30)
    password = StringField(min_length=8)
    email = EmailField(unique=True)
    role = StringField()


class Category(Document):
    title = StringField(max_length=255, unique=True)
    description = StringField(max_length=1024)


class Item(Document):

    added_by = ReferenceField(User)
    category = ReferenceField(Category)
    is_available = BooleanField(default=True)
    name = StringField(required=True, max_length=255)
    description = StringField(max_length=2048, required=False)
    weight = FileField(required=False)


user = {"login": "test_user", "password": "123456789",
        "email": "asasA@ukr.net", "role": "admin"}
user_obj = User(**user)
user = user_obj.save()

print(user.id)

category = {"title": "fruits", "description": "This is fruit"}

category_obj = Category(**category)
category = category_obj.save()

print(category.id)


item = { "added_by": user, "category" : category,
    "is_available": True, "name": "orange"}

item_obj = Item(**item)
item = item_obj.save()

print(item.id)