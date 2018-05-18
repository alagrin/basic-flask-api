from flask import Flask, request
from flask_restful import Resource, Api

# flask restful removes need for jsonify method

app = Flask(__name__)
app.secret_key = 'secretstuff'
api = Api(app)

items = []

class Item(Resource):
    def get(self, name):
        # Get first item matched by filter function, using next
        # if no item found, return None and 404 error
        item = next(filter(lambda x: x['name'] == name, items), None)
        return {'item': item}, 200 if item else 404

    def post(self, name):
        # If user tries to add same item name, returns message and error
        if next(filter(lambda x: x['name'] == name, items), None) is not None:
            return {'message': "An item with name {} already exists".format(name)}, 400
        data = request.get_json()
        item = {'name': name, 'price': data['price']}
        items.append(item)
        return item, 201 # Created

class ItemList(Resource):
    def get(self):
        return {'items': items}

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')

app.run(port=8001, debug=True)