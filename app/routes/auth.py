from flask import Blueprint, request, jsonify
from app.db import db
from app.models import User
from flask_bcrypt import Bcrypt
from flask_jwt_extended import create_access_token
import re

auth_bp = Blueprint('auth', __name__)
#Using Bcrypt to encrypt and protect passwords
bycrypt = Bcrypt()

bycrypt.init_app(auth_bp)

@app.route('/register', methods=["POST"])
def is_valid_password(password):
    #check if password is valid and meets all the requirements
    #must contain atleast one Special character and have a length of at least 8
    password_regex = r'^(?=.*[W_]).{8,}$'
    return re.match(password_regex, password) is not None
    
    
def is_vaild_email(email):
    #check if email is valid
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None
def register():
    #processing the JSON request from the HTTP POST request
    data = request.get_json()
    #If user makes POST request, then create a new user
    if not data.get("username") or not data.get("password") or not data.get("email"):
        return jsonify({"message: Missing required fields"}), 400
    
    #check if user is already registered
    user = User.query.filter_by(username=data['username']).first()
    if user:
        return jsonify({"message": "User already exists"}), 400
        
    hashed_password = bcrypt.generate_password_hash(data["password"]).decode("utf-8")
    
    new_user = User(username=data["username"],email=data["email"],password=hashed_password)
    db.session.add(new_user)
    db.session.commit()
    
    
    return jsonify({"message: User created successfully"}), 201


@auth_bp.route('login', methods=["POST"])

def login():
    
    data = request.get_json()
    
    # Check to make all the fields are filled
    if not data.get("username") or not data.get("password"):
        return jsonify({"message: Missing required fields"}), 400
    
    #Check if the user exist by the username then check the password
    user = User.query.filter_by(username=data["username"]).first()
    if not user or not bcrypt.check_password(user.password, data["password"]):
        return jsonify({"message": "Invalid username or password"}), 401
    
    #Generate an JWT token 
    access_token = create_access_token(identity=user.id)
    
    return jsonify({"access_token": access_token}), 200
    