import random
import string
from project.models.cats_and_products import Category, Product, Texts
from mongoengine import connect

random_bool = (True, False)


def random_string(str_len=20):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(str_len))

#print(random_string())


def seed_and_get_categories(num_of_cats):
    category_list = []
    for i in range(num_of_cats):
        cat = Category(title=random_string(),
                       is_parent=random.choice(random_bool)).save()
        category_list.append(cat)
    return category_list


def seed_products(num_of_products, list_of_cats):
    for i in range(num_of_products):
        product = dict(
            title=random_string(),
            description=random_string(),
            price=random.randint(1000, 100*1000),
            quantity=random.randint(0, 100),
            is_available=random.choice(random_bool),
            is_discount=random.choice(random_bool),
            weight = random.uniform(0, 100),
            width = random.uniform(0, 100),
            height = random.uniform(0, 100),
            category=random.choice(list_of_cats),
        )
        Product(**product).save()


if __name__ == '__main__':
    pass
#    connect('bot_shop')
#    cats = seed_and_get_categories(10)
#    seed_products(50, cats)
#    text = dict(
#        title='Greetings',
#        text=random_string(2000)
#    )
#    Texts(**text).save()
