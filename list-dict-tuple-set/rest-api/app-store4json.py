from flask import Flask, request
from flask_restful import Resource, Api, reqparse
import simplejson as json

app = Flask(__name__)
api = Api(app)

items = []

class Item(Resource):
    # Get the parser instance to parse for 'price'
    parser = reqparse.RequestParser()
    parser.add_argument('price',
        type=float,
        required=True,
        help="This field cannot be left blank!"
    )

    def save_to_json(self):
        global items
        print("Writing items to JSON file")
        with open('./items.json', 'w') as json_file:
            json.dump(items, json_file, indent=2)

    def read_from_json(self):
        global items
        with open('./items.json', 'r') as json_file:
            items = json.load(json_file, items)
        print(items)

    def get(self, name):
        self.read_from_json()
        return {'item': next(filter(lambda x: x['name'] == name, items), None)}

    def post(self, name):
        if next(filter(lambda x: x['name'] == name, items), None) is not None:
            return {'message': "An item with name '{}' already exists.".format(name)}

        # Use the parser define on line 11 to parse 'price' in data
        # parser is a static data belong to Item class
        data = Item.parser.parse_args()

        item = {'name': name, 'price': data['price']}
        items.append(item)

        self.save_to_json()

        return item

    def delete(self, name):
        global items
        items = list(filter(lambda x: x['name'] != name, items))
        return {'message': 'Item deleted'}

    def put(self, name):
        data = Item.parser.parse_args()
        # Once again, print something not in the args to verify everything works
        item = next(filter(lambda x: x['name'] == name, items), None)
        if item is None:
            item = {'name': name, 'price': data['price']}
            items.append(item)
        else:
            item.update(data)

        self.save_to_json()

        return item

class ItemList(Resource):
    def get(self):
        global items
        with open('./items.json', 'r') as json_file:
            items = json.load(json_file, items)
        print(items)
        return {'items': items}

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')

if __name__ == '__main__':
    app.run(debug=True)  # important to mention debug=True
