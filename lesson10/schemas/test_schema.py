from marshmallow import Schema, fields, validates, ValidationError
"""
Описываем классы marshmallow для сериализации и
валидации данных с MongoEngine
"""

class Category(Schema):
    """
    Поля в marshmallow классе должны соответствовать
    полям в mongo модели.
    """
    id = fields.String()
    name = fields.String()


class Item(Schema):
    id = fields.String()
    name = fields.String(required=True)
    category = fields.Nested(Category)

    @validates('name')
    def validate_name(self, value):
        """
        Валидируем поле name (оно должно входить
        в список параметров, указаных ниже)
        :param value:
        :return:
        """

        if value not in ["Cars", "Items", "Lolipops"]:
            raise ValidationError("Not in list")
        #Если нет вхождения в список тогда возвращаем
        #json с эррором

