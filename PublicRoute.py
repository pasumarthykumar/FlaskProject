from flask import Flask, jsonify

app = Flask(__name__)

public_items = [
    {'id': 1, 'name': 'Public Item 1'},
    {'id': 2, 'name': 'Public Item 2'},
    {'id': 3, 'name': 'Public Item 3'},
]

@app.route('/public_items', methods=['GET'])
def get_public_items():
    return jsonify(public_items), 200

if __name__ == '__main__':
    app.run(debug=True)
