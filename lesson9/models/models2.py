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

    @classmethod
    def create_new_item(cls, **kwargs):
        new_obj = cls(**kwargs)


item = Item.objects(category="5d5c341438ae9159c0604f43", )
for i in item:
    print(i.id)

item = Item.objects(category_description="z", )
for i in item:
    print(i.id)