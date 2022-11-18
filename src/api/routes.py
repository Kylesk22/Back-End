"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint

from api.models import db, User, Gym, Posting, user_gym

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

    # query db to find user
    user = User.query.filter_by(email=email).first()
    access_token = create_access_token(identity=user.email)
    gym_id = user.gym_id
    myGym = Gym.query.get(gym_id)
    gym_string = str(myGym)
    if bcrypt.checkpw(password.encode(), user.password.encode()):
        return jsonify(access_token=access_token, user=user.serialize(), gym = gym_string)

    else: 
        return jsonify({"msg": "Bad username or password"}), 401


@api.route('/signup', methods=['POST'])
def create_user():
    request_body = request.get_json()

    password = request_body['password']
    email = request_body['email']
    user = User.query.filter_by(email=email).first()
    if user:
        return jsonify({"msg": "An account has already been made with that email address"}), 401
    hashedPassword = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    new_user = User(
        email = request_body['email'],
        password = hashedPassword.decode("utf-8", "ignore"),
        first_name = request_body['first_name'],
        last_name = request_body['last_name'],
        gym = myGym,
        is_active = True
    )
    db.session.add(new_user)
    db.session.commit()
    access_token = create_access_token(identity=request_body['email'])

    return jsonify(access_token=access_token)

    
    

 


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

@api.route('/post/<string:email>', methods=["POST"])
def create_post(email):
    request_body = request.get_json()
    user = User.query.filter_by(email= email).first()
    post = Posting(
        title = request_body['title'],
        post_info = request_body['content'],
        user_id = user.id
    )
    db.session.add(post)
    db.session.commit()
    return jsonify('hello')

@api.route('/post/<string:email>', methods=["GET"])
def get_posts(email):
    user = User.query.filter_by(email=email).first()
    all_user_posts = user.posts
    all_posts = list(map(lambda x: x.serialize(), all_user_posts))
    reversedList = all_posts[::-1]
    return jsonify(reversedList), 200

@api.route('/post', methods=["GET"])
def get_all_posts():
    posts = Posting.query.all()
    all_posts = list(map(lambda x: x.serialize(), posts))
    return jsonify(all_posts), 200

@api.route('/gym', methods=['POST'])
def gym_signup():
    request_body = request.get_json()
    name = request_body['name']
    gym = Gym(
        name=name
    )
    db.session.add(gym)
    db.session.commit()
    return 'gym added'

@api.route('/gym', methods=["GET"])
def get_all_gyms():
    gyms = Gym.query.all()
    all_gyms = list(map(lambda x: x.serialize(), gyms))
    return jsonify(all_gyms), 200

@api.route('/follow/<string:email>', methods=["POST"])
def follow(email):
    user = User.query.filter_by(email=email).first()
    gym = Gym(
        name="hello"
    )
    user.following.append(gym)
    db.session.commit()
    return 'hello'

@api.route('/follow/gym/<string:email>', methods=["GET"])
def get_user_gym(email):
    user = User.query.filter_by(email=email).first()
    return f'user{user.following}'

@api.route('/gym/followers/<string:name>', methods=["GET"])
def get_gym_followers(name):
    gym = Gym.query.filter_by(name=name).first()
    return f'user{gym.followers}'

@api.route('/user/profiles/<string:gym>', methods=["GET"])

def getGymUsers(gym):
  
    
    all_users = Gym.query.all()
    all_gyms_list = list(map(lambda x: x.serialize(), all_users))
    all_users_list = all_gyms_list[0]['users']
    all_users_list_ser = list(map(lambda x: x.serialize(), all_users_list))
    print(all_users_list_ser)
    print(all_users_list_ser)
    return jsonify(all_users_list_ser)



@api.route('/post/<string:email>', methods=["POST"])
def create_post(email):
    request_body = request.get_json()
    user = User.query.filter_by(email= email).first()
    post = Posting(
        title = request_body['title'],
        post_info = request_body['content'],
        user_id = user.id
    )
    db.session.add(post)
    db.session.commit()
    return jsonify('hello')

@api.route('/post/<string:email>', methods=["GET"])
def get_posts(email):
    user = User.query.filter_by(email=email).first()
    all_user_posts = user.posts
    all_posts = list(map(lambda x: x.serialize(), all_user_posts))
    reversedList = all_posts[::-1]
    return jsonify(reversedList), 200

@api.route('/post', methods=["GET"])
def get_all_posts():
    posts = Posting.query.all()
    all_posts = list(map(lambda x: x.serialize(), posts))
    return jsonify(all_posts), 200

@api.route('/gym', methods=['POST'])
def gym_signup():
    request_body = request.get_json()
    name = request_body['name']
    gym = Gym(
        name=name
    )
    db.session.add(gym)
    db.session.commit()
    return 'gym added'

@api.route('/gym', methods=["GET"])
def get_all_gyms():
    gyms = Gym.query.all()
    all_gyms = list(map(lambda x: x.serialize(), gyms))
    return jsonify(all_gyms), 200

@api.route('/follow/<string:email>', methods=["POST"])
def follow(email):
    user = User.query.filter_by(email=email).first()
    gym = Gym(
        name="hello"
    )
    user.following.append(gym)
    db.session.commit()
    return 'hello'

@api.route('/follow/gym/<string:email>', methods=["GET"])
def get_user_gym(email):
    user = User.query.filter_by(email=email).first()
    return f'user{user.following}'

@api.route('/gym/followers/<string:name>', methods=["GET"])
def get_gym_followers(name):
    gym = Gym.query.filter_by(name=name).first()
    return f'user{gym.followers}'


    

