from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager, create_access_token, jwt_required,get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Wildcrafts%4012@localhost/FLASKDB'

db = SQLAlchemy(app)
# Set up JWT
app.config['JWT_SECRET_KEY'] = 'ppasumarthy'
jwt = JWTManager(app)

# User model
class User(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   username = db.Column(db.String(50), unique=True, nullable=False)
   password = db.Column(db.String(80), nullable=False)

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    # Query the database to find the user by username
    user = User.query.filter_by(username=username).first()

    if user and user.password == password:
        # If the user exists and the password matches, you can create an access token if needed
        # access_token = create_access_token(identity=username)
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token), 200
    else:
        return jsonify(message='Invalid username or password'), 401

@app.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return jsonify(message=f'Hello, {current_user}! This is a protected resource.')

if __name__ == '__main__':
    app.run(debug=True)
