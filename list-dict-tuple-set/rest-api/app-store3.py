from flask import Flask, request
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

items = []

class Item(Resource):
    parser = reqparse.RequestParser()
    # This parser only parses for 'price' if other data is passed in, they're ignored
    parser.add_argument('price',
        type=float,    # data type of price
        required=True,  # 'price' must be passed in
        help="This field cannot be left blank!"
    )

    def get(self, name):
        # No need to use jsonify because flask_restful
        # for x in items:
        #    if items['name'] == name:
        #       return 'item' : x
        # return None
        return {'item': next(filter(lambda x: x['name'] == name, items), None)}

    def post(self, name):
        # built-in function filter takes a function and an iterable object
        # Purpose: filter the list 'items' using lambda (anonymous) function
        # next -> get the first item matching with 'name'
        if next(filter(lambda x: x['name'] == name, items), None) is not None:
            return {'message': "An item with name '{}' already exists.".format(name)}

        # parser is a class data member of Item (no self needed)
        data = Item.parser.parse_args()

        item = {'name': name, 'price': data['price']}
        items.append(item)
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
        return item

class ItemList(Resource):
    def get(self):
        print("in ItemsList, items = {}".format(items))
        return {'items': items}

# Specify access endpoints for http requests:
# Each resource must be a class
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')

if __name__ == '__main__':
    app.run(debug=True)  # important to mention debug=True
