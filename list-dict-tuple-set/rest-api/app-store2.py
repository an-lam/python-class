from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

stores = [{
    'name': 'Target',
    'items': [{'name': 'chair', 'price': 15.99 }]
     },
    {'name': 'Costco',
    'items': [{'name': 'table', 'price': 45.99 }]}]

@app.route('/')
def home():
  return render_template('index.html')

#post /store data: {name :}
# In postman: Post http://localhost:5000/store
#  Body:
#  {
#	"name": "Walmart"
# }
@app.route('/store' , methods=['POST'])
def create_store():
  request_data = request.get_json()
  new_store = {
    'name':request_data['name'],
    'items':[]
  }
  stores.append(new_store)
  return jsonify(new_store)
  #pass

#get /store/<name> data: {name :}
@app.route('/store/<string:name>')
def get_store(name):
  for store in stores:
    if store['name'] == name:
          return jsonify(store)
  return jsonify ({'message': 'store not found'})
  #pass

#get /store
@app.route('/store')
def get_stores():
  return jsonify({'stores': stores})
  #pass

#post /store/<name> data: {name :}
# In postman: Post http://localhost:5000/store/Target/item
#  Body:
#  {
#	"name": "mouse",
#   "price": 9.50
# }
@app.route('/store/<string:name>/item' , methods=['POST'])
def create_item_in_store(name):
  request_data = request.get_json()
  print(name)
  for store in stores:
    if store['name'] == name:
        new_item = {
            'name': request_data['name'],
            'price': request_data['price']
        }
        store['items'].append(new_item)
        return jsonify(new_item)
  return jsonify ({'message' :'store not found'})
  #pass

#get /store/<name>/item data: {name :}
# Postman: GET: http://localhost:5000/store/Target/items
@app.route('/store/<string:name>/items')
def get_item_in_store(name):
  for store in stores:
    if store['name'] == name:
        return jsonify( {'items':store['items'] } )
  return jsonify ({'message':'store not found'})

  #pass

"""
Point browser to:  localhost:5000/store
"""
app.run(port=5000)