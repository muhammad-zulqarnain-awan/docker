from flask import Flask, jsonify, request, redirect, url_for

app = Flask(__name__)

items = [
    {"id": 1, "name": "Item One"},
    {"id": 2, "name": "Item Two"},
    {"id": 3, "name": "Item Three"},
    {"id": 4, "name": "Item Four"},
]

# Index Route
@app.route("/", methods=['GET'])
def index():
    return redirect(url_for('get_items'))

# Retrieve all items
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items)

# Retrieve specific item
@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((item for item in items if item['id'] == item_id), None)
    return jsonify(item) if item else ('', 404)

# Add new item
@app.route('/items', methods=['POST'])
def add_item():
    new_item = request.json
    items.append(new_item)
    return jsonify(new_item), 201

# Delete an item
@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    global items
    items = [item for item in items if item["id"] != item_id]
    return ('', 204)

if __name__ == '__main__':
    app.run(debug=True, port=5000, host="0.0.0.0") 