"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User, Gym
from api.utils import generate_sitemap, APIException
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
import os
import bcrypt


api = Blueprint('api', __name__)


@api.route("/login", methods=["POST"])
def login():
    email = request.json.get("email", None)
    password = request.json.get("password", None)
    unSaltPass = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(unSaltPass, salt)
    
    checkHashed = hashed.decode("utf-8", "ignore")

    checkEmail = User.query.filter_by(email=email).first()



    
    if checkEmail is not None and bcrypt.checkpw(unSaltPass, checkEmail.password.encode('utf-8')):
        access_token = create_access_token(identity=email)
        gym_id = checkEmail.gym_id
        myGym = Gym.query.get(gym_id)
        gym_string = str(myGym)
        print(myGym)
        return jsonify(access_token=access_token, user=checkEmail.serialize(), gym = gym_string)
    else: 
        return jsonify({"msg": "Bad username or password"}), 401


@api.route('/signup', methods=['POST'])
def create_user():
    request_body = request.get_json()
    unsaltPass = request_body['password'].encode('utf-8')
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(unsaltPass, salt)
    print(unsaltPass)
    print(hashed.decode("utf-8", "ignore"))
    thisGym = request_body['gym']
    myGym = Gym.query.filter_by(gym_name = thisGym).first()
    print(myGym)
    new_user = User(
        email = request_body['email'],
        password = hashed.decode("utf-8", "ignore"),
        first_name = request_body['first_name'],
        last_name = request_body['last_name'],
        gym = myGym,
        is_active = True
    )

    db.session.add(new_user)
    db.session.commit()
    access_token = create_access_token(identity=request_body['email'])
    
    

    return jsonify(access_token=access_token, user = new_user.serialize())

@api.route('/test', methods= ["GET"])
def get_test():
    user = User.query.filter_by(email="v").first()
    print(user.sunday)
    # all_users_list = list(map(lambda x: x.serialize(), user.sunday))
    return jsonify(user.sunday)

@api.route('/signup', methods=["GET"])
def get_user():
    all_users = User.query.all()
    all_users_list = list(map(lambda x: x.serialize(), all_users))
    return jsonify(all_users_list), 200

@api.route('/user/workouts/<string:email>', methods=["POST"])
@jwt_required()
def put_workouts(email):
    request_body= request.get_json()
    user = User.query.filter_by(email= email).first()
    user.sunday = request_body["sunday"]
    user.monday = request_body["monday"]
    user.tuesday = request_body["tuesday"]
    user.wednesday = request_body["wednesday"]
    user.thursday = request_body["thursday"]
    user.friday = request_body["friday"]
    user.saturday = request_body["saturday"]
    

    

    db.session.add(user)
    db.session.commit()

    return jsonify(user.serialize())

@api.route('/user/workouts/<string:email>', methods=["GET"])
@jwt_required()
def get_workouts(email):
    user = User.query.filter_by(email=email).first()
    sunday = user.sunday
    monday = user.monday
    tuesday = user.tuesday
    wednesday = user.wednesday
    thursday = user.thursday
    friday = user.friday
    saturday = user.saturday
    return jsonify(sunday, monday, tuesday, wednesday, thursday, friday, saturday)


@api.route('/user/profiles/<string:gym>', methods=["GET"])

def getGymUsers(gym):
  
    
    all_users = Gym.query.all()
    all_gyms_list = list(map(lambda x: x.serialize(), all_users))
    all_users_list = all_gyms_list[0]['users']
    all_users_list_ser = list(map(lambda x: x.serialize(), all_users_list))
    print(all_users_list_ser)
    print(all_users_list_ser)
    return jsonify(all_users_list_ser)
    

