from flask import Flask
from flask_restful import Resource, Api

# flask restful removes need for jsonify method

app = Flask(__name__)
api = Api(app)

items = []

class Item(Resource):
    def get(self, name):
        for item in items:
            if item['name'] == name:
                return item
        return {'item': None}, 404 # Not Found

    def post(self, name):
        item = {'name': name, 'price': 12.00}
        items.append(item)
        return item, 201 # Created

class ItemList(Resource):
    def get(self):
        return {'items': items}

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')

app.run(port=8001, debug=True)