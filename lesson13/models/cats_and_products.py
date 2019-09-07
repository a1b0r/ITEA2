from mongoengine import *

class Category(Document):
    title = StringField(max_length=64)
    sub_category = ListField(ReferenceField('self'))
    is_parent = BooleanField()

    @property
    def category_products(self):
        return Product.objects.filter(categoty=self,
                                      is_avaliable=True)


class Product(Document):
    title = StringField(max_length=64)
    description = StringField(max_length=4096)
    price = IntField(min_value=0)
    quantity = IntField(min_value=0)
    is_available = BooleanField()
    is_discount = BooleanField(default=False)
    category = ReferenceField(Category)
    weight = FloatField(min_value=0, null=True)
    width = FloatField(min_value=0, null=True)
    height = FloatField(min_value=0, null=True)


class Texts(Document):
    title = StringField()
    text = StringField(max_length=4096)

    @classmethod
    def get_text(cls, title):
        return cls.objects.filter(title=title).first().text
