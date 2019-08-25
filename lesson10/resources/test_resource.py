from flask_restful import Resource
from flask import request
from schemas.test_schema import Item
from models.test_model import Item as Item_model


class Test(Resource):

    def get(self, id=None):
        # dump - сериализует данные
        return Item(many=True).dump(Item_model.objects())

    def post(self):
        #Validate проверяет данные на входе и сравнивает
        #их с параметрами которые описаны в схеме.
        #так же валидирует их
        err = Item().validate(request.json)#Если валидация прошла
        #неуспешно тогда ошибки пишем в объект err
        if err:
            #Если были ошибки тогда их возвращаем
            #json-ом
            return err
        #Если ошибок не было
        new_obj = Item_model(**request.json).save()#Создаем новый
        #объект
        return Item().dump(new_obj)#и сериализуем его

    def put(self, id):
        print("Put request is here")

    def delete(self, id):
        print("Delete request")
