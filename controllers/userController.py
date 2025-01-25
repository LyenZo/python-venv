from models.User import User
from flask import request, jsonify
from config import db

def get_all_user():
    try:
        return [user.to_dict() for user in User.query.all()]
    except Exception as error:
        print()
        return jsonify({
            "error" : error
        })
def create_user(name,email):
    try:
        #name = request.json.get('name')
        #email = request.json.get('email')
        if not name or not email:
            return jsonify({"error": "Faltan campos obligatorios"}), 400
        new_user = User(name=name, email=email)
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"message": "Usuario creado exitosamente", "user": new_user.to_dict()}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
