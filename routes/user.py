from flask import Blueprint, jsonify,request
from controllers.userController import get_all_user,create_user

user_bp = Blueprint('users',__name__)
@user_bp.route('/', methods=['GET'])
def index():
    user = get_all_user()
    return jsonify(user)

@user_bp.route('/create', methods=['POST'])
def add_user():
    data = request.get(jsonify)
    email = data.get('email')
    name =data.get('name')
    print(f"name {name} --- email{email}")
    new_user=create_user(name,email)
    return jsonify(new_user)

