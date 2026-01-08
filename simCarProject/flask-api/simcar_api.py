from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api, reqparse, fields, marshal_with, abort

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)
api = Api(app)

class UserModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    charging = db.Column(db.Boolean, nullable=False, default=False)
    battery_health = db.Column(db.Integer, nullable=False, default=0)

    def __repr__(self): # tells object to return a formatted string
        return f"User(name = {self.name}, charging = {self.charging}, battery_health = {self.battery_health})"

user_args = reqparse.RequestParser()
user_args.add_argument('name', type=str, required=True, help="Name cannot be blank")
user_args.add_argument('charging', type=bool, required=False, help="Is it charging?")
user_args.add_argument('battery_health', type=int, required=False, help="What is the battery health?")

userFields = {
    'id':fields.Integer,
    'name':fields.String,
    'charging':fields.Boolean,
    'battery_health':fields.Integer
}

class Users(Resource):
    @marshal_with(userFields)
    def get(self):
        users = UserModel.query.all()
        return users
    
    @marshal_with(userFields)
    def post(self):
        args = user_args.parse_args()
        user = UserModel(name=args["name"], charging=args["charging"], battery_health=args["battery_health"])
        db.session.add(user)
        db.session.commit()
        users = UserModel.query.all()
        return users, 201 # if successfully created
    
class User(Resource):
    @marshal_with(userFields)
    def get(self, id):
        user = UserModel.query.filter_by(id=id).first()
        if not user:
            abort(404, "User not found")
        return user

api.add_resource(Users, '/api/users/')
api.add_resource(User, '/api/users/<int:id>')

@app.route('/', methods=["GET", "POST"])
def home():
    return "<h1>Simulated Car Charging</h1>"

if __name__ == '__main__':
    app.run(debug=True)