from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure the MySQL database connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Wildcrafts%4012@localhost/FLASKDB'
db = SQLAlchemy(app)

# Create a model for your items
class Restaurant(db.Model):
    restaurant_id = db.Column(db.Integer, primary_key=True)
    restaurant_name = db.Column(db.String(100), nullable=False)
    restaurant_description = db.Column(db.String(255), nullable=False)

# Route to create a new Restaurant (POST request)
@app.route('/restaurants', methods=['POST'])
def create_restaurant():
    data = request.get_json()
    if 'restaurant_name' in data and 'restaurant_description' in data:
        new_restaurant = Restaurant(restaurant_name=data['restaurant_name'], restaurant_description=data['restaurant_description'])
        db.session.add(new_restaurant)
        db.session.commit()
        return jsonify(message='Restaurant created successfully'), 201
    else:
        return jsonify(error='Invalid data format'), 400

# Route to retrieve all Restaurants (GET request)
@app.route('/restaurants', methods=['GET'])
def get_restaurants():
    restaurants = Restaurant.query.all()
    restaurant_list = [{'id': restaurant.restaurant_id, 'name': restaurant.restaurant_name, 'description': restaurant.restaurant_description} for restaurant in restaurants]
    return jsonify(restaurants=restaurant_list)

# implement GET, PUT, and DELETE routes for specific items by ID 
@app.route('/restaurants/<int:restaurant_id>', methods=['PUT'])
def update_restaurant(restaurant_id):
    data = request.get_json()
    new_restaurant_name = data.get('restaurant_name')
    new_restaurant_description = data.get('restaurant_description')
    restaurant = Restaurant.query.get(restaurant_id)
    if restaurant is None:
        return jsonify(error='Restaurant not found'), 404
    if new_restaurant_name:
        restaurant.restaurant_name = new_restaurant_name
        restaurant.restaurant_description=new_restaurant_description
        db.session.commit()
        return jsonify(message='Restaurant updated successfully'), 200
    else:
        return jsonify(error='No new restaurant name provided'), 400

# Route to delete a specific restaurants by ID (DELETE request)
@app.route('/restaurants/<int:restaurant_id>', methods=['DELETE'])
def delete_restaurant(restaurant_id):
    restaurant = Restaurant.query.get(restaurant_id)
    if restaurant is not None:
        db.session.delete(restaurant)
        db.session.commit()
        return jsonify(message='Restaurant deleted successfully')
    else:
        return jsonify(error='Restaurant not found'), 404


if __name__ == '__main__':
    app.run(debug=True)
