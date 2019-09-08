from mongoengine import *


class User(Document):
    user_id =StringField(max_length=30)
    name = StringField()
    sur_name = StringField()
    nickname = StringField()
    user_state = ImageField()
    # user_cart = ReferenceField(Cart)
