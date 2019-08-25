from mongoengine import *

connect("lesson_10_rest")


class Category(Document):
    """
    Модель категории, которая расширяет модель Item()
    полем name
    """
    name = StringField()

    @property
    def items(self):
        return Item.objects(category=self)


class Item(Document):
    """
    Объект предмета, который ссылается
    на модель категории. У предмета есть название
    и есть описание, так же есть категория
    """
    name = StringField()
    description = StringField()
    category = ReferenceField(Category)

#Создаем объекты
category = Category(name="Cars").save()
item = Item(name="name", description="desc", category=category).save()